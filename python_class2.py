#!/usr/bin/env python
# coding: utf-8

# In[1]:


import this


# In[ ]:


#Deep Value and Shello Value


# In[2]:


a = 8
b = 8
print (id(a))
print (id(b))


# In[3]:


a = 8 
b = 8
print (type(a))
print (type(b))


# In[ ]:


#Data type


# In[4]:


a = 7
print(type(a))
a = '1'
print(type(a))
a = a + '1'
print(a)
b = int(a) + 5
print(type(b))
print(b)


# In[5]:


a = "shahzada munawer"
dir(a)         


# In[8]:


a = "shahzada munawer"
print(a.upper())        # In-line operation
print(a)
a = a.upper()          # In-memory
print(b)

print(a.capitalize())


# In[9]:


a = "       Shahzada munawer        "
print(len(a))
print(a.strip())
b = len(a.strip())
print(b)
print('We saved ',len(a) - b,' Charecters Space/Memory ')


# In[10]:


c = a.split()       
print(c)


# In[11]:


d = " ".join(c)      
print(d)


# In[12]:


a = "We are pakistani we love our country!"
#Slicing : Same as indexing but access more than one vlaues
b = a[7:15:1]                  # veriable[start:end:step] --> end is not included..
print(b)
print(a[::-1]) 


# In[ ]:


#Lists

