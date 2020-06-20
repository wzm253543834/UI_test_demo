# coding = utf-8
# import time
import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.lemobar_login import HomePage
from pageobjects.lemobar_branch import BranchPage


class BranchSearch(unittest.TestCase):

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

    def test_a_login_lemobar(self):
        """
        乐摩吧首页账号登录
        :return:
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
        homepage.login()
        homepage.get_window_img()  # 调用基类截图方法
        try:
            assert '乐摩吧数据中心管理系统' in homepage.get_page_title()
            print('Test Pass.')
        except Exception as e:
            print('Test Fail.', format(e))

    def test_b_branch_search(self):
        """
        网点管理查询
        :return:
        """
        homepage = BranchPage(self.driver)
        homepage.search_click_branch()
        homepage.sleep(3)
        homepage.search_click_branch_branch()
        homepage.sleep(3)
        homepage.get_window_img()
        try:
            assert '网点管理' in homepage.find_tab_branch()
            print('Test Pass')
        except Exception as e:
            print('Test Fail.', format(e))

    def test_c_price_search(self):
        """
        价格管理查询
        :return:
        """
        homepage = BranchPage(self.driver)
        homepage.search_click_branch_price()
        homepage.sleep(3)
        homepage.get_window_img()
        try:
            assert '价格管理' in homepage.find_tab_price()
            print('Test Pass')
        except Exception as e:
            print('Test Fail.', format(e))

    def test_d_equipment_search(self):
        """
        设备列表查询
        :return:
        """
        homepage = BranchPage(self.driver)
        homepage.search_click_branch_equipment()
        homepage.sleep(3)
        homepage.get_window_img()

    def test_e_equipmessage_search(self):
        """
        设备信息查询
        :return:
        """
        homepage = BranchPage(self.driver)
        homepage.search_click_branch_equipmessage()
        homepage.sleep(3)
        homepage.get_window_img()

    def test_f_abequipment_search(self):
        """
        异常设备列表查询
        :return:
        """
        homepage = BranchPage(self.driver)
        homepage.search_click_branch_abequipment()
        homepage.sleep(3)
        homepage.get_window_img()

    def test_g_contractwarn_search(self):
        """
        合同预警查询
        :return:
        """
        homepage = BranchPage(self.driver)
        homepage.search_click_branch_contractwarn()
        homepage.sleep(3)
        homepage.get_window_img()

    def test_h_sitemanage_search(self):
        """
        场地管理查询
        :return:
        """
        homepage = BranchPage(self.driver)
        homepage.search_click_branch_sitemanage()
        homepage.sleep(3)
        homepage.get_window_img()

    def test_i_officemanage_search(self):
        """
        分公司管理查询
        :return:
        """
        homepage = BranchPage(self.driver)
        homepage.search_click_branch_officemanage()
        homepage.sleep(3)
        homepage.get_window_img()


if __name__ == '__main__':
    unittest.main()
