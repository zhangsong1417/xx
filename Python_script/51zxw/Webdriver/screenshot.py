from selenium import webdriver
from time import sleep

# 加载浏览器驱动
driver = webdriver.Firefox()

# 打开hao123页面并截图
driver.get("https://www.hao123.com/")
driver.get_screenshot_as_file(r'D:\xx\Python_script\51zxw\Webdriver\hao123.png')
sleep(2)

# 打开百度页面并截图
driver.get("https://www.baidu.com/")
driver.get_screenshot_as_file(r'D:\xx\Python_script\51zxw\Webdriver\baidu.png')

sleep(2)
driver.quit()
