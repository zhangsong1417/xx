from selenium import webdriver
from time import sleep


class Login():
    def user_login(self, driver, username, password):
        # 输入用户名
        driver.find_element_by_name('username').clear()
        driver.find_element_by_name('username').send_keys(username)
        # 输入密码
        driver.find_element_by_name('password').clear()
        driver.find_element_by_name('password').send_keys(password)
        # 点击登录
        driver.find_element_by_name('Submit').click()

    def user_logout(self, driver):
        driver.find_element_by_link_text('退出').click()
        sleep(5)
        # 退出
        driver.switch_to_alert().accept()
