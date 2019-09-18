#!/usr/bin/env python
# coding: utf-8

# In[1]:


def funca():
    #your code
    print('function does nothing')


# In[2]:


funca()


# In[3]:


varx = funca()


# In[4]:


print(varx)


# In[5]:


def funcb():
    #your code
    print('function does nothing')
    return 23


# In[6]:


vary = funcb()


# In[7]:


print(vary)


# In[8]:


def funcc():
    #your code
    print('function does nothing')
    return 23, 56, [7, 8, 9], 'hello'


# In[9]:


vara, varb, varc, vard = funcc()


# In[10]:


varc


# In[11]:


def funcc():
    #your code
    print('function does nothing')
    return 23, 56, [7, 8, 9], 'hello'vara, varb, varc = funcc()


# In[12]:


def funcc():
    #your code
    print('function does nothing')
    return 23, 56, [7, 8, 9], 'hello'


vara = funcc()


# In[13]:


type(vara)


# In[14]:


len(funcc())


# In[15]:


varx = 12

def funcc():
    vary = 13
    #your code
    print('varx = ', varx)
    print('vary = ', vary)


# In[16]:


funcc()


# In[17]:


varx = 12

def funcd():
    vary = 13
    varx = vary + 5
    #your code
    print('varx = ', varx)
    print('vary = ', vary)


# In[18]:


funcd()


# In[19]:


varx = 12

def funcd():
    vary = 13
    varx = 23
    #your code
    print('varx = ', varx)
    print('vary = ', vary)


# In[20]:


funcd()


# In[21]:


varx


# In[23]:


varx = 12

def funce():
    vary = 13
    global varx 
    varx = 23
    #your code
    print('varx = ', varx)
    print('vary = ', vary)


# In[24]:


funce()


# In[25]:


varx


# In[26]:


def funcg():
    print('funcg ')
    #some code
    def funch():
        print('funch')
        #some code
        return None
    print('still in funcg')
    return None


# In[27]:


funcg()


# In[28]:


funch()


# In[29]:


def funcg():
    print('funcg ')
    #some code
    def funch():
        print('funch')
        #some code
        return None
    funch()
    print('still in funcg')
    return None


# In[30]:


funcg()


# In[33]:


def funci(x, y, z):
    print('funci ')
    #some code
    print('x=', x)
    print('y=', y)
    print('z=', z)
    return None 


# In[34]:


funci(67, 89, 100)


# In[36]:


def funci(x=3, y=4, z=5):
    print('funci ')
    #some code
    print('x=', x)
    print('y=', y)
    print('z=', z)
    return None 


# In[37]:


funci(67, 89)


# In[38]:


def funci(x, y=4, z=5):
    print('funci ')
    #some code
    print('x=', x)
    print('y=', y)
    print('z=', z)
    return None 


# In[39]:


funci(67, 89)


# In[41]:


def funcj(x=2, y=4, z=6):
    print('funci ')
    #some code
    print('x=', x)
    print('y=', y)
    print('z=', z)
    return None 


# In[42]:


funcj(y=77)


# In[43]:


funcj(44, y=77)


# In[44]:


funcj(z = 44, y=77)


# In[45]:


type(funca)


# In[ ]:




