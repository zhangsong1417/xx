#导包（驱动和selenium）
import selenium
from selenium import webdriver

#导包（延时）
from time import sleep

#驱动谷歌浏览器
driver = webdriver.Iedriver()

#变量操作 确认地址
url = "www.baidu.com"
#驱动调用浏览器地址
driver.get(url)

#延时3s
sleep(3)
#退出
driver.quit()