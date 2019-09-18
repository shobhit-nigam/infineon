#!/usr/bin/env python
# coding: utf-8

# In[1]:


lista = [6, 8, 9, 10]


# In[2]:


lista[1]


# In[3]:


lista[-2]


# In[4]:


lista[3] = 555


# In[5]:


print(lista)


# In[6]:


dc = ['batman', 'superman', 'wonderwoman']


# In[7]:


type(dc)


# In[8]:


dc.insert(2, 'flash')


# In[9]:


print(dc)


# In[10]:


help(dc.insert)


# In[11]:


avengers = ['antman', 'captain', 'ironman', 'hulk', 'blackwidow']


# In[12]:


marvel = ['magneto', 'wolverine', 'magneto']


# In[13]:


compound = [34, 'deadpool', 44.56]


# In[14]:


marvel.append('deadpool')


# In[15]:


marvel


# In[16]:


marvel.append(avengers)


# In[17]:


print(marvel)


# In[18]:


type(marvel[2])


# In[19]:


type(marvel[4])


# In[20]:


marvel[4][2][2]


# In[22]:


marvel[2] = 66.78


# In[23]:


marvel


# In[24]:


marvel.remove(avengers)


# In[25]:


marvel


# In[26]:


marvel.extend(avengers)


# In[27]:


marvel


# In[28]:


print(marvel)


# In[30]:


newheroes = marvel + dc


# In[31]:


print(newheroes)


# In[32]:


len(newheroes)


# In[33]:


marvel


# In[34]:


avengers


# In[35]:


avengers[2:4]


# In[36]:


marvel[4] = None


# In[37]:


marvel


# In[38]:


del marvel[4]


# In[ ]:




