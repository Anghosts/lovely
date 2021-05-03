import csv
# 将字典中的数据保存到csv文件中，以“键”作为标题，以“值”作为数据行
data = {
'name' : ['Dave', 'Dennis', 'Peter', 'Jess'],
'language': ['Python', 'C', 'Java', 'PHP']
}
with open("file.csv", mode='w', newline="") as f:
    writer = csv.writer(f, delimiter=",")
    # 遍历key
    for i in data.keys():
        writer.writerows([[i]])
        writer.writerow(["-" * 10])
        # 遍历value
        for j in range(0, len(data[i])):
            writer.writerow([data[i][j]])
        writer.writerow(["-" * 15])

with open("file.csv", mode="r", newline="") as f:
    reader = csv.reader(f, delimiter=",")
    for po in reader:
        print(po)
