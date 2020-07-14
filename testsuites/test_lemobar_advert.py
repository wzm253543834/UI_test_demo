# coding = utf-8
import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.lemobar_login import HomePage
from pageobjects.lemobar_advert import AdvertPage


class AdvertPageSearch(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """
        测试固件的setUp()代码，主要是测试的前提准备工作
        :return:
        """
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser(cls)

    @classmethod
    def tearDownClass(cls):
        """
        测试结束后的操作，这里基本上就是关闭浏览器
        :return:
        """
        BrowserEngine.quit_browser(cls)

    def test_a_login_lemobar(self):
        """
        乐摩吧首页账号登录
        :return:
        """
        """
        这里一定要test开头，把测试逻辑代码封装到一个test开头的方法里。
        :return:
        """
        homepage = HomePage(self.driver)
        homepage.login()
        homepage.get_window_img()
        try:
            assert '乐摩吧数据中心管理系统' in homepage.get_page_title()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))

    def test_b_advert_search(self):
        """
        广告管理查询
        :return:
        """
        homepage = AdvertPage(self.driver)
        homepage.search_click_advert()
        homepage.sleep(3)
        homepage.search_click_advert_advert()
        homepage.sleep(3)
        homepage.get_window_img()
        try:
            assert '广告管理' in homepage.find_tab_advert()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))


if __name__ == '__main__':
    unittest.main()
