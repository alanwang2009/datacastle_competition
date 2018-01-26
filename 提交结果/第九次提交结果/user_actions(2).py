
# coding: utf-8

# In[14]:

import pandas as pd
import numpy as np
import os
os.chdir(r'C:\Users\May\Desktop\ai')
from functions import sort 




# In[59]:


def action_statistics(action_path,outputpath):

    cm_data_raw=pd.read_table(action_path,sep=',',encoding='utf-8')
    #对user action data 进行统计处理。

    names=['userid','actionType','actionTime']
    
    newCust=pd.DataFrame(columns=["userid",'totalstep','step1N','step2N','step3N','step4N',
                            'step5N','step6N','step7N','step8N','step9N','step1P','step2P','step3P','step4P',
                            'step5P','step6P','step7P','step8P','step9P','viewProductN','last1time','last2time','last3time','last4time',
                            'last5time','last6time','last7time','last8time','last9time','buy/viewProductN','buy/n5','(2-4)/(1)',
                            'tail1','tail2','tail3','tail4','head1',
                            'maxtime','mintime','averagetime','vartime','mediantime','tailtime1','tailtime2','tailtime3','tailtime4','tail3ave','tail3var',
                            'near1','near2','near3','near4','near5','near6','near7','nsar8','near9',
                            't1a','t1v','t1mini','t1max',
                            't2a','t2v','t2mini','t2max',
                            't3a','t3v','t3mini','t3max',
                            't4a','t4v','t4mini','t4max',
                            't5a','t5v','t5mini','t5max',
                            't6a','t6v','t6mini','t6max',
                            't7a','t7v','t7mini','t7max',
                            't8a','t8v','t8mini','t8max',
                            't9a','t9v','t9mini','t9max','t9av'])
    idlist=[]


    for i in range(0,len(cm_data_raw)):
        record=cm_data_raw.iloc[i]
        uid=record['userid']

        if uid not in idlist:
            idlist.append(uid)
            udata=cm_data_raw[cm_data_raw['userid']==uid]
            udata=sort(udata,["actionTime","actionType"],ascending=False)
            
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
            
            
            #距离每个行为最近的行为和时间
            near1=0
            near2=0
            near3=0
            near4=0
            near5=0
            near6=0
            near7=0
            near8=0
            near9=0
            

            #距离各个节点最近时间间隔
            ne1=[]
            ne2=[]
            ne3=[]
            ne4=[]
            ne5=[]
            ne6=[]
            ne7=[]
            ne8=[]
            ne9=[]
            

            
            
            
            
            
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
                        near1=j
                        if j>0:
                            for i in range(1,j):
                                ne1.append(udata.iloc[i]['actionTime']-udata.iloc[i-1]['actionTime'])
                        
                if oudata['actionType']==2:
                    n2=n2+1
                    if f2==0:
                        f2=2
                        t2=oudata['actionTime']
                        near2=j
                        
                        if j>0:
                            for i in range(1,j):
                                ne2.append(udata.iloc[i]['actionTime']-udata.iloc[i-1]['actionTime'])
                        
                        
                if oudata['actionType']==3:
                    n3=n3+1
                    if f3==0:
                        f3=2
                        t3=oudata['actionTime']
                        near3=j
                        
                        if j>0:
                            for i in range(1,j):
                                ne3.append(udata.iloc[i]['actionTime']-udata.iloc[i-1]['actionTime'])
                        
                if oudata['actionType']==4:
                    n4=n4+1
                    if f4==0:
                        f4=2
                        t4=oudata['actionTime']
                        near4=j
                        
                        if j>0:
                            for i in range(1,j):
                                ne4.append(udata.iloc[i]['actionTime']-udata.iloc[i-1]['actionTime'])
                        
                        
                        
                        
                        
                if oudata['actionType']==5:
                    n5=n5+1
                    if f5==0:
                        f5=2
                        t5=oudata['actionTime']
                        near5=j
                        
                        if j>0:
                            for i in range(1,j):
                                ne5.append(udata.iloc[i]['actionTime']-udata.iloc[i-1]['actionTime'])
                        
                
                
                if oudata['actionType']==9:
                    n9=n9+1
                    if f9==0:
                        f9=2
                        t9=oudata['actionTime']
                        near9=j
                        
                        if j>0:
                            for i in range(1,j):
                                ne9.append(udata.iloc[i]['actionTime']-udata.iloc[i-1]['actionTime'])
                        
                if oudata['actionType']==8:
                    n8=n8+1
                    if f8==0:
                        f8=2
                        t8=oudata['actionTime']
                        near8=j
                        
                        if j>0:
                            for i in range(1,j):
                                ne8.append(udata.iloc[i]['actionTime']-udata.iloc[i-1]['actionTime'])
                        
                if oudata['actionType']==7:
                    n7=n7+1
                    if f7==0:
                        f7=2
                        t7=oudata['actionTime']
                        near7=j
                        
                        if j>0:
                            for i in range(1,j):
                                ne7.append(udata.iloc[i]['actionTime']-udata.iloc[i-1]['actionTime'])
                        
                if oudata['actionType']==6:
                    n6=n6+1
                    if f6==0:
                        f6=2
                        t6=oudata['actionTime']
                        near6=j
                        if j>0:
                            for i in range(1,j):
                                ne6.append(udata.iloc[i]['actionTime']-udata.iloc[i-1]['actionTime'])
                        
                        
                if oudata['actionType']==5:
                    n5=n5+1
                    if f5==0:
                        f5=2
                        t5=oudata['actionTime']
                        near5=j
                        if j>0:
                            for i in range(1,j):
                                ne7.append(udata.iloc[i]['actionTime']-udata.iloc[i-1]['actionTime'])
                        
                        
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
            
            t8a=0
            t8v=0
            t8min=0
            t8max=0
            t7a=0
            t7v=0
            t7min=0
            t7max=0
            t6a=0
            t6v=0
            t6min=0
            t6max=0
            t5a=0
            t5v=0
            t5min=0
            t5max=0
            t4a=0
            t4v=0
            t4min=0
            t4max=0
            t3a=0
            t3v=0
            t3min=0
            t3max=0
            t2a=0
            t2v=0
            t2min=0
            t2max=0
            t1a=0
            t1v=0
            t1min=0
            t1max=0
            t9a=0
            t9v=0
            t9min=0
            t9max=0
            t9av=0 
            if len(ne9)!=0:
                t9a=np.average(ne9)
                t9v=np.var(ne9)
                t9min=np.min(ne9)
                t9max=np.max(ne9)
                t9av=t9a*t9v
                
            if len(ne8)!=0:
                t8a=np.average(ne8)
                t8v=np.var(ne8)
                t8min=np.min(ne8)
                t8max=np.max(ne8)
                
            if len(ne7)!=0:
                t7a=np.average(ne7)
                t7v=np.var(ne7)
                t7min=np.min(ne7)
                t7max=np.max(ne7)
                
            if len(ne6)!=0:
                t6a=np.average(ne6)
                t6v=np.var(ne6)
                t6min=np.min(ne6)
                t6max=np.max(ne6)
            if len(ne5)!=0:
                t5a=np.average(ne5)
                t5v=np.var(ne5)
                t5min=np.min(ne5)
                t5max=np.max(ne5)
            if len(ne4)!=0:
                t4a=np.average(ne4)
                t4v=np.var(ne4)
                t4min=np.min(ne4)
                t4max=np.max(ne4)

            if len(ne3)!=0:
                t3a=np.average(ne3)
                t3v=np.var(ne3)
                t3min=np.min(ne3)
                t3max=np.max(ne3)
            
            if len(ne2)!=0:

                t2a=np.average(ne2)
                t2v=np.var(ne2)
                t2min=np.min(ne2)
                t2max=np.max(ne2)
            if len(ne1)!=0:
                t1a=np.average(ne1)
                t1v=np.var(ne1)
                t1min=np.min(ne1)
                t1max=np.max(ne1)
    

                
                    
                    
                    
            finalud={"userid":uid,'totalStep':totalStep,'step1N':n1,'step2N':n2,'step3N':n3,'step4N':n4,
                     'step5N':n5,'step6N':n6,'step7N':n7,'step8N':n8,
                     'step9N':n9,'step1P':p1,'step2P':p2,'step3P':p3,'step4P':p4,
                     'step5P':p5,'step6P':p6,'step7P':p7,'step8P':p8,'step9P':p9,
                     'viewProductN':n2+n3+n4,'last1time':t1,'last2time':t2,'last3time':t3,
                     'last4time':t4,'last5time':t5,'last6time':t6,'last7time':t7,'last8time':t8,
                     'last9time':t9,'buy/viewProductN':buy_viewProductN,'buy/n5':buy_5,'(2-4)/(1)':p24_1,
                     'tail1':tail1,'tail2':tail2,'tail3':tail3,'tail4':tail4,'head1':head1,
                     'maxtime':maxtime,'mintime':mintime,'averagetime':averagetime,'vartime':vartime,'mediantime':mediantime,
                     'tailtime1':tailtime1,'tailtime2':tailtime2,'tailtime3':tailtime3,'tailtime4':tailtime4,'tail3ave':tail3ave,'tail3var':tail3var,
                     't9a':t9a,'t9v':t9v,'t9mini':t9min,'t9max':t9max,'t9av':t9av,
                     't8a':t8a,'t8v':t8v,'t8mini':t8min,'t8max':t8max,
                     't7a':t7a,'t7v':t7v,'t7mini':t7min,'t7max':t7max,
                     't6a':t6a,'t6v':t6v,'t6mini':t6min,'t6max':t6max,
                     't5a':t5a,'t5v':t5v,'t5mini':t5min,'t5max':t5max,
                     't4a':t4a,'t4v':t4v,'t4mini':t4min,'t4max':t4max,
                     't3a':t3a,'t3v':t3v,'t3mini':t3min,'t3max':t3max,
                     't2a':t2a,'t2v':t2v,'t2mini':t2min,'t2max':t2max,
                     't1a':t1a,'t1v':t1v,'t1mini':t1min,'t1max':t1max}
            
            newCust=newCust.append(finalud,ignore_index=True)
        
    newCust.to_csv(outputpath)
                
                        
                
    return
                
                


    


# In[60]:

action_statistics(r'train_set\action_train.csv',r'action_stantistics.csv')


# In[61]:

action_statistics(r'test\action_test.csv',r'action_stantistics_test.csv')


# In[ ]:



