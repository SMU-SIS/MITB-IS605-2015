
# coding: utf-8

# In[25]:

import pandas as pd
from pandas import *
import pylab as pyl
from pylab import *
import csv
import numpy as np
import matplotlib.pyplot as plt
from pandas import DataFrame

get_ipython().magic('matplotlib inline')

crimes=pd.read_csv('crimes2.csv')
crimes.head()


#crimes1=crimes['Year'].value_counts()
#crimes1
#crimes2=crimes['Location Description'].value_counts()
#crimes2
#crimes2.plot(kind='barh')

crimes['Arrest']=='False'


# In[ ]:



