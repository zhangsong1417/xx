from selenium import  webdriver
from time import sleep

driver = webdriver.Firefox()

driver.get("http://www.baidu.com")
# 根据id来定位
# driver.find_element_by_css_selector("#kw").send_keys("selenium")
# driver.find_element_by_css_selector("#su").click()
# 根据class定位
# driver.find_element_by_css_selector(".s_ipt").send_keys("selenium")
# driver.find_element_by_css_selector(".bg.s_btn").send_keys("selenium")
# 根据属性来定位
# driver.find_element_by_css_selector("[autocomplete='off']").send_keys("selenium")
# sleep(3）
# driver.find_element_by_id("su").click()
# sleep(3)

# 通过元素层级来定位
driver.find_element_by_css_selector("form#form>span>input").send_keys("selenium")
driver.find_element_by_css_selector("form#form>span>input[type='submit']").click()
sleep(3)

driver.quit()
