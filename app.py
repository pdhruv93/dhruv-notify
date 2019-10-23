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

driver.get(skypeurl)

app=Flask(__name__)



@app.route('/')
def index():
     try:
        driver.find_element_by_id('idSIButton9')
        
        #its not login. so perform login
        print("Performing Login to Skype")
        driver.find_element_by_id('i0116').send_keys(skypeusername)
        time.sleep(2)
        driver.find_element_by_id('idSIButton9').click()
        time.sleep(2)
        driver.find_element_by_id('i0118').send_keys(skypepassword)  
        time.sleep(2)
        driver.find_element_by_id('idSIButton9').click()
        time.sleep(6)
    except:
         #its already login. refresh and get count
        driver.refresh()
        time.sleep(6)
        
        try:
            temp1=driver.title.split(')')[0]
            temp2=temp1.split('(')[1]
        
            skypeNotifications=temp2
        except:
            skypeNotifications=0
            
        if not skypeNotifications:
            skypeNotifications=0
        
        print("{}:".format(skypeNotifications))
        time.sleep(6)
    return '<h1>Dhruv-----</h1>'
	
if __name__ == '__main__':
    app.run(threaded=True, port=5000)
