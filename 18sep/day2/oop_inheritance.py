#!/usr/bin/env python
# coding: utf-8

# In[6]:


class linux:
    varx = 44
    def __init__(self, ia=0):
        print("init of linux")
        self.varx = ia
    def cmd(self):
        print("command line")


# In[7]:


class gui:
    def graphics(self):
        print("visually appealing")


# In[8]:


class ubuntu(linux):
    def specail(self):
        print("some specail functionality")


# In[9]:


obja = ubuntu()


# In[10]:


obja.specail()


# In[11]:


obja.cmd()


# In[12]:


class linux:
    varx = 44
    def __init__(self):
        print("init of linux")
        self.varx = ia
    def cmd(self):
        print("command line")
    def funca(self):
        print("in a of linux")
    def funcb(self):
        print("in b of linux")


# In[13]:


class ubuntu(linux):
    def __init__(self):
        print("init of ubuntu")
    def specail(self):
        print("some specail functionality")
    def funca(self):
        print("a of ubuntu")


# In[14]:


obju = ubuntu()


# In[15]:


obju.funca()


# In[18]:


class linux:
    def __init__(self):
        print("init of linux")
    def cmd(self):
        print("command line")
    def funca(self):
        print("in a of linux")
    def funcb(self):
        print("in b of linux")

class gui:
    def graphics(self):
        print("visually appealing")

class android(linux, gui):
    def mobileapps(self):
        print("mobile applications")


# In[19]:


obja = android()


# In[20]:


obja.graphics()


# In[21]:


class linux:
    def __init__(self):
        print("init of linux")
    def cmd(self):
        print("command line")
    def funca(self):
        print("in a of linux")
    def funcb(self):
        print("in b of linux")

class gui:
    def graphics(self):
        print("visually appealing")
    def funca():
        print("in a of gui")

class android(linux, gui):
    def mobileapps(self):
        print("mobile applications")


# In[22]:


obja = android()


# In[23]:


obja.funca()


# In[ ]:




