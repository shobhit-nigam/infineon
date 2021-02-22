#!/usr/bin/env python
# coding: utf-8

# In[4]:


lista = [3, 6, 8, 4]
listb = [4, 7, 9, 5]


# In[5]:


listc = []

for i in range(len(lista)):
    listc.append(lista[i] + listb[i])


# In[6]:


listc


# In[10]:


listd = [lista[i]+listb[i] for i in range(len(lista))]


# In[11]:


listd


# In[12]:


liste = [x for x in "world"]


# In[13]:


liste


# In[14]:


listb = [4, 7, 9, 5]


# In[15]:


listf = [x for x in listb if x%2==0]


# In[16]:


listf


# In[18]:


[x for x in range(10) if x%3 == 0]


# In[19]:


lista = [3, 6, 8, 4]
listb = [4, 7, 9, 5]


# In[20]:


def funca(la):
    res = []
    for i in la:
        res.append(i**3)
    return res


# In[21]:


def funcb(la):
    return [i**3 for i in la]


# In[22]:


get_ipython().run_line_magic('timeit', 'funca(range(1, 15))')


# In[23]:


get_ipython().run_line_magic('timeit', 'funcb(range(1, 15))')


# In[ ]:




