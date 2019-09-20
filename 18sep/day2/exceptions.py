#!/usr/bin/env python
# coding: utf-8

# In[1]:


vara = 20
varb = 0
varc = 10


# In[3]:


print('first line')
varc = vara/varb
print('last line')


# In[4]:


print('first line')
try:
    varc = vara/varb
except ZeroDivisionError:
    print("handled zero division error")
print('last line')


# In[5]:


print('first line')
try:
    varc = vara/vard
except ZeroDivisionError:
    print("handled zero division error")
print('last line')


# In[6]:


print('first line')
try:
    varc = vara/vard
except ZeroDivisionError:
    print("handled zero division error")
except NameError:
    print('sorry name of variable is wrong')
print('last line')


# In[14]:


lista = [4, 5, 8, 23, 8]
print('first line')
try:
    varc = vara/vara
    varc = sum(lista)/len(lista)
    i = int(input('enter index'))
    print('value is ', lista[i])
except ZeroDivisionError:
    print("handled zero division error")
except NameError:
    print('sorry name of variable is wrong')
except:
    print('something went wrong, dont know what')
print('last line')


# In[15]:


lista[8]


# In[18]:


lista = [4, 5, 8, 23, 8]
print('first line')
try:
    try:
        varc = vara/vara
        varc = sum(lista)/len(lista)
        i = int(input('enter index'))
        print('value is ', lista[i])
    except ZeroDivisionError:
        print('value is zero, in inner exception')
except ZeroDivisionError:
    print("handled zero division error")
except NameError:
    print('sorry name of variable is wrong')
except:
    print('something went wrong, dont know what')
print('last line')


# In[23]:


def funca():
    vara = 0
    varb = 0
    try:
        varc = vara/vard
    except ZeroDivisionError:
        print('value is zero, in inner exception')
#        raise NameError
    return
    


# In[24]:


try:
    funca()
except:
    print('something wronh while calling function')


# In[30]:


try:
    varc = vara/varb
except:
    print('exception occoured')
else:
    print('else block')
finally:
    print('compulsory code')


# In[31]:


try:
    varc = vara/vara
except:
    print('exception occoured')
else:
    print('else block')
finally:
    print('compulsory code')


# In[32]:


#custom exceptions


# In[33]:


class AppException(Exception):
    "base class for all exceptions in my application"
    pass

class SmallValue(AppException):
    "raised when value is too small"
    pass

class LargeValue(AppException):
    "raised when value is too large"
    pass


# In[34]:


number = 100
while True:
    try:
        i = int(input('enter a num'))
        if i < number:
            raise SmallValue
        elif i > number:
            raise LargeValue
        break
    except SmallValue:
        print('value is too small, try again')
    except LargeValue:
        print('value is too large, try again')
        
print('congrats, guessed it correctly')


# In[ ]:




