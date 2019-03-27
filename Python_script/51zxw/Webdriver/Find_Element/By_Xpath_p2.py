from selenium import  webdriver
from time import sleep

driver = webdriver.Firefox()

driver.get("http://192.168.20.214/videoclient/")
# 层级和属性结合定位
driver.find_element_by_xpath("//form[@id='form1']/div[4]/div[1]/div[2]/div[2]/input").send_keys("vorx")
driver.find_element_by_xpath("//form[@id='form1']/div[4]/div[1]/div[2]/div[3]/input").send_keys("vorx")
# 逻辑运算组合定位
# driver.find_element_by_xpath("//input[@class='i-text' and @name='UserName']").send_keys("vorx")
# driver.find_element_by_xpath("//input[@class='i-text' and @name='PassWord']").send_keys("vorx")
sleep(3)
driver.find_element_by_xpath("//*[@id='btnLogin']").click()
sleep(3)
driver.quit()
