
# coding: utf-8

# In[14]:

import pandas as pd
import numpy as np
import os
os.chdir(r'C:\Users\May\Desktop\ai')
from functions import sort 




# In[41]:


def action_statistics(action_path,outputpath):

    cm_data_raw=pd.read_table(action_path,sep=',',encoding='utf-8')
    #对user action data 进行统计处理。

    names=['userid','actionType','actionTime']
    
    newCust=pd.DataFrame(columns=["userid",'totalstep','step1N','step2N','step3N','step4N',
                            'step5N','step6N','step7N','step8N','step9N','step1P','step2P','step3P','step4P',
                            'step5P','step6P','step7P','step8P','step9P','viewProductN','last1time','last2time','last3time','last4time',
                            'last5time','last6time','last7time','last8time','last9time','buy/viewProductN','buy/n5','(2-4)/(1)',
                            'tail1','tail2','tail3','tail4','head1',
                            'maxtime','mintime','averagetime','vartime','mediantime','tailtime1','tailtime2','tailtime3','tailtime4','tail3ave','tail3var'])
    idlist=[]


    for i in range(0,len(cm_data_raw)):
        record=cm_data_raw.iloc[i]
        uid=record['userid']

        if uid not in idlist:
            idlist.append(uid)
            udata=cm_data_raw[cm_data_raw['userid']==uid]
            udata=sort(udata,["actionType","actionTime"],ascending=False)
            
            #总步数为
            totalStep=0
  
            #记录每一步击中数量
            n1=0
            n2=0
            n3=0
            n4=0
            n5=0
            n6=0
            n7=0
            n8=0
            n9=0
            #记录每一步击中数量比例
            p1=0
            p2=0
            p3=0
            p4=0
            p5=0
            p6=0
            p7=0
            p8=0
            p9=0
            #第一次击中步骤时间标签。用于识别最近一次到达此步骤。
            f1=0
            f2=0
            f3=0
            f4=0
            f5=0
            f6=0
            f7=0
            f8=0
            f9=0
            #第一次击中某一步骤的时间
            t1=0
            t2=0
            t3=0
            t4=0
            t5=0
            t6=0
            t7=0
            t8=0
            t9=0
            
            #倒数几步为何总总type
            tail1=0
            tail2=0
            tail3=0
            tail4=0
            #第一步为何type
            head1=0
            #时间间隔初始化
            timeslot=[]
            times1=0
            ptime=0
            ctime=0
            #时间间隔相关统计
            maxtime=0
            mintime=0
            averagetime=0
            vartime=0
            mediantime=0
            #倒数实践间隔
            tail3a=[]
            tailtime1=0
            tailtime2=0
            tailtime3=0
            tailtime4=0
            
            tail3ave=0
            tail3var=0

            
            
            
            
            
            #对一个用户行为数据信息进行统计
            for j in range(0,len(udata)):
                
            

                oudata=udata.iloc[j]
                #倒数的type
                if j==0:
                    tail1=oudata['actionType']
                    tailtime1=oudata['actionTime']
                if j==1:
                    tail2=oudata['actionType']
                    tailtime2=oudata['actionTime']
                
                if j==2:
                    tail3=oudata['actionType']
                    tailtime3=oudata['actionTime']
                
                if j==3:
                    tail4=oudata['actionType']
                    tailtime4=oudata['actionTime']
                
                
                #每个行为每个用户使用过几次
                if oudata['actionType']==1:
                    n1=n1+1
                    if f1==0:
                        f1=2
                        t1=oudata['actionTime']
                if oudata['actionType']==2:
                    n2=n2+1
                    if f2==0:
                        f2=2
                        t2=oudata['actionTime']
                        
                if oudata['actionType']==3:
                    n3=n3+1
                    if f3==0:
                        f3=2
                        t3=oudata['actionTime']
                if oudata['actionType']==4:
                    n4=n4+1
                    if f4==0:
                        f4=2
                        t4=oudata['actionTime']
                        
                        
                        
                        
                        
                if oudata['actionType']==5:
                    n5=n5+1
                    if f5==0:
                        f5=2
                        t5=oudata['actionTime']
                        
                
                
                if oudata['actionType']==9:
                    n9=n9+1
                    if f9==0:
                        f9=2
                        t9=oudata['actionTime']
                if oudata['actionType']==8:
                    n8=n8+1
                    if f8==0:
                        f8=2
                        t8=oudata['actionTime']
                if oudata['actionType']==7:
                    n7=n7+1
                    if f7==0:
                        f7=2
                        t7=oudata['actionTime']
                if oudata['actionType']==6:
                    n6=n6+1
                    if f6==0:
                        f6=2
                        t6=oudata['actionTime']
                        
                if oudata['actionType']==5:
                    n5=n5+1
                    if f5==0:
                        f5=2
                        t5=oudata['actionTime']
                head1=oudata['actionType']
                
                
                
                 #进行时间间隔计算
                if j!=0:
                    ctime=oudata['actionTime']
                    times1=ctime-ptime
                    ptime=ctime
                    timeslot.append(times1)
                    
                else:
                    ptime=oudata['actionTime']
               
                if len(timeslot)!=0:
                    maxtime=np.max(timeslot)
                    mintime=np.min(timeslot)

                    averagetime=np.average(timeslot)
                    mediantime=np.median(timeslot)
                    vartime=np.var(timeslot)
                    tail3a=timeslot[-3:]
                    tail3ave=np.average(tail3a)
                    tail3var=np.var(tail3a)
                    
                
            
                        
                        
                    
            if n2+n3+n4 !=0:
                buy_viewProductN=n9/(n2+n3+n4)
            elif n9==0:
                buy_viewProductN=0
            elif n9!=0 and n2+n3+n4 ==0:
                buy_viewProductN=1

            if n5 !=0:
                buy_5=n9/n5
            else: 
                buy_5=0


            if n2+n3+n4 !=0:
                p59_24=(n5+n6+n7+n8+n9)/(n2+n3+n4)
            else: 
                p59_24=1

            if p59_24>1:
                p59_24=1


            if n1!=0:
                p24_1=(n2+n3+n4)/n1
            else: 
                p24_1=0

            totalStep=n1+n2+n3+n4+n5+n6+n7+n8+n9
            p1=n1/totalStep
            p2=n2/totalStep
            p3=n3/totalStep
            p4=n4/totalStep
            p5=n5/totalStep
            p6=n6/totalStep
            p7=n7/totalStep
            p8=n8/totalStep
            p9=n9/totalStep


                
                    
                    
                    
            finalud={"userid":uid,'totalStep':totalStep,'step1N':n1,'step2N':n2,'step3N':n3,'step4N':n4,
                     'step5N':n5,'step6N':n6,'step7N':n7,'step8N':n8,
                     'step9N':n9,'step1P':p1,'step2P':p2,'step3P':p3,'step4P':p4,
                     'step5P':p5,'step6P':p6,'step7P':p7,'step8P':p8,'step9P':p9,
                     'viewProductN':n2+n3+n4,'last1time':t1,'last2time':t2,'last3time':t3,
                     'last4time':t4,'last5time':t5,'last6time':t6,'last7time':t7,'last8time':t8,
                     'last9time':t9,'buy/viewProductN':buy_viewProductN,'buy/n5':buy_5,'(2-4)/(1)':p24_1,
                     'tail1':tail1,'tail2':tail2,'tail3':tail3,'tail4':tail4,'head1':head1,
                     'maxtime':maxtime,'mintime':mintime,'averagetime':averagetime,'vartime':vartime,'mediantime':mediantime,
                     'tailtime1':tailtime1,'tailtime2':tailtime2,'tailtime3':tailtime3,'tailtime4':tailtime4,'tail3ave':tail3ave,'tail3var':tail3var}
            
            newCust=newCust.append(finalud,ignore_index=True)
        
    newCust.to_csv(outputpath)
                
                        
                
    return
                
                


    


# In[42]:

action_statistics(r'train_set\action_train.csv',r'action_stantistics.csv')


# In[43]:

action_statistics(r'test\action_test.csv',r'action_stantistics_test.csv')


# In[ ]:



