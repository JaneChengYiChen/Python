#Python串SQL
#pip install pymysql
#coding: utf-8 
import pandas as pd
import numpy as np
import pymysql

host = "172.20.32.127"
port1 = 3306
user1 = "as"
passwd = "rup4bj4"
db_name = "wh_youtube"

conn = pymysql.connect(host, port=port1, user=user1, passwd=passwd, db=db_name)

SQLstr = "SELECT * from ts_page_content\
       where s_area_iD = 'WH_F0147_0416'\
       and post_time> '2017-11-01'\
       and post_time< '2018-11-01'\
       order by post_time desc\
       limit 10000;"
Test = pd.read_sql(SQLstr, conn)
conn.close()
print(Test) (edited)
