from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import Select

driver = webdriver.Firefox()
driver.get("https://www.ctrip.com/")
sleep(4)
# 利用Select类来定位（7间三星级/舒适）
roomCount = Select(driver.find_element_by_css_selector("#J_roomCountList"))
# roomCount.select_by_index(6)
# roomCount.select_by_visible_text("7间")
roomCount.select_by_value("7")
star = Select(driver.find_element_by_css_selector("[name='Star']"))
# star.select_by_index(3)
# star.select_by_visible_text("三星级/舒适")
star.select_by_value("3")

sleep(2)

driver.quit()
