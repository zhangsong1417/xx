from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
driver.get("http://rm.vorx.com.cn/redmine/")
sleep(4)
# 根据option标签来定位
driver.find_elements_by_tag_name('option')[2].click()
# driver.find_element_by_css_selector('[value="3"]').click()
sleep(2)

driver.quit()
