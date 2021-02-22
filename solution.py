import csv
import operator

file = open("basket.csv")
data = csv.DictReader(file)

total = 0
newDic = {}
fruit_details = {}
fruit_days = {}
for row in data:
    types_of_fruit = []

    if row['name'] not in newDic:
        tempDic = set()
        newDic[row['name']] = 1

    if int(row['days']) >= 3:
        if row['name'] not in fruit_days:
            fruit_days[row['name']] = 1
        else:
            fruit_days[row['name']] += 1

    else:
        newDic[row['name']] += 1
    tempDic.add(row['size'])
    tempDic.add(row['color'])
    tempDic.add(row['shape'])

    fruit_details[row['name']] = tempDic

for key in newDic:
    total += newDic[key]

for key in fruit_details:
    ('FRUIT DETAILS', newDic[key], key, fruit_details[key])

def fruit_type_descending():
    print("The number of each type of fruit in descending order \n")
    processed_fruit = sorted(newDic.items(), key=operator.itemgetter(1), reverse=True)

    for i in range(len(newDic)):
        type_count = processed_fruit[i][1]
        name = processed_fruit[i][0]
        print(name + ": " + str(type_count))

def fruit_details_output():
    print("\nThe characteristics (size, color, shape, etc.) of each fruit by type\n")
    for key in fruit_details:
        characteristics_dic = fruit_details[key]
        count = newDic[key]
        characteristics = ''
        for value in characteristics_dic:
            characteristics += value + " "
        print(count, key, characteristics)

def fruit_date_output():
    print("\nHave any fruit been in the basket for over 3 days\n")
    fruit_over_three = ''
    for key in fruit_days:
        count = newDic[key]
        fruit_over_three += str(count) + " " + key + ", "
    fruit_over_three += "are over 3 days"
    print(fruit_over_three)

print("Total number of fruit:", total)
print("Types of fruit:", len(newDic))
fruit_type_descending()
fruit_details_output()
fruit_date_output()

