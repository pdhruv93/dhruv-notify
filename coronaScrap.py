#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver
import time
import threading
from flask import Flask, request, jsonify, make_response
import winsound


# In[2]:


coronaurl = 'https://www.worldometers.info/coronavirus/'

coronaDriver = webdriver.Chrome("chromedriver")
coronaDriver.get(coronaurl)

duration = 1000  # milliseconds
freq = 440  # Hz
totalcases=0
totalcasesOld="0,"
deaths=0
recovered=0

def coronaCountManager():
    global totalcases
    global totalcasesOld
    global deaths
    global recovered
    
    
    
    while True:
        try:
            coronaDriver.refresh()

            print("Started Scraping")
            totalcases=coronaDriver.find_elements_by_css_selector('#maincounter-wrap .maincounter-number span')[0].text
        
            print("Old:{}  New:{}".format(totalcasesOld, totalcases))
        
            if(float(totalcases.replace(',', '')) > float(totalcasesOld.replace(',', ''))):
                winsound.Beep(freq, duration)
                
            
            deaths=coronaDriver.find_elements_by_css_selector('#maincounter-wrap .maincounter-number span')[1].text
            recovered=coronaDriver.find_elements_by_css_selector('#maincounter-wrap .maincounter-number span')[2].text
            
            totalcasesOld=coronaDriver.find_elements_by_css_selector('#maincounter-wrap .maincounter-number span')[0].text
                
            time.sleep(20)
        except:
            pass
    
            

def getCoronaCounts():
    print("Corona Counts:   Totalcases:{}, Deaths:{}, Recovered:{}".format(totalcases,deaths,recovered))


# In[ ]:


coronaThread = threading.Thread(target=coronaCountManager)

coronaThread.start()


# In[ ]:


app=Flask(__name__)

@app.route('/getcounts/', methods=['GET'])
def respond():
    response_body = {
            "totalcases": totalcases,
            "deaths": deaths,
            "recovered":recovered
        }

    res = make_response(jsonify(response_body), 200)
    return res


@app.route('/')
def index():
    getCoronaCounts()
    return '<h1>Corona App</h1>'

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)

