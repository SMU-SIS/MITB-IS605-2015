
# coding: utf-8

# In[36]:

import pandas as pd
from pandas import *
import pylab as pyl
from pylab import *
import csv
import numpy as np
import matplotlib.pyplot as plt

get_ipython().magic('matplotlib inline')

crimes=read_csv('crimes2.csv')
crimes.head()

#crimes.shape
#crimes.dtypes
#rimes1=crimes['Location Description'].value_counts()
#rimes1







#crimes2=crimes[['Year','Location Description']]
#group=crimes2.groupby('Location Description')
#group.size()
#crimes2=group.sum()
#crimes2.sort(columns='Year').head()
#my_plot = crimes2.plot(kind='bar', color='Navy')



# In[ ]:



