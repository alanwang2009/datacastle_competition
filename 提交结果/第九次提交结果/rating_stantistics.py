
# coding: utf-8

# In[14]:

import pandas as pd
import numpy as np
import os
os.chdir(r'C:\Users\May\Desktop\ai')
from functions import sort 




# In[15]:

def rating_stantistics(inputpath,outputpath):
    cm_data_raw=pd.read_table(inputpath,sep=',',encoding='utf-8')
    #对user action data 进行统计处理。

    
    newCust=pd.DataFrame(columns=["userid",'totalrate','totalnumber','averate','numberof1','numberof2','numberof3',
                                  'numberof367','numberof433','numberof4','numberof5','lowrate','highrate'])
    idlist=[]


    for i in range(0,len(cm_data_raw)):
        record=cm_data_raw.iloc[i]
        uid=record['userid']

        if uid not in idlist:
            idlist.append(uid)
            udata=cm_data_raw[cm_data_raw['userid']==uid]
            udata=sort(udata,["orderid"],ascending=False)
            
            #记录总分数
            totalrate=0
            totalnumber=0
            averate=0
            
            numberof5=0
            numberof1=0
            numberof2=0
            numberof3=0
            numberof367=0
            numberof433=0
            numberof4=0
            #3分及其以下为low rate,求其数量
            lowrate=0
            #4分及其以上为高分
            highrate=0
            
            
            
            

          
            #对一个用户评分信息进行统计
            for j in range(0,len(udata)):

                oudata=udata.iloc[j]
                totalrate=totalrate+oudata['rating']
                totalnumber=totalnumber+1
                
                if j==0:
                    nr=oudata['rating']
                
                #统计用户评分
                if oudata['rating']==1:
                    numberof1=numberof1+1
                    lowrate=lowrate+1
                    
                if oudata['rating']==2:
                    numberof2=numberof2+1
                    lowrate=lowrate+1
                if oudata['rating']==3:
                    numberof3=numberof3+1
                    lowrate=lowrate+1
                if oudata['rating']==3.67:
                    numberof367=numberof367+1
                if oudata['rating']==4.33:
                    numberof367=numberof433+1
                    
                if oudata['rating']==4:
                    numberof4=numberof4+1
                    
                if oudata['rating']==5:
                    numberof5=numberof5+1
                    
                   
                    
            
                    
                    
                    
            averate=  totalrate/totalnumber
            lowrate=numberof1+numberof2+numberof3
            highrate=numberof4+numberof5+numberof433
            
            
            
                    
                    
                    
                    
                    
            finalud={"userid":uid,'totalrate':totalrate,'totalnumber':totalnumber,'averate':averate,'numberof1':numberof1,
                            'numberof2':numberof2,'numberof3':numberof3,'numberof367':numberof367,'numberof433':numberof433,
                        'numberof4':numberof4,'numberof5':numberof5,'lowrate':lowrate,'highrate':highrate}

            newCust=newCust.append(finalud,ignore_index=True)
        
    newCust.to_csv(outputpath)
                
                        
                
    return
                









# In[16]:

rating_stantistics(r'train_set\userComment_train.csv',r'rating_stantistics.csv')


# In[ ]:



