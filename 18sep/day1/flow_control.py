#!/usr/bin/env python
# coding: utf-8

# In[1]:


varx = vary = varz = 23


# In[3]:


if varx == 20:
    #belongs to if
    print("varx is 20")
elif varx < 20:
    print("varx is greater than 20")
else:
    print("varx is ", varx)
print('outside if else')


# In[4]:


dc = ['batman', 'superman', 'wonderwoman']


# In[5]:


for characters in dc:
    print(characters)


# In[6]:


characters


# In[7]:


avengers = ['antman', 'captain', 'ironman', 'hulk', 'blackwidow']


# In[8]:


for val in avengers:
    if len(val) > 6:
        print(val, len(val))


# In[9]:


for val in avengers:
    print(val, len(val))


# In[10]:


for val in avengers[2:6]:
    print(val, len(val))


# In[11]:


marvel = ['magneto', 'wolverine', 'magneto']


# In[12]:


marvel.append(avengers)


# In[13]:


marvel


# In[14]:


for val in marvel:
    print(val, len(val))


# In[15]:


val


# In[16]:


type(val)


# In[17]:


for i in range(3):
    print(i)


# In[18]:


for i in range(2,9):
    print(i)


# In[19]:


for i in range(2,9, 3):
    print(i)


# In[20]:


for i in range(2, -1):
    print(i)


# In[21]:


i


# In[22]:


avengers[1:5:2]


# In[23]:


avengers


# In[24]:


for i in range(0,3):
    for j in range(0,3):
        if(i==j):
            print('tea break')
            break;
        else:
            print('no tea break')


# In[25]:


import sys
import os


# In[26]:


os.path


# In[27]:





# In[ ]:




