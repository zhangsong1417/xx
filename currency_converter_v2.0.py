"""
作者：张松
功能：汇率计算
版本：2.0
日期：2018.10.17
2.0 增加功能：根据输入判断是人民币还是美元，进行相应的转换计算

"""
# 汇率
USD_VS_RMB = 6.77

# 带单位的货币输入
currency_str_value = input("请输入带单位的货币金额：")

# 获取货币单位
unit = currency_str_value[-3:]

if unit == "CNY":
    # 输入的是人民币
    rmb_str_value = currency_str_value[:-3]
    # 将字符串转为数字
    rmb_str_value = eval(rmb_str_value)
    # 汇率计算
    usd_str_value = rmb_str_value/USD_VS_RMB
    print("美元金额是：", usd_str_value)
elif unit == "USD":
    # 输入的是美元
    usd_str_value = currency_str_value[:-3]
    # 将字符串转为数字
    usd_str_value = eval(usd_str_value)
    # 汇率计算
    rmb_str_value = usd_str_value*USD_VS_RMB

    # 输出结果
    print("人民币金额是：", rmb_str_value)

    # 其他情况
else:
    print('目前版本尚不支持该种货币！')
