from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
driver.get('http://www.baidu.com/')

# 手动添加cookie
driver.add_cookie({'name': 'BAIDUID', 'value': '9E4BF1D44014F344D40E6A3EB389A3:FG=1'})
driver.add_cookie({'name': 'BDUSS','value': 'NLddddddfdfd???'})

sleep(2)
driver.refresh()

sleep(2)
driver.quit()