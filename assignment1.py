#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
df=pd.read_csv('Salaries.csv')
df.head()


# In[3]:


df.info()


# In[4]:


df['BasePay'].mean()


# In[5]:


df['OvertimePay'].max()


# In[6]:


df[df['EmployeeName']=='JOSEPH DRISCOL']['JobTitle']


# In[7]:


df[df['EmployeeName']=='JOSEPH DRISCOL']['TotalPayBenefits']


# In[9]:


df[df['TotalPayBenefits']==df['TotalPayBenefits'].max()]


# In[10]:


df[df['TotalPayBenefits']==df['TotalPayBenefits'].min()]


# In[11]:


df.groupby('Year').mean()['BasePay']


# In[12]:


df['JobTitle'].nunique()


# In[13]:


jobs=df.groupby('JobTitle').count()
top_five=jobs.sort_values(by='Id',ascending=False)[:5]
top_five['Id']


# In[14]:


year=df[df['Year']==2013]
group=year.groupby('JobTitle').count()
count=group[group['Id']==1]
count.count()['Id']


# In[21]:


def go_chief(job_title):
    if 'chief' in job_title.lower().split():
        return True
    else:
        return False
df=pd.read_csv('Salaries.csv')
sum(df['JobTitle'].apply(lambda x:go_chief(x)))


# In[22]:


df['title_len']=df['JobTitle'].apply(len)
df[['title_len','TotalPayBenefits']].corr()


# In[ ]:




