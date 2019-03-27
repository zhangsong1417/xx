from selenium import  webdriver
from time import sleep

driver = webdriver.Firefox()

driver.get("https://www.baidu.com")

driver.find_element_by_class_name("s_ipt").send_keys("selenium我要自学网")
sleep(2)

driver.find_element_by_id("su").click()
sleep(3)

driver.quit()
