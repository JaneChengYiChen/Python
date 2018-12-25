#抓FBpost(notyet)
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
email.send_keys("0965...")

#enter password
password = driver.find_element_by_name("pass")
password.clear()
password.send_keys("fa...")

#press button

form = driver.find_element_by_id("login_form")
form.submit()

time.sleep(3)

driver.get("https://www.facebook.com/pg/ddcqqmei/posts/")

userContentWrapper = driver.find_elements_by_class_name("userContentWrapper")
for messages in userContentWrapper:
   for item in range(0,3):
       message = messages.find_element_by_class_name("UFIPagerLink")
       message.click()
       time.sleep(2)

for i in range(0,3):
   driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
   time.sleep(3)

block = driver.find_elements_by_class_name("_1xnd")
for all_posts in block:
   single_post = all_posts.find_elements_by_class_name("userContentWrapper")
   for post_content in single_post:
       post = post_content.find_element_by_class_name("userContent").text
       post_time = post_content.find_element_by_class_name("timestampContent").text
       print("—————————————————————————————————")
       great = post_content.find_element_by_class_name("_4arz").text
       comment_number = post_content.find_element_by_class_name("_ipm").text
       print(post)
       print("")
       print("貼文時間:{} 按讚數:{} {} ".format(post_time, great, comment_number))
       print("")

       comments = post_content.find_elements_by_class_name("UFIComment")
       for auther in comments:
           auther_name = auther.find_element_by_class_name("UFICommentActorName").text
           auther_post = auther.find_element_by_class_name("UFICommentBody").text
           print("{}:{}".format(auther_name, auther_post))
