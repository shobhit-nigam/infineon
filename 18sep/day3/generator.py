#!/usr/bin/env python
# coding: utf-8

# In[1]:


def funca(varx):
    return varx*varx


# In[2]:


vary = funca(2)


# In[3]:


vary


# In[4]:


def funcb():
    yield 1
    yield 4
    yield 9


# In[5]:


varx = funcb()


# In[6]:


varx


# In[8]:


varx.__next__()


# In[9]:


varx.__next__()


# In[10]:


varx.__next__()


# In[11]:


varx.__next__()


# In[12]:


def funcc():
    yield 1
    yield 4
    yield 9


# In[14]:


for val in funcc():
    print(val)


# In[ ]:




