import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from plyer import notification
import sys
WEBDRIVERPATH = r"TypingTest/chromedriver.exe"
SITE_URL = "https://cpstest.org/typing-speed-test/1-minute.php"

global driver
driver = webdriver.Chrome(executable_path=WEBDRIVERPATH)

driver.get(SITE_URL) #Opens The SpeedTest Site in Chrome
time.sleep(5)


SpeedTestTimer = driver.find_element_by_id("timer")
while True:
    
    try:
        currentWord = driver.find_element_by_class_name("current-word")
        TypeBox = driver.find_element_by_id("typebox")
        TypeBox.send_keys(currentWord.text)
        TypeBox.send_keys(Keys.SPACE)

        
    except:
        break
        

notification.notify(
            title = "The TypingSpeedTest Bot Is Done",
            message = "The TypingSpeedTest Bot Has Finished The Speed Test",
            timeout = 10,
        )

time.sleep(10)
driver.close()
sys.exit()