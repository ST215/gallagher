import csv
import operator
from collections import Counter

file = open("basket.csv")
data = csv.DictReader(file)

total = 0
newDic = {}
fruit_details = {}
for row in data:
    types_of_fruit = []
    print(row)

    if row['name'] not in newDic:
        tempDic = set()
        newDic[row['name']] = 1


    else: newDic[row['name']] += 1
    tempDic.add(row['size'])
    tempDic.add(row['color'])
    tempDic.add(row['shape'])

    # print("SIZE::::", row["size"])
    # print("COLOR:::", row["color"])

    # print("TEMP DIC", tempDic)
    fruit_details[row['name']] = tempDic

for key in newDic:
    total += newDic[key]

for key in fruit_details:
    print('FRUIT DETAILS',newDic[key],key, fruit_details[key])

print("TOTAL FRUITS:::::::::::", total)
print("NEW DIC!!!!", newDic)
print("TOTAL FRUIT TYPES::::::", len(newDic))
each_type_of_fruit_in_descending_order = sorted(newDic.items(), key=operator.itemgetter(1), reverse=True)
print("SORTED:::::::::::::::::", each_type_of_fruit_in_descending_order)
print("Fruit details::::",fruit_details)
