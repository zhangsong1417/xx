from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
driver.get("http://www.baidu.com")

driver.find_element_by_css_selector('.soutu-btn').click()
sleep(2)
driver.find_element_by_css_selector('.upload-pic').send_keys(r"D:\xx\BMW1.jpg")

sleep(5)
driver.quit()