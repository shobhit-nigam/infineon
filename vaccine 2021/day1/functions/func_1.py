#!/usr/bin/env python
# coding: utf-8

# In[1]:


2 + 3


# In[2]:


print("hello world")


# In[3]:


def greet():
    print("hello")
    print("good afternoon")


# In[4]:


greet()


# In[5]:


def funca(la, lb):
    print("la =", la)
    print("lb =", lb)
    return la + lb*2


# In[6]:


varx = funca(10, 20)


# In[7]:


print(varx)


# In[8]:


def funca(la, lb, lc):
    print("la =", la)
    print("lb =", lb)
    print("lc =", lc)


# In[9]:


funca(100, 200, 300)


# In[10]:


funca(100, 200)


# In[11]:


def funca(la, lb, lc):
    print("la =", la)
    print("lb =", lb)
    print("lc =", lc)
    return la+lb+lc, "hello", [la, 33, 45]


# In[12]:


varx, vary, varz = funca(100, 200, 300)


# In[13]:


print(varz)


# In[14]:


varx, vary = funca(100, 200, 300)


# In[15]:


x, y, z = 33, 55, 77


# In[16]:


x, y, z = 33, 55


# In[17]:


x = 33, 55, 77


# In[18]:


print(x)


# In[19]:


def funca(la, lb, lc):
    print("la =", la)
    print("lb =", lb)
    print("lc =", lc)
    return la+lb+lc, "hello", [la, 33, 45]


# In[20]:


varx = funca(100, 200, 300)


# In[21]:


print(type(varx))


# In[22]:


def funca(la, lb=77, lc=99):
    print("la =", la)
    print("lb =", lb)
    print("lc =", lc)


# In[23]:


funca(100, 200, 300)


# In[24]:


funca(100)


# In[25]:


def funcc(la=77, lb, lc=99):
    print("la =", la)
    print("lb =", lb)
    print("lc =", lc)


# In[26]:


def funcc(la=77, lb=88, lc=99):
    print("la =", la)
    print("lb =", lb)
    print("lc =", lc)


# In[27]:


funcc(lb=100)


# In[28]:


print("good noon")
print("namaste")
print("salaam")


# In[29]:


print("good noon", end=', ')
print("namaste", end=', ')
print("salaam") 


# In[30]:


help(print)


# In[32]:


def funcd(la=77, lb=88, lc=99):
    print("la =", la)
    print("lb =", lb)
    print("lc =", lc)


# In[33]:


funcd(100, 200, 300, 400, 500)


# In[34]:


def funcd(la=77, lb=88, *lc):
    print("la =", la)
    print("lb =", lb)
    print("lc =", lc)


# In[35]:


funcd(100, 200, 300, 400, 500)


# In[36]:


def funcd(la=77, lb=88, *args):
    print("la =", la)
    print("lb =", lb)
    print("args =", args) 


# In[37]:


funcd(100, 200, 300, 400, 500)


# In[38]:


def funce(la=77, lb=88, *args, **kwargs):
    print("la =", la)
    print("lb =", lb)
    print("args =", args)
    print("kwargs =", kwargs)


# In[39]:


funce(100, 200, 300, 400, 500, country='india', city='hyderabad')


# In[40]:


funce(100, lb=200, 300, 400, 500, country='india', city='hyderabad')


# In[44]:


def funcf(la=77, lb=88, **kwargs):
    print("la =", la)
    print("lb =", lb)
    print("kwargs =", kwargs)

funcf(la = 100, lb = 200, la = 300)


# In[45]:


ga = 100


# In[46]:


def funcf():
    print("ga =", ga)
    la = 66
    print("la =", la)


# In[47]:


funcf()


# In[48]:


print(la)


# In[49]:


def funcf():
    ga = 77
    print("ga =", ga)
    la = 66
    print("la =", la)


# In[50]:


ga = 100

print("ga =", ga)


# In[51]:


funcf()


# In[52]:


print("ga =", ga)


# In[53]:


def funcf():
    global ga
    ga = 77
    print("ga =", ga)
    la = 66
    print("la =", la)


# In[54]:


print("ga =", ga)


# In[55]:


funcf()


# In[56]:


print("ga =", ga)


# In[57]:


# can call functions within functions


# can create functions within functions


# In[58]:


avengers = {'captain':'sheild', 'ironman':'suit'}

marvel = {'xmen':['mystique', 'magento'], 'avengers':avengers}

superheroes = {'dc':['batman', 'catwoman', 'cyborg'], 'marvel':marvel}


# In[59]:


def get_values(d):
    for k,v in d.items():
        if type(v) is dict:
            get_values(v)
        else:
            print(v)


# In[60]:


get_values(superheroes)


# In[ ]:


avengers.

