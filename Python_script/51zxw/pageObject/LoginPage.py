from BasePage import *
from selenium.webdriver.common.by import By


class LoginPage(Page):
    '''首页登录页面'''

    url = '/'

    # 定位器
    username_loc = (By.NAME, 'username')
    password_loc = (By.NAME, 'password')
    summit_loc = (By.NAME, 'Submit')

    # 用户输入框元素
    def type_username(self, username):
        self.find_element(*self.username_loc).clear()
        self.find_element(*self.username_loc).send_keys(username)

    # 用户输入框元素
    def type_password(self, password):
        self.find_element(*self.password_loc).clear()
        self.find_element(*self.password_loc).send_keys(password)

    def type_summit(self):
        self.find_element(*self.submit_loc).click()


def test_user_login(driver, username, password):
    '''测试用户名密码是否可以登录'''

    login_page = LoginPage(driver)
    login_page.open()

    login_page.type_username(username)
    login_page.type_password(password)
    login_page.type_summit()
