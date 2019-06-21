from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()

driver.get("https://www.baidu.com/")

driver.find_element_by_link_text("新闻").click()
sleep(3)

driver.find_element_by_partial_link_text("国内").click()
sleep(3)

#driver.quit()
