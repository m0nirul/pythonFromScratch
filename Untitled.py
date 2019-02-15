#!/usr/bin/env python
# coding: utf-8

# In[4]:


import requests, json
endpoint = "https://thispersondoesnotexist.com/"
repos = requests.get(endpoint).text


# In[5]:


print(repos)

