#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Q-8 write a program to swap the value of two variables by call by reference By Kaustubh Chakraborty

x = int(input("Enter first number"))
y = int(input("Enter second number"))
def swap(w,v):
    return v,w
x,y=swap(x , y)
print("first number is:",x)
print("second number is :",y)


# In[ ]:




