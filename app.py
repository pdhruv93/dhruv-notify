from selenium import webdriver
import time
import threading
from flask import Flask

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
skypeDriver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)


skypeurl = 'https://web.skype.com/'
skypeusername = 'dhruv.pandey5'
skypepassword = 'dhruv.pandey5'

skypeNotifications=0
skypeDriver.get(skypeurl)

def skypeCountManager():
    global skypeNotifications
    while True:
        try:
            skypeDriver.find_element_by_id('idSIButton9')

            #its not login. so perform login
            print("Performing Login to Skype")
            skypeDriver.find_element_by_id('i0116').send_keys(skypeusername)
            time.sleep(2)
            skypeDriver.find_element_by_id('idSIButton9').click()
            time.sleep(2)
            skypeDriver.find_element_by_id('i0118').send_keys(skypepassword)  
            time.sleep(2)
            skypeDriver.find_element_by_id('idSIButton9').click()
            time.sleep(6)
        except:
             #its already login. refresh and get count
            skypeDriver.refresh()
            time.sleep(6)

            try:
                temp1=skypeDriver.title.split(')')[0]
                temp2=temp1.split('(')[1]

                skypeNotifications=temp2
            except:
                skypeNotifications=0

            if not skypeNotifications:
                skypeNotifications=0

            #print("{}:".format(skypeNotifications))
            time.sleep(6)
		
def getNotificationCounts():
    #print("Facebook Count: {},{}".format(fbNotifications,messengerNotifications))
    print("Skype Count: {}".format(skypeNotifications))
	
skypeThread = threading.Thread(target=skypeCountManager)
skypeThread.start()

app=Flask(__name__)
@app.route('/')
def index():
    getNotificationCounts()
    return '<h1>Dhruv-----</h1>'

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
