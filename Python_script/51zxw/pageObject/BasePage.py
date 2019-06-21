from time import sleep


class Page():
    '''页面基础类'''

    # 初始化
    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'http://localhost:8080'
        self.timeout = 10

    # 打开不同的子页面
    def _open(self, url):
        url_ = self.base_url + url
        print("Test page is: %s" %url_)
        self.driver.maximize_window()
        self.driver.get(url_)
        sleep(2)
        assert self.driver.current_url == url_, 'Did not land on %s' %url_

    def open(self):
        self._open(self.url)

    # 元素定位方法封装
    def find_element(self, *loc):
        return self.driver.find_element(*loc)
