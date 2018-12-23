"""
    作者：张松
    版本：V1.0
    日期：2018/10/30
    功能：输入某年某月某日，判断这一天是这一年中的第几天？

"""
from _datetime import datetime


def main():
    input_date_str = input('请输入日期（yyyy/mm/dd）')
    input_date = datetime.strptime(input_date_str, '%Y/%m/%d')
    print(input_date)


    year = input_date.year
    mouth = input_date.month
    day = input_date.day

    # 计算之前月份天数的总和以及当前月份的天数
    days_in_mouth_tup = (31,28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    # print(days_in_mouth_tup[:mouth -1])
    days = sum(days_in_mouth_tup[:mouth - 1]) + day

    # 判断闰年
    if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
        if mouth > 2:
            days += 1

    print('这是第{}天。'.format(days))


if __name__ == '__main__':
    main()
