#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time        


# In[2]:


def funca():
    i = 0
    for i in range(-9, 1):
        print('A will take {} seconds more'.format(i))
        time.sleep(1)
        
def funcb():
    i = 0
    for i in range(-3, 1):
        print('B will take {} seconds more'.format(i))
        time.sleep(1)
        


# In[3]:


funca()


# In[6]:


def maintask():
    print("main task")
    i = 0
    funca()
    funcb()
    for i in range(-6, 1):
        print("main will take {} seconds more".format(i))
        time.sleep(1)
    print("main exits")


# In[7]:


maintask()


# In[8]:


import multiprocessing
from multiprocessing import Process
import time
def funca():
    i = 0
    for i in range(-9, 1):
        print('A will take {} seconds more'.format(i))
        time.sleep(1)
        
def funcb():
    i = 0
    for i in range(-3, 1):
        print('B will take {} seconds more'.format(i))
        time.sleep(1)

def maintask():
    print("main task")
    pa = Process(target = funca)
    pb = Process(target = funcb)
    pa.start()
    pb.start()
    for i in range(-6, 1):
        print("main will take {} seconds more".format(i))
        time.sleep(1)
    print("main exits")


# In[9]:


maintask()


# In[10]:


maintask()


# In[11]:


import multiprocessing
from multiprocessing import Process
import time
def funca():
    i = 0
    for i in range(-9, 1):
        print('A will take {} seconds more'.format(i))
        time.sleep(1)
        
def funcb():
    i = 0
    for i in range(-3, 1):
        print('B will take {} seconds more'.format(i))
        time.sleep(1)

def maintask():
    print("main task")
    pa = Process(target = funca)
    pb = Process(target = funcb)
    pa.start()
    pb.start()
    for i in range(-6, 1):
        print("main will take {} seconds more".format(i))
        time.sleep(1)
    pa.join()
    pb.join()
    print("main exits")


# In[12]:


maintask()


# In[17]:


x = 0
y = 0
import threading
def activity():
    global x
    x = x + 1
    
def taska():
    global y
    y = y+1
    print('starting task', y)
    for var in range(1000000):
        activity()
    print('ending task', y)

def taskb():
    global y
    y = y + 1
    print('starting task', y)
    for var in range(1000000):
        activity()
    print('ending task', y)    
def main_task():
    ta = threading.Thread(target=taska)
    tb = threading.Thread(target=taskb)
    ta.start()
    tb.start()
    ta.join()
    tb.join()
    global x
    print(x)
    print("main task exits")


# In[20]:


main_task()


# In[16]:


main_task()


# In[23]:


x = 0
y = 0
import threading
lock = threading.Lock()
def activity():
    global x
    x = x + 1
    
def taska():
    global y
    print('task a needs the lock')
    global lock
    lock.acquire()
    y = y+1
    print('starting task', y)
    for var in range(100000000):
        activity()
    print('ending task', y)
    print('a will release the lock')
    lock.release()

def taskb():
    global y
    print('task b needs the lock')
    global lock
    lock.acquire()
    y = y + 1
    print('starting task', y)
    for var in range(100000000):
        activity()
    print('ending task', y)
    print('b will release the lock')
    lock.release()
    
def main_task():
    ta = threading.Thread(target=taska)
    tb = threading.Thread(target=taskb)
    ta.start()
    tb.start()
    ta.join()
    tb.join()
    global x
    print(x)
    print("main task exits")


# In[24]:


main_task()


# In[25]:


help(threading.Thread)


# In[ ]:




