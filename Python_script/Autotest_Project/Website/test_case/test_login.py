import unittest
from model import function, myunit
from page_object.LoginPage import *
from time import sleep


class LoginTest(myunit.StartEnd):
    # @unittest.skip('skip this case')
    def test_login1_normal(self):
        '''username password is normal'''
        print("test_login1_normal is start run...")
        po = LoginPage(self.driver)
        po.Login_action('51zxw', 123456)

       # sleep(5)

        # 断言与截屏
        self.assertEqual(po.type_loginPass_hint(), "我的空间")
        function.insert_img(self.driver, '51zxw_login1_normal.jpg')
        print("test_login1_normal is test end!")

    def test_login2_passwdError(self):
        '''username is ok,password is error!'''
        print("test_login2_PasswdError is start run...")
        po = LoginPage(self.driver)
        po.Login_action("51zxw", 12342)
        sleep(2)

        self.assertEqual(po.type_loginFail_hint(), '')
        function.insert_img(self.driver, "51zxw_login2_fail.jpg")
        print("test_login2_PasswdError is test end!")

    def test_login3_empty(self):
        '''username password is empty'''
        print("test_login3_empty is start run...")
        po = LoginPage(self.driver)
        po.Login_action("", "")
        sleep(2)

        self.assertEqual(po.type_loginFail_hint(), '')
        function.insert_img(self.driver, "51zxw_login3_empty.jpg")
        print("test_login3_empty is test end!")

    if __name__ == '__main__':
        unittest.main()
