#!/usr/bin/env python
# coding: utf-8

# In[2]:


from flask import Flask

from selenium import webdriver
import os
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)


skypeurl = 'https://web.skype.com/'
skypeusername = 'dhruv.pandey5'
skypepassword = 'dhruv.pandey5'



app=Flask(__name__)



@app.route('/')
def index():
    print("Sample___")
    return '<h1>Dhruv-----</h1>'
	
if __name__ == '__main__':
    app.run(threaded=True, port=5000)
