from LoginClass import *
from time import sleep
from selenium import webdriver

driver=webdriver.Firefox()
driver.get("http://localhost:8080/")


Login().user_login(driver)
sleep(5)
Login().user_logout(driver)

sleep(3)
driver.quit()
