from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
driver.get("https://www.ctrip.com/")
sleep(4)
# 根据option标签来定位（7间三星级/舒适）
# driver.find_elements_by_tag_name('option')[6].click()
# driver.find_elements_by_tag_name('option')[175].click()
driver.find_elements_by_css_selector("[value='7']")[0].click()

sleep(5)

driver.quit()
