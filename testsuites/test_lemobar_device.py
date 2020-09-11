# coding = utf-8
import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.lemobar_login import HomePage
from pageobjects.lemobar_device import DevicePage
from pageobjects.lemobar_device import DeviceBatchSearch
from pageobjects.lemobar_device import DeviceFactorySearch
from pageobjects.lemobar_device import DeviceCustomerSearch
from pageobjects.lemobar_device import DeviceTypeSearch


class DevicePageSearch(unittest.TestCase):

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

    def test_b_devicebatch_search(self):
        """
        设备批次查询
        :return:
        """
        homepage = DevicePage(self.driver)
        homepage.search_click_divice()
        homepage.sleep(3)
        homepage.search_click_divice_devicebatch()
        homepage.sleep(3)
        homepage.get_window_img()
        try:
            assert '设备批次' in homepage.find_tab_devicebatch()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))

        newsearch = DeviceBatchSearch(self.driver)

        # 批次名称查询
        newsearch.batchname_search('20180130')
        newsearch.search_button_click()
        newsearch.sleep(2)
        try:
            assert '20180130' in newsearch.find_result_batchname()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))
        newsearch.empty_button_click()
        newsearch.sleep(2)

        # 批次ID查询
        newsearch.batchid_search('180130')
        newsearch.search_button_click()
        newsearch.sleep(2)
        try:
            assert '180130' in newsearch.find_result_batchid()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))
        newsearch.empty_button_click()
        newsearch.sleep(2)

        # 工厂名称查询
        newsearch.factoryname_search('福安荣耀')
        newsearch.search_button_click()
        newsearch.sleep(2)
        try:
            assert '福安荣耀' in newsearch.find_result_factoryname()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))
        newsearch.empty_button_click()
        newsearch.sleep(2)

        # 设备类型名称查询
        newsearch.devicetypename_search('X7')
        newsearch.search_button_click()
        newsearch.sleep(2)
        try:
            assert 'X7' in newsearch.find_result_devicetypename()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))
        newsearch.empty_button_click()
        newsearch.sleep(2)

        # 客户名称查询
        newsearch.customername_search('乐摩吧')
        newsearch.search_button_click()
        newsearch.sleep(2)
        try:
            assert '乐摩吧' in newsearch.find_result_customername()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))
        newsearch.empty_button_click()
        newsearch.sleep(2)

        # 刷新页面
        homepage.refresh()

    def test_c_devicefactory_search(self):
        """
        设备工厂查询
        :return:
        """
        homepage = DevicePage(self.driver)
        homepage.search_click_divice()
        homepage.sleep(3)
        homepage.search_click_divice_devicefactory()
        homepage.sleep(3)
        homepage.get_window_img()
        try:
            assert '设备工厂' in homepage.find_tab_devicefactory()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))

        newsearch = DeviceFactorySearch(self.driver)

        # 工厂ID查询
        newsearch.factoryid_search('4')
        newsearch.search_button_click()
        newsearch.sleep(2)
        try:
            assert '4' in newsearch.find_result_factoryid()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))
        newsearch.empty_button_click()
        newsearch.sleep(2)

        # 工厂名称查询
        newsearch.factoryname_search('福安荣耀')
        newsearch.search_button_click()
        newsearch.sleep(2)
        try:
            assert '福安荣耀' in newsearch.find_result_factoryname()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))
        newsearch.empty_button_click()
        newsearch.sleep(2)

        # 联系方式查询
        newsearch.contacts_search('13559447851')
        newsearch.search_button_click()
        newsearch.sleep(2)
        try:
            assert '13559447851' in newsearch.find_result_contacts()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))
        newsearch.empty_button_click()
        newsearch.sleep(2)

        # 刷新页面
        homepage.refresh()

    def test_d_devicecustomer_search(self):
        """
        客户数据查询
        :return:
        """
        homepage = DevicePage(self.driver)
        homepage.search_click_divice()
        homepage.sleep(3)
        homepage.search_click_divice_devicecustomer()
        homepage.sleep(3)
        homepage.get_window_img()
        try:
            assert '客户数据' in homepage.find_tab_devicecustomer()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))

        newsearch = DeviceCustomerSearch(self.driver)

        # 客户ID查询
        newsearch.customerid_search('4')
        newsearch.search_button_click()
        newsearch.sleep(2)
        try:
            assert '4' in newsearch.find_result_customerid()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))
        newsearch.empty_button_click()
        newsearch.sleep(2)

        # 客户名称查询
        newsearch.customername_search('乐摩吧')
        newsearch.search_button_click()
        newsearch.sleep(2)
        try:
            assert '乐摩吧' in newsearch.find_result_customername()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))
        newsearch.empty_button_click()
        newsearch.sleep(2)

        # 联系方式查询
        newsearch.contacts_search('13559447851')
        newsearch.search_button_click()
        newsearch.sleep(2)
        try:
            assert '13559447851' in newsearch.find_result_contacts()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))
        newsearch.empty_button_click()
        newsearch.sleep(2)

        # 刷新页面
        homepage.refresh()

    def test_f_devicetype_search(self):
        """
        设备型号查询
        :return:
        """
        homepage = DevicePage(self.driver)
        homepage.search_click_divice()
        homepage.sleep(3)
        homepage.search_click_divice_devicetype()
        homepage.sleep(3)
        homepage.get_window_img()
        try:
            assert '设备型号' in homepage.find_tab_devicetype()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))

        newsearch = DeviceTypeSearch(self.driver)

        # 型号ID查询
        newsearch.typeid_search('4')
        newsearch.search_button_click()
        newsearch.sleep(2)
        try:
            assert '4' in newsearch.find_result_typeid()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))
        newsearch.empty_button_click()
        newsearch.sleep(2)

        # 型号名称查询
        newsearch.typename_search('X2')
        newsearch.search_button_click()
        newsearch.sleep(2)
        try:
            assert 'X2' in newsearch.find_result_typename()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))
        newsearch.empty_button_click()
        newsearch.sleep(2)

        # 刷新页面
        homepage.refresh()


if __name__ == '__main__':
    unittest.main()
