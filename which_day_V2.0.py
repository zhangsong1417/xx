"""
    作者：张松
    版本：V2.0
    日期：2018/10/30
    功能：输入某年某月某日，判断这一天是这一年中的第几天？
    2.0增加功能：用列表替换元组

"""
from _datetime import datetime


def is_leap_year(year):

    """
        判断year是否为闰年
        是，返回True
        否，返回False
    """
    is_leap = False

    if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
        is_leap = True

    return is_leap


def main():
    input_date_str = input('请输入日期（yyyy/mm/dd）')
    input_date = datetime.strptime(input_date_str, '%Y/%m/%d')
    # print(input_date)

    year = input_date.year
    mouth = input_date.month
    day = input_date.day

    # 计算之前月份天数的总和以及当前月份的天数
    days_in_mouth_list = [31,28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap_year(year):
        days_in_mouth_list[1] = 29
    days = sum(days_in_mouth_list[:mouth - 1]) + day

    print('这是{}年的第{}天。'.format(year, days))


if __name__ == '__main__':
    main()
