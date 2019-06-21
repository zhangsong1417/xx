from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver=webdriver.Firefox()
driver.get("http://www.baidu.com/")
driver.implicitly_wait(5)

driver.find_element(By.ID, 'kw').clear()
driver.find_element(By.NAME, 'wd').send_keys("Selenium")
driver.find_element(By.CLASS_NAME, 's_ipt').send_keys("自学网")
driver.find_element(By.CSS_SELECTOR, '#kw').send_keys("Python")

sleep(3)
driver.find_element(By.ID, 'su').click()
sleep(3)
driver.quit()
