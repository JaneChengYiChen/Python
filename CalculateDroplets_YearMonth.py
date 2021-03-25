import csv
from datetime import datetime

YearMonthDict = dict()
with open('/Users/user/Desktop/RAINdata_5MIN_RG1.csv') as csvfile:
    rows = csv.reader(csvfile)
    for data in rows:
            if(data[0]) == 'datatime':
                    continue
            time = datetime.strptime(data[0], '%Y-%m-%d %H:%M:%S')
            YearMonth = time.strftime("%Y%m")
            Hour = time.strftime("%H")
            if YearMonth not in YearMonthDict:
                    YearMonthDict[YearMonth] = dict()
            if Hour not in YearMonthDict[YearMonth]:
                    YearMonthDict[YearMonth][Hour] = 0
            amount = 0 if float(data[1]) < 0 else float(data[1])
            YearMonthDict[YearMonth][Hour] = YearMonthDict[YearMonth][Hour] + amount

print YearMonthDict

