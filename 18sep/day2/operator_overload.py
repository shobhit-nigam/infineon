#!/usr/bin/env python
# coding: utf-8

# In[1]:


4 + 3


# In[2]:


"hi" + "hello"


# In[3]:


varx = 'infi'
vary = 'neon'


# In[4]:


varx + vary


# In[5]:


varx*3 + vary


# In[6]:


varz = 7/2


# In[7]:


varz


# In[8]:


varz = 7//2


# In[9]:


varz


# In[10]:


varz = 7%2


# In[11]:


varz


# In[12]:


varz = 2**3


# In[13]:


varz


# In[15]:


12/6/2


# In[16]:


class time:
    def __init__(self, hours=0, minutes=0):
        self.hours = hours
        self.minutes = minutes


# In[17]:


obja = time(2, 40)
objb = time(2, 40)


# In[18]:


objc = time()
objc = obja + objb

#obja + objb = obja.__add__(objb)
# = time.__add__(obja, objb)


# In[19]:


class time:
    def __init__(self, hours=0, minutes=0):
        self.hours = hours
        self.minutes = minutes
    def __add__(self, selfb):
        selfc = time()
        tempa = self.hours * 60 + self.minutes
        tempb = selfb.hours * 60 + selfb.minutes 
        tempc = tempa + tempb
        selfc.hours = tempc//60
        selfc.minutes = tempc%60
        return selfc


# In[20]:


obja = time(2, 40)
objb = time(2, 40)
objc = time()


# In[21]:


objc = obja + objb


# In[22]:


print(objc.hours, "hours & ", objc.minutes , "minutes")


# In[23]:


objd = time(2, 33)


# In[24]:


objc = obja + objb + objd


# In[25]:


print(objc)


# In[26]:


objc.hours


# In[27]:


objc.minutes


# In[ ]:




