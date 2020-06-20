# coding=utf-8
import time
import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.lemobar_homepage import HomePage


class LemobarSearch(unittest.TestCase):

    @classmethod
    # def setUp(self):
    def setUpClass(cls):
        """
        测试固件的setUp()代码，主要是测试的前提准备工作
        :return:
        """
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser(cls)

    @classmethod
    # def tearDown(self):
    def tearDownClass(cls):
        """
        测试结束后的操作，这里基本上就是关闭浏览器
        :return:
        """
        BrowserEngine.quit_browser(cls)

    def test_enter_lemobar(self):
        """
        测试1
        """
        """
        这里一定要test开头，把测试逻辑代码封装到一个test开头的方法里。
        :return:
        """
        """
        self.driver.find_element_by_id('kw').send_keys('selenium')
        self.driver.find_element_by_id('su').click()
        time.sleep(2)
        """
        homepage = HomePage(self.driver)
        # homepage.type_search('selenium')  # 调用页面对象中的方法
        # homepage.send_submit_btn()  # 调用页面对象类中的点击搜索按钮方法
        # time.sleep(30)
        homepage.input_username('wangzm')
        homepage.input_password('a645765783')
        homepage.sleep(20)
        homepage.enter_homepage()
        homepage.sleep(20)
        homepage.get_window_img()  # 调用基类截图方法
        try:
            assert 'selenium' in homepage.get_page_title()
            print('Test Pass.')
        except Exception as e:
            print('Test Fail.', format(e))

    def test_homepage_search(self):
        """
        测试2
        """
        homepage = HomePage(self.driver)
        homepage.search_click_branch()
        homepage.sleep(3)
        homepage.search_click_branch_branch()
        time.sleep(5)
        homepage.get_window_img()


if __name__ == '__main__':
    unittest.main()
