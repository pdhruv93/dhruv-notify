#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver
import time
import threading
from flask import Flask, request, jsonify, make_response


fbDriver = webdriver.Chrome("chromedriver")
waDriver = webdriver.Chrome("chromedriver")
ytDriver = webdriver.Chrome("chromedriver")


fburl = 'https://www.facebook.com/'
waurl = 'https://web.whatsapp.com/'
yturl = 'https://www.youtube.com/'


fbNotifications=0
msgNotifications=0
waNotifications=0
ytNotifications=0

fbDriver.get(fburl)
waDriver.get(waurl)
ytDriver.get(yturl)


        
def fbCountManager():
    global fbNotifications
    global msgNotifications
    while True:
        try:
            fbNotifications=fbDriver.find_element_by_id('notificationsCountValue')
            msgNotifications=fbDriver.find_element_by_id('mercurymessagesCountValue')
        except:
            fbNotifications=0
            msgNotifications=0

        #print("{}:".format(skypeNotifications))
        fbDriver.refresh()
        time.sleep(20)
        

def waCountManager():
    global waNotifications
    while True:
        try:
            waNotifications=0
            allMsgs=waDriver.find_elements_by_css_selector('.OUeyt')
            
            for msg in allMsgs: 
                waNotifications=waNotifications+int(msg.text) 
                
        except:
            
            waNotifications=0

        waDriver.refresh()
        time.sleep(20)
          
        
def ytCountManager():
    global ytNotifications
    while True:
        try:
            temp1=ytDriver.title.split(')')[0]
            temp2=temp1.split('(')[1]

            ytNotifications=temp2
        except:
            ytNotifications=0

        #print("{}:".format(skypeNotifications))
        ytDriver.refresh()
        time.sleep(20)
        

		
def getCoronaCounts():
    print("Facebook:{}, Messeneger:{}, Whatsapp:{}".format(fbNotifications,msgNotifications,waNotifications,ytNotifications))


fbThread = threading.Thread(target=fbCountManager)
fbThread.start()

waThread = threading.Thread(target=waCountManager)
waThread.start()

ytThread = threading.Thread(target=ytCountManager)
ytThread.start()


app=Flask(__name__)

@app.route('/getcounts/', methods=['GET'])
def respond():
    response_body = {
            "fbNotifications":fbNotifications,
            "msgNotifications": msgNotifications,
            "waNotifications": waNotifications,
            "ytNotifications": ytNotifications
        }

    res = make_response(jsonify(response_body), 200)
    return res


@app.route('/')
def index():
    getCoronaCounts()
    return '<h1>Notiifcation App</h1>'

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)

