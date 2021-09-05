import csv
import pandas as pd

with open('data1.csv', newline="") as f:
    reader = csv.reader(f)
    data1 = list(reader)

with open('data2.csv', newline="") as a:
    reader = csv.reader(a)
    data2 = list(reader)

header1 = data1[0]
header2 = data2[0]

pl_data1 = data1[1:]
pl_data2 = data2[1:]

headers = header1+header2

pl_datas = []
count = 0
for x in pl_data1:
    row = pl_data1[count]+pl_data2[count]
    pl_datas.append(row)
    count = count+1


print(pl_datas[0])

with open("main.csv", "a+") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(pl_datas)
