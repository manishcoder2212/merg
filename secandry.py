import csv


with open('main.csv', newline="") as f:
    reader = csv.reader(f)
    data1 = list(reader)


count = 0
for x in data1:
    if data1 == []:

        data1.pop(count)


# print(data1[0])
# print(data1[1])
# print(data1[2])
print(data1)
