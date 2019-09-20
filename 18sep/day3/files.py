#!/usr/bin/env python
# coding: utf-8

# In[1]:


obja = open("energy.txt", 'r')


# In[2]:


obja = open("energy.txt", 'r')


# In[3]:


stra = obja.read(6)


# In[4]:


type(stra)


# In[5]:


len(stra)


# In[6]:


print(stra)


# In[7]:


stra = obja.readline()


# In[8]:


print(stra)


# In[9]:


obja.tell()


# In[10]:


obja.seek(0)


# In[11]:


obja.tell()


# In[12]:


strc = obja.read()


# In[13]:


lista = strc.split()


# In[14]:


lista


# In[15]:


obja.close()


# In[16]:


objb = open("lethargy.txt", 'w')


# In[17]:


help(open)


# In[18]:


objb.close()


# In[19]:


objb = open("lethargy.txt", 'w')


# In[20]:


objb.write("some data written")


# In[21]:


objb.close()


# In[22]:


import os


# In[23]:


os.remove('lethargy copy.txt')


# In[ ]:




