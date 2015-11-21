
# coding: utf-8

# In[21]:

import pandas as pd
from pandas import *
import pylab as pyl
from pylab import *
import csv
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')
get_ipython().magic('matplotlib inline')

df=pd.read_csv('crimes2 - Copy.csv')
df.head()

crimes2=df[['Location Description','Primary Type','FBI Code','Year']]
crimes2.head()
category_group=crimes2.groupby(['Location Description','Primary Type']).sum()
category_group.head()
category_group.unstack().head()






my_plot = category_group.unstack().plot(kind='bar',stacked=True,title="Total Sales by Customer")
my_plot.set_xlabel("Customers")
my_plot.set_ylabel("Sales")

# In[23]:

my_plot = category_group.unstack().plot(kind='bar',stacked=True,title="Total Sales by Customer")
my_plot.set_xlabel("Crimes")
my_plot.set_ylabel("Number")


# In[ ]:



