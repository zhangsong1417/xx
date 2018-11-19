"""
   作者：张松
   日期：2018/11/19
   功能：
   版本：v1.0
"""

def cal_linear(iaqi_lo, iaqi_hi, bp_lo, bp_hi, cp):
    """
        范围缩放
    """
    iaqi = (iaqi_hi - iaqi_lo)*(cp)


def cal_pm_iaqi(pm_val):
    """
        计算pm2.5的IAQI
    """
    if 0 <= pm_val < 36:
        iaqi = cal_linear(0, 50, 0, 35, pm_val)


def cal_co_iaqi(co_val):
    """
        计算CO的IAQI
    """
    pass


def cal_aqi(param_list):
    """
        AQI计算
    """
    pm_val = param_list[0]
    co_val = param_list[1]

    pm_iaqi = cal_pm_iaqi(pm_val)
    co_iaqi = cal_co_iaqi(co_val)

    iaqi_list = []
    iaqi_list.append(pm_iaqi)
    iaqi_list.append(co_iaqi)

    aqi = max(iaqi_list)
    return aqi


def main():
    """
        主函数
    """
    print('请输入一下信息，用空格分割')
    input_str = input('(1)PM2.5 (2)CO:')
    str_list = input_str.split(' ')
    pm_val = float(str_list[0])
    co_val = float(str_list[1])

    param_list = []
    param_list.append(pm_val)
    param_list.append(co_val)

    # 调用AQI计算函数
    aqi_val = cal_aqi(param_list)


if __name__ == '__main__':
    main()