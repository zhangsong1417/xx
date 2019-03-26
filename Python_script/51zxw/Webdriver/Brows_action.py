from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()

driver.get("https://www.51zxw.net/")
driver.maximize_window()
sleep(2)

driver.get("https://www.51zxw.net/list.aspx?cid=615")
driver.set_window_size(800, 800)
driver.refresh()
sleep(2)

driver.back()
sleep(2)

driver.forward()

sleep(2)
driver.quit()
