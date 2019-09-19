#!/usr/bin/env python
# coding: utf-8

# In[2]:


class linux:
    varx = 44
    def __init__(self):
        print("init of linux")
    def cmd(self):
        print("command line")


# In[4]:


obja = linux()


# In[5]:


help(linux)


# In[6]:


linux.__init__.__doc__


# In[7]:


class linux:
    varx = 44
    def __init__(self):
        print("init of linux")
    def cmd(self):
        print("command line")
    def change(self):
        self.vary = 66
        print("changing the object")


# In[8]:


obja = linux()
objb = linux()


# In[9]:


obja.change()


# In[10]:


obja.vary


# In[11]:


objb.vary


# In[12]:


linux.vary


# In[13]:


obja.varz = 44


# In[14]:


objc = obja


# In[15]:


objc.varz


# In[17]:


pass


# In[19]:


objd = obja


# In[ ]:




