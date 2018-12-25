from selenium import webdriver
import time

driver=webdriver.PhantomJS("./phantomjs")
driver.get("https://trends.google.com.tw/trends/hottrends#pn=p12") #google 趨勢的網址

for index in range(0,5) : #index 是名字而已
    hot_div= driver.find_elements_by_class_name("feed-list-wrapper") #整個頁面

    for single_div in hot_div: #走一遍，並且每個都取一個名字
        date_text = single_div.find_element_by_class_name("content-header-title").text #標題
        hot_row = single_div.find_elements_by_class_name("feed-item-header") #一橫欄
        if date_text != "":
            print("-------",date_text,"--------")
            for single_row in hot_row:
                title = single_row.find_element_by_class_name("title").text
                print(title)
    botton = driver.find_element_by_class_name("feed-load-more-button") #載入更多
    botton.click()
    time.sleep(3) #等3秒

driver.close()
