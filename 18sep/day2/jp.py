#!/usr/bin/env python
# coding: utf-8

# In[1]:


"jp module for understanding modules"


# In[3]:


def green():
    "go green"
    print("green of jp")
    #some code


# In[4]:


import astha


# In[5]:


help(astha)


# In[6]:


print(__doc__)


# In[7]:


print(green.__doc__)


# In[8]:


help(green)


# In[9]:


help(astha.orange)


# In[11]:


print(astha.orange.__doc__)


# In[12]:


import sys


# In[13]:


sys.path


# In[14]:


import astha


# In[15]:


from astha import pink


# In[16]:


import importlib


# In[17]:


importlib.reload(astha)


# In[18]:


astha.pink()


# In[19]:





# In[20]:


varx = 45


# In[ ]:




