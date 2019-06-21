from LoginClass_para import *
from time import sleep
from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://localhost:8080/")
driver.implicitly_wait(10)

Login().user_login(driver, '51zxw', 123456)
sleep(5)
Login().user_logout(driver)

Login().user_login(driver, 'vorx', 123456)
sleep(5)
Login().user_logout(driver)

sleep(3)
driver.quit()
