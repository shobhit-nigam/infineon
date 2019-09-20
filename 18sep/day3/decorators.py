#!/usr/bin/env python
# coding: utf-8

# In[1]:


motichoor = "motichoor"
besan = "besan"


# In[2]:


def funca(x):
    print("making", x, "laddoos")
    
def funcb(x):
    print("making", x, "modaks")


# In[3]:


funca(motichoor)


# In[4]:


funcb(besan)


# In[5]:


def make(gen, x):
    gen(x)


# In[6]:


make(funca , motichoor)


# In[7]:


#higher order functions


# In[8]:


make(funca , besan)


# In[9]:


def funca():
    print("plain Ganesha")
    
def funcb(gen):
    def funcc():
        gen()
        print("decorated Ganesha")
    return funcc


# In[10]:


funcb(funca)


# In[11]:


funcx = funcb(funca)

#funcx = funcc

#funcc():
#    funca()
#    print("decorated Ganesha")


# In[12]:


funca()


# In[13]:


funcx()


# In[14]:


funcx = funcb(funca)
funca = funcb(funca)


# In[15]:


funca()


# In[16]:


def funca():
    print("plain Ganesha")
    
def funcb(gen):
    def funcc():
        gen()
        print("decorated Ganesha")
    return funcc

funca()
print("---")
funca = funcb(funca)
funca()


# In[17]:


def funcb(gen):
    def funcc():
        gen()   #plain Ganesha
        print("decorated Ganesha")
    return funcc

def funca():
    print("plain Ganesha")
funca = funcb(funca)

@funcb
def funca():
    print("plain Ganesha")

    
    
"""    
@xxx
def yyy():
    pass


yyy = xxx(yyy)
"""


# In[18]:


def hash(funca):
    def inner(*args):
        print("#" * 25)
        funca(*args)
        print("#" * 25)
    return inner

@hash
def display(msg):
    print(msg)


# In[19]:


display("hello")


# In[20]:


def hash(funca):
    def inner(*args):
        print("#" * 25)
        funca(*args)
        print("#" * 25)
    return inner

def star(funca):
    def inner(*args):
        print("*" * 25)
        funca(*args)
        print("*" * 25)
    return inner


@star
def display(msg):
    print(msg)


# In[21]:


display("hello")


# In[22]:


def hash(funca):
    def inner(*args):
        print("#" * 25)
        funca(*args)
        print("#" * 25)
    return inner

def star(funca):
    def inner(*args):
        print("*" * 25)
        funca(*args)
        print("*" * 25)
    return inner

@hash
@star
def display(msg):
    print(msg)


# In[23]:


display("hello")


# In[ ]:




