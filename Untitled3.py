#!/usr/bin/env python
# coding: utf-8

# In[1]:


#loop
msg="Welcome To The Course"
print(msg[1])


# In[2]:


index=len(msg)-1
print(msg[index])


# In[9]:



numbers=range(2,20,2)
print(numbers)
numbers=list (numbers)
print(numbers)


# In[10]:


2 in numbers


# In[11]:


for n in range(10):
    print (n)


# In[19]:


msg="Welcome To The Course"
for s in range(len(msg)):
    print(msg[s])


# In[ ]:


msg="Welcome To The Course"


# In[21]:


for s in (msg): 
    print(s)


# In[23]:


list1=['huda','nareman','body']
for name in list1:
    print(name)


# In[24]:


dic={'name':'Hanan','job': 'Eng','hop':'learn'}
for key,value in dic.items():
    print(key ," ," ,value)


# In[26]:


dic.items()   #tupple


# In[30]:


# while loop
num=input('plz enter number')
while num !='0':
    print('continue')
    num=input('plz enter number')
print('bye bye')


# In[34]:


#nested loop
#step1 print- step 2 repeat
for i in range(0,5,1):
    print('*' ,end='')#on line no line under line


# In[36]:


#*******
#***********
for line in range(2):
    for i in range(0,5):
        print('*',end='')
    print('\n')


# In[ ]:




