#!/usr/bin/env python
# coding: utf-8

# In[2]:


varq = int(input())


# In[3]:


type(varq)


# In[5]:


varq = int(input())

if varq < 60:
    print("less than 60")
    print("")
else:
    print("more than or equal to 60")


# In[7]:


varq = int(input())

if varq < 60:
    print("less than 60")
    print("")
else:
    print("more than or equal to 60")


# In[8]:


if varq < 60:
    print("less than 60")
    print("")
elif varq == 60:
    print("equal to 60")
else:
    print("more tha 60")


# In[10]:


if varq < 60:
    print("less than 60")
    print("")
elif varq == 60:
    print("equal to 60")
else:
    pass


# In[11]:


varq = int(input())
varr = int(input())

if varq < 60 and varr > 50:
    print("less than 60")
    print("")
else:
    print("more than or equal to 60")


# In[ ]:


varq = int(input())
varr = int(input())

if varq > 30 and varq < 60 :
    print("less than 60")
    print("")
else:
    print("more than or equal to 60")


# In[12]:


varq > 30 and varq < 60


# In[13]:


30 < varq < 60

# chain


# In[14]:


varq = int(input())

while(varq < 60):
    print("varq =", varq)
    varq = varq+1


# In[15]:


print(varq)


# In[16]:


for x in range(6):
    print("x is", x)


# In[17]:


for x in range(2, 8):
    print("x is", x)


# In[18]:


for x in range(2, 19, 3):
    print("x is", x)


# In[19]:


for x in range(13, 9):
    print("x is", x)


# In[20]:


for x in range(13, 9, -1):
    print("x is", x)


# In[21]:


lista = ['qq', 'tt', 'dd', 'yy', 'ss', 'qq', 'ff', 'dd']


# In[22]:


for i in range(len(lista)):
    print("lista[i] =", lista[i])


# In[23]:


for val in lista:
    print("lista[i] =", val)


# In[24]:


for val in "hello":
    print("val", val)


# In[25]:


listb = ['aa', 'rr', 'ss', 'ww', 'ii', 'xx', 'ff']


# In[26]:


lista = ['qq', 'tt', 'dd', 'yy', 'ss', 'qq', 'ff', 'dd']


# In[27]:


for a in lista:
    if a in listb:
        print(a)


# In[28]:


lista.index('ff')


# In[29]:


listc = []

for a in lista:
    if a in listb:
        listc.append(a)
        print("found common")


# In[30]:


listc = []

for a in lista:
    if a in listb:
        print("found common")
        break


# In[31]:


listd = ['aa', 'rr', 'cc', 'ww', 'ii', 'xx', 'mm']


# In[32]:


for a in lista:
    if a in listd:
        print("found common")
        break


# In[33]:


for a in lista:
    if a in listd:
        print("found common")
        break
    else:
        print("no common")


# In[34]:


for a in lista:
    if a in listd:
        print("found common")
        break
else:
    print("no common")


# In[35]:


for a in lista:
    if a in listb:
        print("found common")
        break
else:
    print("no common")


# In[38]:


for a in lista:
    if a in listb:
        print("found common")
        break
else:
    print("no common")


# In[39]:


for a in lista:
    break
else:
    print("no common")


# In[44]:


get_ipython().run_cell_magic('python2', '', '\nx = xrange(2, 5)\n\nprint(x)')


# In[43]:


get_ipython().run_cell_magic('python2', '', '\nx = range(2, 5)\n\nprint(x)')


# In[42]:


type(x)


# In[45]:


avengers = {'captain':'sheild', 'ironman':'suit', 'vision':'stone'}


# In[46]:


for x in avengers:
    print(x)


# In[47]:


for x in avengers:
    print(x, "\t", avengers[x])


# In[48]:


for x, y in avengers.items():
    print(x, y)


# In[ ]:


x = [i for i in range(3, 5)]

