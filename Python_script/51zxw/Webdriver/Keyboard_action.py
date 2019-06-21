from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Firefox()
driver.get("https://www.baidu.com")
driver.find_element_by_css_selector("#kw").send_keys("Python")

sleep(3)
# 键盘全选操作Ctrl+A
driver.find_element_by_css_selector("#kw").send_keys(Keys.CONTROL, 'a')
sleep(2)

# 键盘选择复制或剪切操作Ctrl+c/Ctrl+x
driver.find_element_by_css_selector("#kw").send_keys(Keys.CONTROL, 'c')
# driver.find_element_by_css_selector("#kw").send_keys(Keys.CONTROL, 'x')

# 打开搜狗页面
driver.get("http://www.sogou.com/")
sleep(3)

# 粘贴复制内容
driver.find_element_by_css_selector(".sec-input").send_keys(Keys.CONTROL, 'v')
sleep(2)

# 点击搜索按钮
driver.find_element_by_xpath("//input[@id='stb']").click()
# driver.find_element_by_css_selector("#stb").click()

sleep(3)
driver.quit()
