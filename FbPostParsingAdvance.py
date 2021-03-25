#Nike版型1
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#打開Facebook的網址
driver = webdriver.Chrome("./driver/chromedriver")
driver.get("https://www.facebook.com/")

#enter email
email = driver.find_element_by_name("email")
email.clear()
email.send_keys("0965")

#enter password
password = driver.find_element_by_name("pass")
password.clear()
password.send_keys("fa")

#press button

form = driver.find_element_by_id("login_form")
form.submit()

time.sleep(3)

driver.get("https://www.facebook.com/nba.taiwan/videos/1992009344429376/")

Clickclick = driver.find_elements_by_class_name("uiStreamStory ")
for messages in Clickclick:
   message = messages.find_element_by_class_name("_2xui")
   message.click()
   time.sleep(2)

userContentWrapper = driver.find_elements_by_class_name("_3b-9 ")

time.sleep(3)

for auther in userContentWrapper:
   auther_name = auther.find_element_by_class_name("UFICommentActorName").text
   auther_post = auther.find_element_by_class_name("UFICommentBody").text
   print("{}:{}".format(auther_name, auther_post))

