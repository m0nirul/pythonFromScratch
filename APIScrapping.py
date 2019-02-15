#!/usr/bin/env python
# coding: utf-8

# # API Scrapping
# ## Github unauthenticate api

# In[3]:


import requests, json
endpoint = "https://api.github.com/users/m0nirul/repos"
repos = json.loads(requests.get(endpoint).text)


# ## Twitter
# > USE YOUR OWN KEY's these are wrong [Twitter APP](https://apps.twitter.com/)

# In[8]:


from twython import Twython

CONSUMER_KEY = 'Nt1hpFpOrT387hApB4C9gGyyd' 
CONSUMER_SECRET = 't1IuBDXwEKorKkXKn2v2jbft2eeLaIv2sbfmf8VWt0wUstvT4t'
ACCESS_TOKEN = '2162160453-3t5N1ZV1RoV5Wuzy6a7Q3GUPkGe9aYQ9zUwm9MX'
ACCESS_TOKEN_SECRET = 'OsiiUHZKRmYYRN1dJhKaW2VetqaEU9Ipa89VEmgRXsnCM'


# In[6]:


twitter = Twython(CONSUMER_KEY,CONSUMER_SECRET)
for status in twitter.search(q='"data science"')["statuses"]:
    user = status["user"]["screen_name"].encode('utf-8')
    text = status["text"].encode('utf-8')
    print (user, ":", text)
#     print


# ## Twitter Stream

# In[7]:


from twython import TwythonStreamer

tweets = []
class MyStreamer(TwythonStreamer):
    def on_success(self,data):
        if data['lang'] == 'en':
            tweets.append(data)
            print("Received tweets #",data)
        if len(tweets)>1000:
            self.disconnect()
    def on_error(self,status_code,data):
        print(status_code,data)
        self.disconnect()


# In[ ]:


stream = MyStreamer(CONSUMER_KEY, CONSUMER_SECRET,ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
# starts consuming public statuses that contain the keyword 'data'
stream.statuses.filter(track='data')


# In[ ]:




