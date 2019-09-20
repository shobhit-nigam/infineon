#!/usr/bin/env python
# coding: utf-8

# In[1]:


class linux:
    def cmd(self):
        print("command line")
        self.funca()
        self.funcb()
        self.funcc()
    def funca(self):
        print("in a of linux")
    def funcb(self):
        print("in b of linux")
    def funcc(self):
        print("in c of linux")


# In[2]:


obja = linux()


# In[3]:


obja.cmd()


# In[5]:


class linux:
    def cmd(self):
        print("command line")
        self._funca()
        self.__funcb()
        self.__funcc__()
    def _funca(self):
        print("in a of linux")
    def __funcb(self):
        print("in b of linux")
    def __funcc__(self):
        print("in c of linux")


# In[6]:


obja = linux()


# In[7]:


obja._funca()


# In[8]:


obja.__funcb()


# In[9]:


obja.__funcc__()


# In[10]:


obja.cmd()


# In[ ]:




