from selenium import webdriver
from time import sleep


driver = webdriver.Firefox()
driver.get("https://www.hao123.com/")
sleep(2)

# 将滚动条拖到最底部
js = 'var action=document.documentElement.scrollTop=10000'
driver.execute_script(js)
sleep(5)


# 将滚动条拖到最顶部
js = 'var action=document.documentElement.scrollTop=0'
driver.execute_script(js)
sleep(2)

driver.quit()
