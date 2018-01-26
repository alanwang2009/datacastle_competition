
# coding: utf-8

# In[20]:

import pandas as pd
import numpy as np
import os
os.chdir(r'C:\Users\May\Desktop\ai')
from functions import sort


# In[21]:

#数据预处理


def datatonumber(uppath,ohpath):
    #将userprofile 中中文mapping为数字   
    up_data_raw=pd.read_table(uppath,sep=',',encoding='utf-8')
    agemapping=pd.read_table(r'mapping\agemapping.csv',sep=',',encoding='utf-8')
    gendermapping=pd.read_table(r'mapping\gendermapping.csv',sep=',',encoding='utf-8')
    provincemapping=pd.read_table(r'mapping\provincemapping.csv',sep=',',encoding='utf-8')
    up_data_1=pd.merge(up_data_raw,agemapping,how='left',on='age')
    up_data_2=pd.merge(up_data_1,gendermapping,how='left',on='gender')
    up_data_3=pd.merge(up_data_2,provincemapping,how='left',on='province')

    columns=['userid','genderN','ageN','provinceN']
    up_data=up_data_3[columns]


    #orderhistory 中中文mapping为数字

    continentmapping=pd.read_table(r'mapping\continentmapping.csv',sep=',',encoding='utf-8')
    countrymapping=pd.read_table(r'mapping\countrymapping.csv',sep=',',encoding='utf-8')
    citymapping=pd.read_table(r'mapping\citymapping.csv',sep=',',encoding='utf-8')

    oh_data_raw=pd.read_table(ohpath ,sep=',',encoding='utf-8')
    oh_data_1=pd.merge(oh_data_raw,continentmapping,how='left',on='continent')
    oh_data_2=pd.merge(oh_data_1,countrymapping,how='left',on='country')
    oh_data_3=pd.merge(oh_data_2,citymapping,how='left',on='city')

    columns=['userid','orderid','orderTime','orderType','cityN','countryN','continentN']
    oh_data=oh_data_3[columns]

    return oh_data,up_data











# In[ ]:





# In[13]:

def up_oh_statistics(up_path,oh_path,outputpath):

    up_op_data=datatonumber(up_path,oh_path)
    up_data=up_op_data[1]
    oh_data=up_op_data[0]
    #对orderhistory data 进行统计处理。

    names=['userid','orderid','orderTime','orderType','contientN','cityN','countryN']
    prev_cus_id='0'
    newCust=pd.DataFrame(columns=["userid",'nearestOrderTime','nearestCity','nearestCountry','nearestContinent',
                            'totalOrder','numberOftype0ne','typeOnePer','numberofCity',
                        'numberofCountry','NumberofU','NumberofNA','NumberofA','NumberofO',
                        'NumberofAF','NumberofSA'])
    idlist=[]


    for i in range(0,len(oh_data)):
        record=oh_data.iloc[i]
        uid=record['userid']

        if uid not in idlist:
            idlist.append(uid)
            udata=oh_data[oh_data['userid']==uid]
            udata=sort(udata,["orderTime","orderType"],ascending=False)
            prv_time=[]

            totalOrder=0
            numberOftype0ne=0
            numberofCity=0
            numberofCountry=0
            NumberofU=0
            NumberofA=0
            NumberofNA=0
            NumberofSA=0
            NumberofAF=0
            NumberofO=0
            cityList=[]
            countryList=[]
            #对一个用户历史信息进行统计
            for j in range(0,len(udata)):

                oudata=udata.iloc[j]
                odtime=oudata['orderTime']
                ot=oudata['orderType']
                ct=oudata['cityN']
                coun=oudata['countryN']
                cn=oudata['continentN']


                 #最近一次去过的城市，国家，以及大洲,因为之前userdata 按照时间大小排序，所以第一个就是最近的订单
                if j==0:
                    nearestCity=ct
                    nearestCou=coun
                    nearestCn=cn 
                    nearestOd=odtime


                if odtime not in prv_time:
                    prv_time.append(odtime)
                    #总订单数，同一时间订单视为父子订单只计一个订单
                    totalOrder=totalOrder+1
                    #精品游订单数量统计
                    if ot==1:
                        numberOftype0ne=numberOftype0ne+1
                    #去过的城市列表，用于计算去过几个城市
                    if ct not in cityList:
                        cityList.append(ct)
                    #去过的国家列表，用于计算去过几个国家
                    if coun not in countryList:
                        countryList.append(coun)
                    #去过各个大洲几次
                    if cn=='U':
                        NumberofU=NumberofU+1
                    if cn=='NA':
                        NumberofNA=NumberofNA+1
                    if cn=='A':
                        NumberofA=NumberofA+1
                    if cn=='O':
                        Numberof0=NumberofO+1
                    if cn=='AF':
                        NumberofAF=NumberofAF+1
                    if cn=='SA':
                        NumberofSA=NumberofSA+1

            finalud={'userid':uid,'nearestOrderTime':nearestOd,'nearestCity':nearestCity,'nearestCountry':nearestCou,'nearestContinent':nearestCn,
                            'totalOrder':totalOrder,'numberOftype0ne':numberOftype0ne,'typeOnePer':numberOftype0ne/totalOrder,'numberofCity':len(cityList),
                        'numberofCountry':len(countryList),'NumberofU':NumberofU,'NumberofNA':NumberofNA,'NumberofA':NumberofA,'NumberofO':NumberofO,
                        'NumberofAF':NumberofAF,'NumberofSA':NumberofSA}

            newCust=newCust.append(finalud,ignore_index=True)
    #用order history 统计好的表left join user profile表得出一个新表并输出
    up_oh_data=pd.merge(up_data,newCust,how='outer',on='userid')
    data_1=up_oh_data[['genderN','provinceN','nearestCity','nearestCountry','nearestContinent']]
    data_2=pd.get_dummies(data_1)
    result_1=pd.concat([up_oh_data,data_2],axis=1)
    result_1.drop(['genderN','provinceN','nearestCity','nearestCountry','nearestContinent'], axis=1,inplace=True)
    result_1.to_csv(outputpath)
    return




# In[ ]:

#输出order history 统计结果
up_oh_statistics(r'train_set\userProfile_train.csv',r'train_set\orderHistory_train.csv','up_oh_stantistics_result.csv')


# In[24]:


#输出order history 统计结果
up_oh_statistics(r'test\userProfile_test.csv',r'test\orderHistory_test.csv','up_oh_stantistics_result_test.csv')


# In[ ]:



