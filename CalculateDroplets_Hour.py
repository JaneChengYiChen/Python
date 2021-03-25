import csv
from datetime import datetime

HourDict = dict()
with open('/Users/user/Desktop/RAINdata_5MIN_RG1.csv') as csvfile:
    rows = csv.reader(csvfile)
    for data in rows:
            if(data[0]) == 'datatime':
                    continue
            time = datetime.strptime(data[0], '%Y-%m-%d %H:%M:%S')
            Hour = time.strftime("%H")
            if Hour not in HourDict:
                    HourDict[Hour] = 0
            amount = 0 if float(data[1]) < 0 else float(data[1])
            HourDict[Hour] = HourDict[Hour] + amount
print HourDict