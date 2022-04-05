#!/usr/bin/env python
# coding: utf-8

# In[42]:


lst = [1,2,3,4]


# In[3]:


type(lst)


# In[4]:


lst[2]


# In[5]:


lst[-1]


# In[7]:


type(lst[-4])


# In[43]:


lst = lst + [3.14,4.3,5.6]


# In[44]:


lst


# In[13]:


st = ['Umt','Delhi']


# In[45]:


lst = lst + st


# In[21]:


lst


# In[46]:


#using this func for added the list
lst.extend([55,66,77])


# In[47]:


lst


# In[48]:


lst.insert(3,77777)


# In[49]:


lst


# In[50]:


lst.append(st)


# In[51]:


lst


# In[33]:


lst[-1]


# In[34]:


lst[-1][1]


# In[38]:


lst[-1][1][2]


# In[53]:


del lst[3]


# In[54]:


lst


# In[55]:


lst.remove('Umt')


# In[57]:


lst.pop()


# In[58]:


lst


# In[59]:


lst.sort()


# In[61]:


lst.remove('Delhi')


# In[62]:


lst


# In[63]:


lst.sort()


# In[64]:


lst


# In[66]:


lst.sort(reverse=True)


# In[67]:


lst


# In[74]:


#Dictionary............
#Key --- unique,,, Value(s)
d = {'Country':['Pakistan','Iran','India'],
  'Capital':['Islamabad','Teharn','Delhi'],
  'population':[24.5,22.6,135.7]
 }


# In[75]:


d


# In[77]:


d.keys()


# In[79]:


d.values()


# In[80]:


d.items()


# In[82]:


for k in d.keys():
    print(k)


# In[83]:


for k in d.values():
    print(k)


# In[84]:


for k,v in d.items():
    print(k,'=>',v)


# ## Pandas Library

# In[85]:


import pandas as pd


# In[86]:


df = pd.DataFrame.from_dict(d)


# In[87]:


df


# In[90]:


df.to_csv('pbd_d3.csv',index = False , header = True)


# In[91]:


dff = pd.read_csv('pbd_d3.csv')


# In[93]:


dff.head()


# In[94]:


dff.tail()


# In[99]:


tp = (1,2,4,3)


# In[97]:


tp


# In[101]:


type(tp)


# In[104]:


tp[1] = 8


# In[106]:


tp = tp + (55,66,77)


# In[107]:


tp


# In[108]:


tp = tp + tuple(lst)


# In[109]:


tp

