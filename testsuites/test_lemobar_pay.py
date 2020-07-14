# coding = utf-8
import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.lemobar_login import HomePage
from pageobjects.lemobar_pay import PayPage
from pageobjects.lemobar_pay import BasepaymentSearch
from pageobjects.lemobar_pay import PaymentSearch


class PayPageSearch(unittest.TestCase):

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

    def test_b_basepayment_search(self):
        """
        基础支付类型查询
        :return:
        """
        homepage = PayPage(self.driver)
        homepage.search_click_pay()
        homepage.sleep(3)
        homepage.search_click_pay_basepayment()
        homepage.sleep(3)
        homepage.get_window_img()
        try:
            assert '基础支付类型' in homepage.find_tab_basepayment()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))

        newsearch = BasepaymentSearch(self.driver)

        # ID查询
        newsearch.id_search('1')
        newsearch.search_button_click()
        newsearch.sleep(2)
        try:
            assert '1' in newsearch.find_result_id()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))
        newsearch.click_button_click()
        newsearch.sleep(2)

        # 类型名称查询
        newsearch.typename_search('微信支付')
        newsearch.search_button_click()
        newsearch.sleep(2)
        try:
            assert '微信支付' in newsearch.find_result_typename()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))
        newsearch.click_button_click()
        newsearch.sleep(2)

        # 是否启用查询
        newsearch.isenable_search()
        newsearch.search_button_click()
        newsearch.sleep(2)
        try:
            assert 'el-icon-circle-check' in newsearch.find_result_isenable()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))
        newsearch.click_button_click()
        newsearch.sleep(2)

    def test_c_payment_search(self):
        """
        支付组管理查询
        :return:
        """
        homepage = PayPage(self.driver)
        homepage.search_click_pay_payment()
        homepage.sleep(3)
        homepage.get_window_img()
        try:
            assert '支付组管理' in homepage.find_tab_payment()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))

        newsearch =PaymentSearch(self.driver)

        # 支付组ID查询
        newsearch.paymentid_search('1')
        newsearch.search_button_click()
        newsearch.sleep(2)
        try:
            assert '1' in newsearch.find_result_paymentid()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))
        newsearch.click_button_click()
        newsearch.sleep(2)

        # 支付组名称查询
        newsearch.paymentname_search('默认支付组')
        newsearch.search_button_click()
        newsearch.sleep(2)
        try:
            assert '默认支付组' in newsearch.find_result_paymentname()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))
        newsearch.click_button_click()
        newsearch.sleep(2)

        # 是否启用查询
        newsearch.isenable_search()
        newsearch.search_button_click()
        newsearch.sleep(2)
        try:
            assert 'el-icon-circle-check' in newsearch.find_result_isenable()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))
        newsearch.click_button_click()
        newsearch.sleep(2)


if __name__ == '__main__':
    unittest.main()
