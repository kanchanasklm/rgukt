#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
dg=pd.read_csv('Ecommerce Purchases.csv')
dg.head()


# In[6]:


dg.info()


# In[7]:


dg['Purchase Price'].mean()


# In[8]:


dg['Purchase Price'].max()


# In[9]:


dg['Purchase Price'].min()


# In[10]:


dg[dg['Language']=='en'].count()


# In[11]:


dg[dg['Job']=='Lawyer'].info()


# In[12]:


dg['AM or PM'].value_counts()


# In[13]:


dg['Job'].value_counts().head(5)


# In[14]:


dg[dg['Lot']=='90 WT']['Purchase Price']


# In[15]:


dg[dg['Credit Card']==4926535242672853]['Email']


# In[18]:


dg[(dg['CC Provider']=='American Express') & (dg['Purchase Price']>95)].count()


# In[19]:


sum(dg['CC Exp Date'].apply(lambda x: x[3:])=='25')


# In[20]:


dg['Email'].apply(lambda x:x.split('@')[1]).value_counts().head(5)


# In[ ]:




