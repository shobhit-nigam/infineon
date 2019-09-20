#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re


# In[4]:


pattern = '^a..a$'

stra = input("enter string ")
result = re.match(pattern, stra)

if result:
    print("its a match")
else:
    print("not a match")


# In[6]:


pattern = 'h..l'

stra = input("enter string ")
result = re.findall(pattern, stra)

if result:
    print("its a match")
    print(result)
    print(len(result))
else:
    print("not a match")


# In[8]:


objb = open('test.txt', 'r')
stra = objb.read()
objb.close()
pat = '\d+'
res = re.findall(pat, stra)
print(res)


# In[9]:


objb = open('test.txt', 'r')
stra = objb.read()
objb.close()
pat = '\d+'
res = re.split(pat, stra)
print(res)


# In[10]:


import re

stra = 'abc 12\de 23 \n f55 8'
pat = '\s+'
replace = '_'

strb = re.sub(pat, replace, stra)
print(strb)


# In[11]:


import re

stra = 'abc 12\de 23 \n f55 8'
pat = '\s+'
replace = '_'

strb = re.subn(pat, replace, stra)
print(strb)


# In[12]:


strc = '\new delhi'


# In[13]:


strc


# In[14]:


print(strc)


# In[15]:


help(re.subn)


# In[16]:


stra = 'abc 12\de 23 \n f55 8'


# In[17]:


stra


# In[ ]:




