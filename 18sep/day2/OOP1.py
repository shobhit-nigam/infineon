#!/usr/bin/env python
# coding: utf-8

# In[14]:


#bjarne strotsup
class unix:
    "unix if not free"
    varx = 35
    vary = 44.66
    def cmd():
        print("command line")


# In[2]:


unix.varx


# In[3]:


type(unix)


# In[4]:


unix.cmd()


# In[5]:


hi = print


# In[6]:


hi("hello")


# In[15]:


obja = unix()


# In[16]:


objb = unix


# In[17]:


obja.varx = 55


# In[18]:


objb.varx


# In[19]:


objb.varx = 66


# In[20]:


unix.varx


# In[21]:


#bjarne strotsup
class unix:
    "unix if not free"
    varx = 35
    vary = 44.66
    def cmd():
        print("command line")


# In[22]:


obja = unix()


# In[23]:


unix.cmd()


# In[24]:


obja.cmd()
#unix.cmd(obja)


# In[25]:


#bjarne strotsup
class unix:
    "unix if not free"
    varx = 35
    vary = 44.66
    def cmd(ttt):
        print("command line")


# In[26]:


obja = unix()


# In[27]:


obja.cmd()
#unix.cmd(obja)


# In[29]:


#bjarne strotsup
class unix:
    "unix if not free"
    varx = 35
    vary = 44.66
    def cmd(self):
        print("command line")
        print(self.varx)
        self.varx = 77


# In[30]:


obja = unix()


# In[31]:


obja.cmd()


# In[32]:


obja.varx


# In[33]:


objb = unix()


# In[34]:


objb.varx


# In[35]:


objb.cmd()


# In[36]:


objb.varx


# In[37]:


unix.varx = 88


# In[38]:


objc = unix()


# In[39]:


objc.varx


# In[40]:


unix.cmd()


# In[41]:


unix.cmd(obja)


# In[42]:


#bjarne strotsup
class unix:
    "unix if not free"
    varx = 35
    vary = 44.66
    def cmd(self):
        print("command line")


# In[43]:


unix.cmd("hello")


# In[44]:


#bjarne strotsup
class unix:
    "unix if not free"
    varx = 35
    vary = 44.66
    def cmd(self):
        print("command line")
        self.varx = 44


# In[45]:


unix.cmd(unix)


# In[46]:


#bjarne strotsup
class unix:
    "unix if not free"
    varx = 35
    vary = 44.66
    def cmd(self, la, lb):
        print("command line")
        self.varx = la + lb


# In[47]:


obja = unix()


# In[48]:


obja.cmd(5, 6)
#unix.cmd(obja, 5, 6)


# In[49]:


obja.varx


# In[50]:


help(unix)


# In[51]:


print(unix.__doc__)


# In[ ]:




