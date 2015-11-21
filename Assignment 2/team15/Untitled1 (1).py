
# coding: utf-8

# In[42]:

import pandas as pd
from pandas import *
import pylab as pyl
from pylab import *
import csv
import numpy as np
import matplotlib.pyplot as plt
from pandas import DataFrame

get_ipython().magic('matplotlib inline')

df=pd.read_csv('crimes2.csv')
df.head()
crime2=pd.pivot_table(df,index=['Year','Location Description'])
#crime2.plot(kind='bar')

a=df['Location Description']=='BAR OR TAVERN'

temp3 = pd.crosstab(df['Primary Type'], df.Arrest.astype(bool))
temp3.plot(kind='bar', stacked=True, color=['red','blue'], grid=False)






# In[ ]:



