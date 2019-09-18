#!/usr/bin/env python
# coding: utf-8

# In[1]:


lista = [7, 8, 9, 13]


# In[2]:


listb = (7, 8, 9, 13)


# In[3]:


type(listb)


# In[4]:


lista[2] = 5577


# In[5]:


pass


# In[6]:


listb[2] = 5577


# In[7]:


tupb = (6, 7, "hi", [83, 93, 63])


# In[8]:


tupb[3] = "hello"


# In[9]:


tupb[3][1] = "hello"


# In[10]:


tupb


# In[11]:


#dict


# In[12]:


ditcb = {'red':'ferrari' , 'green':'peace', 'blue':['kohli', 'dhoni', 'sachin'], 'white':'curd'}


# In[14]:


ditcb['red']


# In[15]:


ditcb['green'] = 'leaves'


# In[16]:


ditcb


# In[17]:


ditcb['orange'] = 'orange'


# In[18]:


ditcb


# In[19]:


varx = 33
vary = 44


# In[21]:


ditcc = {varx:'three', vary:'four', 'colours':ditcb}


# In[22]:


len(ditcc)


# In[23]:


ditcc['colours']['blue'][2][2]


# In[24]:


ditcc[varx]


# In[26]:


ditcc = {varx:'three', vary:'four', 'colours':ditcb, listb:'some value'}


# In[27]:


type(listb)


# In[28]:


ditcc[listb]


# In[29]:


for k, v in ditcb.items():
    print(k, '\t', v)


# In[30]:


listc = list(ditcb.keys())


# In[31]:


listc


# In[32]:


seta = {'arsenal', 'liverpool', 'bayern munich', 'juventus', 'chennaiFC', 'juventus'}


# In[33]:


seta


# In[34]:


varx = ()


# In[35]:


type(varx)


# In[36]:


varx = [4]


# In[37]:


type(varx)


# In[38]:


varx = (4)


# In[39]:


type(varx)


# In[40]:


varx = (4,)


# In[41]:


type(varx)


# In[42]:


vary = 4,


# In[43]:


type(vary)


# In[44]:


vara, varb = 7,8


# In[45]:


vara = 7,8


# In[46]:


type(vara)


# In[47]:


print(vara)


# In[49]:


id(vara[1]) == id(varb)


# In[50]:


varj,vark,varl = 5


# In[51]:


tupb = varj,vark,varl


# In[ ]:




