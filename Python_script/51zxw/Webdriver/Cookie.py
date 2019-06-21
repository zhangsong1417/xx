from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://www.hao123.com")

# 获取cookie的全部内容
cookie = driver.get_cookies()
# 打印全部cookie信息
print(cookie)
# 打印cookie第一组信息
print(cookie[0])

# 添加cookie
driver.add_cookie({'name':'hao123', 'value': 'www.hao123.com'})
for cookie in driver.get_cookies():
    print("%s的值%s"%(cookie['name'], cookie['value']))

driver.quit()
