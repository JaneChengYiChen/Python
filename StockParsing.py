#股票
from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv
from time import localtime, strftime #strftime=string format time  將時間轉為字串
from os.path import exists #檢查檔案有沒有存在，再將標籤列寫進，資料寫進

#print(urlopen("http://rate.bot.com.tw/xrt?Lang=zh-TW"))
#第一步驟是得到網頁(上面)
#第二步驟─安裝beautifulsoup4
#第三部分─儲存起來
response=urlopen("http://rate.bot.com.tw/xrt?Lang=zh-TW")
html=BeautifulSoup(response,"html.parser") #後面的""裡的東西會因為電腦而有差異
html.find("table")
print(html.find("table").find("tbody").findAll("tr")) #抽取出table 這整串元素，抽取出tbody整串元素
for single_tr in html.find("table").find("tbody").findAll("tr"):
    rate =single_tr.findAll("td")[2].contents[0] #這樣就可以直接拿出td 的列，但還位萃取出內容
    currency=single_tr.findAll("td")[0].find("div",{"class":"visible-phone"}).contents[0] #將幣別和數字拿出來了，後面再找出div，再找出class 屬性，contents[0]→拿出內容，第0是全部的內容
    currency = currency.replace(" ", "")  # 去掉空白#replace是產生新資料的一種函式
    currency = currency.replace("\r", "")
    currency = currency.replace("\n", "")  # 清換行
    print(currency,rate)

    time_str = strftime("%Y-%m-%d %H:%M:%S", localtime())
    file_name="./result/"+currency+".csv" #成為 CSV 檔
    if not exists(file_name): #加標籤列
        f = open(file_name, "a", newline="")
        writer = csv.writer(f)
        writer.writerow(["時間", "匯率"])
        f.close()
    f = open(file_name,"a",newline="") #r=read only  w=重新寫過 a=加在原本檔案的最後面 newline =將空格去除掉
    writer = csv.writer(f) #writer要跟檔案連在一起
    writer.writerow([time_str, rate]) #writerow=寫一筆資料，記得每次都要 close writer，代表儲存的意思，[ ]=list 意思
    f.close() #記得把檔案關閉

#PLOT
import matplotlib.pyplot as plt #plt是大家習慣用語，plotlib都是英文版的
#plt.plot([1,2,3],[4,5,6]) #前面是x座標  後面是y座標
#plt.show()
import csv
from datetime import datetime #strftime=將時間字串變成時間資料

f = open( "./result/日圓(JPY).csv", "r") #r=only read
#print(csv.DictReader(f))
x_axis=[] #用 list 表示
y_axis=[]
for single_row in csv.DictReader(f):
    timeOBJ = datetime.strptime(single_row["時間"],"%Y-%m-%d %H:%M:%S")
    x_axis.append(timeOBJ)
    y_axis.append(single_row["匯率"])
plt.plot(x_axis,y_axis)
plt.gcf().autofmt_xdate() #plt.gcf是專門畫圖的東西，可以比較漂亮
plt.show()

#test1
import matplotlib.pyplot as plt #plt是大家習慣用語，plotlib都是英文版的
#plt.plot([1,2,3],[4,5,6]) #前面是x座標  後面是y座標
#plt.show()
import csv
from datetime import datetime #strftime=將時間字串變成時間資料

f = open( "./result/日圓(JPY).csv", "r") #r=only read
#print(csv.DictReader(f))
x_axis=[] #用 list 表示
y_axis=[]
for single_row in csv.DictReader(f):
    timeOBJ = datetime.strptime(single_row["時間"],"%Y-%m-%d %H:%M:%S")
    x_axis.append(timeOBJ)
    y_axis.append(single_row["匯率"])
plt.plot(x_axis,y_axis)
plt.gcf().autofmt_xdate() #plt.gcf是專門畫圖的東西，可以比較漂亮
plt.show()


#test2
from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv
from time import localtime, strftime #strftime=string format time  將時間轉為字串
from os.path import exists

response=urlopen("http://rate.bot.com.tw/xrt?Lang=zh-TW")
html=BeautifulSoup(response,"html.parser") #後面的""裡的東西會因為電腦而有差異
html.find("table")

for single_tr in html.find("table").find("tbody").findAll("tr"):
    rate =single_tr.findAll("td")[2].contents[0] #這樣就可以直接拿出td 的列，但還位萃取出內容
    currency=single_tr.findAll("td")[0].find("div",{"class":"visible-phone"}).contents[0] #將幣別和數字拿出來了，後面再找出div，再找出class 屬性，contents[0]→拿出內容，第0是全部的內容
    currency = currency.replace(" ", "")  # 去掉空白#replace是產生新資料的一種函式
    currency = currency.replace("\r", "")
    currency = currency.replace("\n", "")  # 清換行
    print(currency,rate)

