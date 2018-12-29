#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Q-2 write a program to accept'n' numbers from user,store these into an array.find out maximum and minun number from the array By Kaustubh Chakraborty
num=[]
n=int(input("how many numbers u want to enter"))
for i in range(1,n+1,1):
    x=int(input("enter the number"))
    num.append(x)
print("the numbers in tha array are",num)
print("max number in the array is",max(num))
print("min number in the array is",min(num))


# In[ ]:




