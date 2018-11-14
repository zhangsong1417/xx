import os
from selenium import webdriver
os.startfile("C:\Program Files\Internet Explorer\iexplore.exe")  #方法一

#import os
#os.system(r'C:\"Program Files"\"Internet Explorer"\iexplore.exe')  #方法二

#import webbrowser
#webbrowser.open('http://www.baidu.com')   #方法三
driver = webdriver.Ie
webdriver.Ie.navigate('http://www.baidu.com')
url = 'https://www.baidu.com'
driver.get(url)
print ("access to %s " %(url))
driver.find_element_by_name("wd").send_keys("G2Bent")
