
# coding: utf-8

# In[49]:

import pandas as pd
import numpy as np
import os
os.chdir(r'C:\Users\May\Desktop\ai')
'''
from functions import sort 
from rating_stantistics import rating_stantistics
from userprofile_and_orderhistory import up_oh_statistics
from user_actions import action_statistics
'''


# In[50]:

#计算训练集各个表统计结果
rating_stantistics(r'train_set\userComment_train.csv',r'rating_stantistics.csv')
#输出order history 统计结果
up_oh_statistics(r'train_set\userProfile_train.csv',r'train_set\orderHistory_train.csv','up_oh_stantistics_result.csv')
action_statistics(r'train_set\action_train.csv',r'action_stantistics.csv')


# In[61]:

#读取training数据统计结果。
future_train =pd.read_table(r'train_set\orderFuture_train.csv',sep=',',encoding='utf-8')
up_oh_train=pd.read_table(r'up_oh_stantistics_result.csv',sep=',',encoding='utf-8')
action_train=pd.read_table(r'action_stantistics.csv',sep=',',encoding='utf-8')
rating_train=pd.read_table(r'rating_stantistics.csv',sep=',',encoding='utf-8')

#读取test数据统计结果。
future_test =pd.read_table(r'test\orderFuture_test.csv',sep=',',encoding='utf-8')
up_oh_test=pd.read_table(r'up_oh_stantistics_result_test.csv',sep=',',encoding='utf-8')
action_test=pd.read_table(r'action_stantistics_test.csv',sep=',',encoding='utf-8')
rating_test=pd.read_table(r'rating_stantistics_test.csv',sep=',',encoding='utf-8')


# In[62]:

#由future order 为原表建立大宽表
data_1=pd.merge(future_train,up_oh_train,how='left',on='userid',left_index=False, right_index=False)
data_2=pd.merge(data_1,rating_train,how='left',on='userid',left_index=False, right_index=False)
data_3=pd.merge(data_2,action_train,how='left',on='userid',left_index=False, right_index=False)
data_3.drop(['Unnamed: 0_y','Unnamed: 0','Unnamed: 0_x'], axis=1,inplace=True)
#由future order 为原表建立test大宽表
test_data_1=pd.merge(future_test,up_oh_test,how='left',on='userid',left_index=False, right_index=False)
test_data_2=pd.merge(test_data_1,rating_test,how='left',on='userid',left_index=False, right_index=False)
test_data_3=pd.merge(test_data_2,action_test,how='left',on='userid',left_index=False, right_index=False)
test_data_3.drop(['Unnamed: 0_y','Unnamed: 0','Unnamed: 0_x'], axis=1,inplace=True)


# In[64]:


data=data_3.drop(['orderType'], axis=1)
label=data_3['orderType']

data_test=test_data_3
data_test.to_csv('test_data_all.csv')
data_3.to_csv('train_data_all.csv')


# In[65]:


import xgboost as xgb
# read in data
dtrain = xgb.DMatrix(data,label)
#dtest = xgb.DMatrix('demo/data/agaricus.txt.test')
# specify parameters via map
param = {'max_depth':2, 'eta':1, 'silent':1, 'objective':'binary:logistic' }
num_round = 5
bst = xgb.train(param, dtrain, num_round)

dtest = xgb.DMatrix(data_test)
preds = bst.predict(dtest)


# In[67]:

result=preds.tolist()
fr=result

for i in range(0,len(result)):
    if result[i]>0.3:
        fr[i]=1
    else:
        fr[i]=0



# In[69]:

np.savetxt('finalresultwith01.csv', fr, delimiter = ',') 


# In[58]:




# In[ ]:



