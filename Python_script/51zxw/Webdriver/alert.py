from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
driver.get("https://www.baidu.com")
sleep(3)
driver.find_element_by_link_text('设置').click()
sleep(2)
# driver.find_element_by_link_text('搜索设置').click()
driver.find_element_by_link_text('高级搜索').click()
sleep(2)
# driver.find_element_by_link_text("保存设置").click()
driver.find_element_by_link_text('恢复默认').click()
sleep(2)

# 处理警告窗口
alert = driver.switch_to.alert()
alert.accept()

sleep(2)
driver.quit()
