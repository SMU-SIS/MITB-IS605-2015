#!/bin/bash

sudo service docker restart;

sudo docker rm proxy;
sudo docker rm tmpnb;

export TOKEN=$( head -c 30 /dev/urandom | xxd -p );

sudo docker run --net=host -d -e CONFIGPROXY_AUTH_TOKEN=$TOKEN --name=proxy jupyter/configurable-http-proxy --default-target http://127.0.0.1:9999;

sudo docker run --net=host -d -e CONFIGPROXY_AUTH_TOKEN=$TOKEN \
           -v /var/run/docker.sock:/docker.sock \
           jupyter/tmpnb python orchestrate.py --image='waituck/custom_nb' --command="ipython notebook --NotebookApp.base_url={base_path} --ip=0.0.0.0 --port {port}";
           clear


           a=$(curl http://169.254.169.254/latest/meta-data/public-ipv4 | grep -E '[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}')
           b="$a:8000"
           clear
           echo "Your tmpnb server is ready at $b"
