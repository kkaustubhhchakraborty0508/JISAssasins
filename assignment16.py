#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Q-16 write a program to accept character and display its ASCII value and its next and previous character By Kaustubh Chakraborty

x= input("Enter the input :")
n= ord(x)
prev= n - 1
next= n + 1
a=chr(prev)
b=chr(next)
print(" ASCII value is : ",n)
print("The previous value is : ",a)
print("The next value is : ",b)


# In[ ]:




