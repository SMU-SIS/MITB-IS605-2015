# MITB-IS605-2015
IS605 Cloud Computing and Big Data Analytics 2015


## 12 Oct In Class Demo
### Starting a tmpnb server on Amazon EC2

`export TOKEN=$( head -c 30 /dev/urandom | xxd -p )`

`sudo service docker start`

`sudo docker run --net=host -d -e CONFIGPROXY_AUTH_TOKEN=$TOKEN --name=proxy jupyter/configurable-http-proxy --default-target http://127.0.0.1:9999`

`sudo docker pull waituck/custom_nb`

`sudo docker run --net=host -d -e CONFIGPROXY_AUTH_TOKEN=$TOKEN -v /var/run/docker.sock:/docker.sock -v /var/run/docker.sock:/docker.sock jupyter/tmpnb python orchestrate.py --image='waituck/custom_nb' --pool_size=10 --command="ipython notebook --NotebookApp.base_url={base_path} --ip=0.0.0.0 --port {port}"`
