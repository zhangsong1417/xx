from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
# 设置网页文件路径，r代表路径转义
file_path = r"file:///D:\xx\Python_script\51zxw\Webdriver\Frame.html"
# 路径转义另一种写法
# file_path = 'file:///D:\\xx\\Python_script\\51zxw\\Webdriver\\Frame.html'
driver.get(file_path)

# 切换到frame页面内
driver.switch_to.frame("search")

# 定位到搜索按钮输入关键词
driver.find_element_by_css_selector("#query").send_keys("Python")
sleep(3)

driver.find_element_by_css_selector("#stb").click()

sleep(3)
driver.quit()