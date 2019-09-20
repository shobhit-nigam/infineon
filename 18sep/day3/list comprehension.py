#!/usr/bin/env python
# coding: utf-8

# In[1]:


lista = []

for var in 'rose':
    lista.append(var)


# In[2]:


lista


# In[3]:


listb = [var for var in 'rose']


# In[4]:


listb


# In[5]:


strb = "ashish verma from pune"


# In[6]:


listc = strb.split()


# In[7]:


listc


# In[8]:


number = [x for x in range(20) if x%2 == 0]


# In[9]:


number


# In[10]:


numbers = [1, 2, 3, 4]
squares = []

for n in numbers:
    squares.append(n**2)


# In[11]:


def square_for(arr):
    result = []
    for i in arr:
        result.append(i**2)
    return result

def square_lc(arr):
    return [i**2 for i in arr]


# In[12]:


arr = [1, 3, 4, 6]


# In[14]:


square_lc(arr)


# In[15]:


get_ipython().run_line_magic('timeit', 'square_for(range(1, 11))')


# In[16]:


get_ipython().run_line_magic('timeit', 'square_lc(range(1, 11))')


# In[ ]:




