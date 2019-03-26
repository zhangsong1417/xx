# f = open('stu_info.txt', 'r')
# lines = f.readlines()
# print(lines)
#
# for line in lines:
#     print(line.split(',')[0])
'''
import  csv
csv_file =csv.reader(open('stu_info.csv', 'r'))
print(csv_file)

for stu in csv_file:
    print(stu[1])
'''

import csv
stu = ['Marry', 28, 'Changsha']
stu1 = ['Rom', 23, 'Chengdu']
# 打开文件
out = open('stu_info.csv', 'a', newline='')
# 设定写入模式
csv_write = csv.writer(out, dialect='excel')
# 写入具体内容
csv_write.writerow(stu)
csv_write.writerow(stu1)
print("Write file over！")
