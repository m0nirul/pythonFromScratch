#!/usr/bin/env python
# coding: utf-8

# In[14]:


import urllib.request
for i in range(1000):
    urllib.request.urlretrieve("https://thispersondoesnotexist.com/", 
                           "images/tpdne_image_" + str(i) + ".png")
    print("Done => ",i)


# In[9]:


# print(repos)


# In[ ]:




