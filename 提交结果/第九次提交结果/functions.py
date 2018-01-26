
# coding: utf-8

# In[1]:

import pandas as pd
import numpy as np
import os
os.chdir(r'C:\Users\May\Desktop\ai')


# In[2]:

#自定义程序
#排序
def sort(df, *args, **kwargs):
    try:
        return df.sort_values(*args, **kwargs)
    except AttributeError:
        return df.sort(*args, **kwargs)


# In[ ]:



