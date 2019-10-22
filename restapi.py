#!/usr/bin/env python
# coding: utf-8

# In[2]:


from flask import Flask


# In[ ]:


app=Flask(__name__)


# In[ ]:


@app.route('/')
def index():
    return '<h1>Dhruv-----</h1>'
	
if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)

