#!/usr/bin/env python
# coding: utf-8

# In[15]:


from pytrends.request import TrendReq
import pandas as pd
import time
startTime = time.time()
pytrend = TrendReq(hl='en-IN', tz=360)


# In[16]:


colnames = ["list"]
df = pd.read_csv("list.csv", names=colnames)
df2 = df["list"].values.tolist()
df2.remove("list")

dataset = []


# In[17]:


for x in range(0,len(df2)):
    words = [df2[x]]
    pytrend.build_payload(kw_list=words,cat=0,timeframe='2020-01-01 2020-02-01',geo='IN')
    data = pytrend.interest_over_time()
    if not data.empty:
        data = data.drop(labels=['isPartial'],axis='columns')
        dataset.append(data)


# In[18]:


result = pd.concat(dataset, axis=1)
result.to_csv('trends.csv')


# In[19]:


import csv

with open('trends.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

print(data)


# In[ ]:




