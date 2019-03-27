from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()

driver.get("http://192.168.20.214/videoclient/")
sleep(5)
# 定位标签名为input的元素
#driver.find_element_by_tag_name("input").send_keys("vorx")
# 获取页面所有标签名为“input”的标签。
driver.find_elements_by_tag_name("input")[2].send_keys("vorx")
driver.find_elements_by_tag_name("input")[3].send_keys("vorx")
# 点击登录按钮
# driver.find_element_by_id("btnLogin").click()
driver.find_elements_by_tag_name("input")[4].click()
sleep(5)

driver.quit()
