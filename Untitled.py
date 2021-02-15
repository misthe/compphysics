#!/usr/bin/env python
# coding: utf-8

# In[9]:


def f(x) : return x*x - 5


# In[10]:


a=2
b=3
n=0
e=0.00001
while ( b - a > e and n<100):
    c=(a+b)/2
    if f(b)*f(c) < 0 : a=c
    else: b=c
    n=n+1
    print ('n= ' , n ,'a= ', a , 'b= ', b)


# In[ ]:




