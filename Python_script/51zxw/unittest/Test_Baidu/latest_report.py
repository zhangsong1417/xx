import os  # 用于访问操作系统功能的模块

# 报告存放位置
report_dir = './test_report'
# os.listdir()方法用于返回指定的文件夹包含的文件或文件夹的名称的列表
lists = os.listdir(report_dir)
print(lists)
# 按时间顺序对该目录文件夹下面的文件进行排序
lists.sort(key=lambda fn: os.path.getatime(report_dir + '\\' + fn))

print("the latest report is" + lists[-1])
# 输出最新报告的路径
file = os.path.join(report_dir, lists[-1])
print(file)
