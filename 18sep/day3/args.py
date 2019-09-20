#!/usr/bin/env python
# coding: utf-8

# In[1]:


def funcp(varx, vary):
    print(varx)
    print(vary)


# In[2]:


funcp(6, 7)


# In[3]:


def funcp(varx, vary, *lista):
    print(varx)
    print(vary)
    print("variable arguments:")
    for val in lista:
        print(val)


# In[4]:


funcp(5, 8)


# In[5]:


funcp(5, 8, 12, 13, 'hi', [9, 7], 'string')


# In[6]:


def funcp(*args, **kwargs):
    print("variable arguments:")
    for val in args:
        print(val)
    print("pairs:")
    for key, val in kwargs.items():
        print("key=", key, "\tval=", val)


# In[7]:


funcp(12, "hi", 34, company='infineon', location='trinity', pincode=560001)


# In[8]:


print("hi")
print("hello")


# In[11]:


def funcp(*args, **kwargs):
    print("variable arguments:")
    for val in args:
        print(val, end=', ')
    print("\npairs:")
    for key, val in kwargs.items():
        print("key=", key, "\tval=", val)


# In[12]:


funcp(12, "hi", 34, company='infineon', location='trinity', pincode=560001)


# In[13]:


stra = "\new delhi"
print(stra)


# In[14]:


stra = "\\new delhi"
print(stra)


# In[15]:


print("\new delhi")


# In[16]:


print(r"\new delhi")


# In[ ]:


print("hi" + varx)

