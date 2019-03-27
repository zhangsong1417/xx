from selenium import webdriver
from time import sleep

# 加载浏览器驱动
#driver = webdriver.Firefox()
#driver = webdriver.Chrome()
driver = webdriver.Ie()

# 打开自学网页面
driver.get("https://www.51zxw.net")
print(driver.title)
sleep(3)

# 打开百度首页
driver.get("http://www.baidu.com")
print(driver.title)
sleep(2)

driver.quit()
