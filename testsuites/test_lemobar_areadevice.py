# coding = utf-8
# import time
import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.lemobar_login import HomePage
from pageobjects.lemobar_areadevice import AreadevicePage
from pageobjects.lemobar_areadevice import AreaSearch
from pageobjects.lemobar_areadevice import PriceSearch
from pageobjects.lemobar_areadevice import DevicelistSearch
from pageobjects.lemobar_areadevice import DeviceInfoSearch
from pageobjects.lemobar_areadevice import EpdevicelistSearch
from pageobjects.lemobar_areadevice import ContractSearch
from pageobjects.lemobar_areadevice import PlaceSearch
from pageobjects.lemobar_areadevice import CompanySearch


class AreadevicePageSearch(unittest.TestCase):

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

    def test_b_area_search(self):
        """
        网点管理查询
        :return:
        """
        homepage = AreadevicePage(self.driver)
        homepage.search_click_areadevice()
        homepage.sleep(3)
        homepage.search_click_areadevice_area()
        homepage.sleep(3)
        homepage.get_window_img()
        try:
            assert '网点管理' in homepage.find_tab_area()
            print('Test Pass')
        except Exception as e:
            print('Test Fail.', format(e))

        newsearch = AreaSearch(self.driver)
        # 网点ID查询
        newsearch.areaid_search('22515')
        newsearch.search_button_click()
        newsearch.sleep(2)
        try:
            assert '22515' in newsearch.find_result_areaid()
            print('Test Pass')
        except Exception as e:
            print('Test Fail.', format(e))

        newsearch.clear_button_click()
        newsearch.sleep(2)
        # 网点名称查询
        newsearch.areaname_search('福州展示仓01')
        newsearch.search_button_click()
        newsearch.sleep(2)
        newsearch.clear_button_click()
        newsearch.sleep(2)
        # 分公司名称查询
        newsearch.companyname_search()
        newsearch.search_button_click()
        newsearch.sleep(2)
        newsearch.clear_button_click()
        newsearch.sleep(2)
        # 网点启用状态查询
        newsearch.areaenablestatus_search()
        newsearch.search_button_click()
        newsearch.sleep(2)
        newsearch.clear_button_click()
        newsearch.sleep(2)
        # 周边网点状态查询
        newsearch.besideareastatus_search()
        newsearch.search_button_click()
        newsearch.sleep(2)
        newsearch.clear_button_click()
        newsearch.sleep(2)
        # 合伙人查询
        newsearch.partnername_search('直营仓库')
        newsearch.search_button_click()
        newsearch.sleep(2)
        newsearch.clear_button_click()
        newsearch.sleep(2)
        # 设备型号查询
        newsearch.devicemodel_search()
        newsearch.search_button_click()
        newsearch.sleep(2)
        newsearch.clear_button_click()
        newsearch.sleep(2)
        # 合作类型查询
        newsearch.partnertype_search()
        newsearch.search_button_click()
        newsearch.sleep(2)
        newsearch.clear_button_click()
        newsearch.sleep(2)
        # 场地名称查询
        newsearch.placename_search('福州展示仓')
        newsearch.search_button_click()
        newsearch.sleep(2)
        newsearch.clear_button_click()
        newsearch.sleep(2)
        # 是否仓库查询
        newsearch.iswarehouse_search()
        newsearch.search_button_click()
        newsearch.sleep(2)
        newsearch.clear_button_click()
        newsearch.sleep(2)
        # 刷新页面
        homepage.refresh()

    def test_c_price_search(self):
        """
        价格管理查询
        :return:
        """
        homepage = AreadevicePage(self.driver)
        homepage.search_click_areadevice_price()
        homepage.sleep(3)
        homepage.get_window_img()
        try:
            assert '价格管理' in homepage.find_tab_price()
            print('Test Pass')
        except Exception as e:
            print('Test Fail.', format(e))

        newsearch = PriceSearch(self.driver)
        # 唤醒身体价格查询
        newsearch.wakeupbodyprice_search('10')
        newsearch.search_button_click()
        newsearch.sleep(2)
        newsearch.clear_button_click()
        newsearch.sleep(2)
        # 通行气血价格查询
        newsearch.passbreathbloodprice_search('10')
        newsearch.search_button_click()
        newsearch.sleep(2)
        newsearch.clear_button_click()
        newsearch.sleep(2)
        # 舒张筋骨价格查询
        newsearch.diastolemeridiansprice_search('10')
        newsearch.search_button_click()
        newsearch.sleep(2)
        newsearch.clear_button_click()
        newsearch.sleep(2)
        # 价格ID查询
        newsearch.priceid_search('10')
        newsearch.search_button_click()
        newsearch.sleep(2)
        newsearch.clear_button_click()
        newsearch.sleep(2)
        # 是否启用查询
        newsearch.isenable_search()
        newsearch.search_button_click()
        newsearch.sleep(2)
        newsearch.clear_button_click()
        newsearch.sleep(2)
        # 唤醒身体时长查询
        newsearch.wakeupbodytime_search('10')
        newsearch.search_button_click()
        newsearch.sleep(2)
        newsearch.clear_button_click()
        newsearch.sleep(2)
        # 通行气血时长查询
        newsearch.passbreathbloodtime_search('10')
        newsearch.search_button_click()
        newsearch.sleep(2)
        newsearch.clear_button_click()
        newsearch.sleep(2)
        # 舒张筋骨时长查询
        newsearch.diastolemeridianstime_search('10')
        newsearch.search_button_click()
        newsearch.sleep(2)
        newsearch.clear_button_click()
        newsearch.sleep(2)
        # 价格名称查询
        newsearch.pricename_search('通用价格组')
        newsearch.search_button_click()
        newsearch.sleep(2)
        newsearch.clear_button_click()
        newsearch.sleep(2)
        # 刷新页面
        homepage.refresh()

    def test_d_devicelist_search(self):
        """
        设备列表查询
        :return:
        """
        homepage = AreadevicePage(self.driver)
        homepage.search_click_areadevice_devicelist()
        homepage.sleep(3)
        homepage.get_window_img()
        try:
            assert '设备列表' in homepage.find_tab_devicelist()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))

        newsearch = DevicelistSearch(self.driver)
        # 设备ID查询
        newsearch.deviceid_search('123456')
        newsearch.search_button_click()
        newsearch.sleep(2)
        newsearch.clear_button_click()
        newsearch.sleep(2)
        # 设备名称查询
        newsearch.devicename_search('测试')
        newsearch.search_button_click()
        newsearch.sleep(2)
        newsearch.clear_button_click()
        newsearch.sleep(2)
        # 设备型号查询
        newsearch.devicemodel_search()
        newsearch.search_button_click()
        newsearch.sleep(2)
        newsearch.clear_button_click()
        newsearch.sleep(2)
        # 网点ID查询
        newsearch.areaid_search('22515')
        newsearch.search_button_click()
        newsearch.sleep(2)
        newsearch.clear_button_click()
        newsearch.sleep(2)
        # 网点名称查询
        newsearch.areaname_search('福州展示仓01')
        newsearch.search_button_click()
        newsearch.sleep(2)
        newsearch.clear_button_click()
        newsearch.sleep(2)
        # 合伙人查询
        newsearch.partnername_search('直营仓库')
        newsearch.search_button_click()
        newsearch.sleep(2)
        newsearch.clear_button_click()
        newsearch.sleep(2)
        # 设备状态查询
        newsearch.devicestatus_search()
        newsearch.search_button_click()
        newsearch.sleep(2)
        newsearch.clear_button_click()
        newsearch.sleep(2)
        # 发货时间查询
        newsearch.delivertime_search()
        newsearch.search_button_click()
        newsearch.sleep(2)
        newsearch.clear_button_click()
        newsearch.sleep(2)
        # 设备启用状态查询
        newsearch.deviceisenablestatus_search()
        newsearch.search_button_click()
        newsearch.sleep(2)
        newsearch.clear_button_click()
        newsearch.sleep(2)
        # 移机时间（大于）查询
        newsearch.movetime_search('10')
        newsearch.search_button_click()
        newsearch.sleep(2)
        newsearch.clear_button_click()
        newsearch.sleep(2)
        # 是否在仓查询
        newsearch.isinwarehouse_search()
        newsearch.search_button_click()
        newsearch.sleep(2)
        newsearch.clear_button_click()
        newsearch.sleep(2)
        # 标签查询
        newsearch.tag_search('测试')
        newsearch.search_button_click()
        newsearch.sleep(2)
        newsearch.clear_button_click()
        newsearch.sleep(2)
        # 是否报废查询
        newsearch.isscrap_search()
        newsearch.search_button_click()
        newsearch.sleep(2)
        newsearch.clear_button_click()
        newsearch.sleep(2)
        # 刷新页面
        newsearch.refresh()

    def test_e_deviceInfo_search(self):
        """
        设备信息查询
        :return:
        """
        homepage = AreadevicePage(self.driver)
        homepage.search_click_areadevice_deviceInfo()
        homepage.sleep(3)
        homepage.get_window_img()
        try:
            assert '设备信息' in homepage.find_tab_deviceInfo()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))

        newsearch = DeviceInfoSearch(self.driver)
        # 设备ID查询
        newsearch.deviceid_search('123456')
        newsearch.search_button_click()
        newsearch.sleep(2)
        newsearch.clear_button_click()
        newsearch.sleep(2)
        # 设备型号查询
        newsearch.devicemodel_search()
        newsearch.search_button_click()
        newsearch.sleep(2)
        newsearch.clear_button_click()
        newsearch.sleep(2)
        # 网点ID查询
        newsearch.areaid_search('22515')
        newsearch.search_button_click()
        newsearch.sleep(2)
        newsearch.clear_button_click()
        newsearch.sleep(2)
        # 网点名称查询
        newsearch.areaname_search('福州展示仓01')
        newsearch.search_button_click()
        newsearch.sleep(2)
        newsearch.clear_button_click()
        newsearch.sleep(2)
        # 设备状态查询
        newsearch.devicestatus_search()
        newsearch.search_button_click()
        newsearch.sleep(2)
        newsearch.clear_button_click()
        newsearch.sleep(2)
        # 是否启用查询
        newsearch.isenable_search()
        newsearch.search_button_click()
        newsearch.sleep(2)
        newsearch.clear_button_click()
        newsearch.sleep(2)
        # SIM卡号查询
        newsearch.simcardnumber_search('1')
        newsearch.search_button_click()
        newsearch.sleep(2)
        newsearch.clear_button_click()
        newsearch.sleep(2)
        # 刷新页面
        newsearch.refresh()

    def test_f_epdevicelist_search(self):
        """
        异常设备列表查询
        :return:
        """
        homepage = AreadevicePage(self.driver)
        homepage.search_click_areadevice_epdevicelist()
        homepage.sleep(3)
        homepage.get_window_img()
        try:
            assert '异常设备列表' in homepage.find_tab_epdevicelist()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))

        newsearch = EpdevicelistSearch(self.driver)
        # 设备ID查询
        newsearch.deviceid_search('123456')
        newsearch.search_button_click()
        newsearch.sleep(2)
        newsearch.clear_button_click()
        newsearch.sleep(2)
        # 设备名称查询
        newsearch.devicename_search('测试')
        newsearch.search_button_click()
        newsearch.sleep(2)
        newsearch.clear_button_click()
        newsearch.sleep(2)
        # 设备型号查询
        newsearch.devicemodel_search()
        newsearch.search_button_click()
        newsearch.sleep(2)
        newsearch.clear_button_click()
        newsearch.sleep(2)
        # 网点ID查询
        newsearch.areaid_search('22515')
        newsearch.search_button_click()
        newsearch.sleep(2)
        newsearch.clear_button_click()
        newsearch.sleep(2)
        # 网点名称查询
        newsearch.areaname_search('福州展示仓01')
        newsearch.search_button_click()
        newsearch.sleep(2)
        newsearch.clear_button_click()
        newsearch.sleep(2)
        # 合伙人查询
        newsearch.partnername_search('直营仓库')
        newsearch.search_button_click()
        newsearch.sleep(2)
        newsearch.clear_button_click()
        newsearch.sleep(2)
        # 发货时间查询
        newsearch.delivertime_search()
        newsearch.search_button_click()
        newsearch.sleep(2)
        newsearch.clear_button_click()
        newsearch.sleep(2)
        # 刷新页面
        newsearch.refresh()

    def test_g_contract_search(self):
        """
        合同预警查询
        :return:
        """
        homepage = AreadevicePage(self.driver)
        homepage.search_click_areadevice_contract()
        homepage.sleep(3)
        homepage.get_window_img()
        try:
            assert '合同预警' in homepage.find_tab_contract()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))

        newsearch = ContractSearch(self.driver)
        # 合伙人查询
        newsearch.partnername_search('直营仓库')
        newsearch.search_button_click()
        newsearch.sleep(2)
        newsearch.clear_button_click()
        newsearch.sleep(2)
        # 网点名称查询
        newsearch.areaname_search('福州展示仓01')
        newsearch.search_button_click()
        newsearch.sleep(2)
        newsearch.clear_button_click()
        newsearch.sleep(2)
        # 刷新页面
        newsearch.refresh()

    def test_h_place_search(self):
        """
        场地管理查询
        :return:
        """
        homepage = AreadevicePage(self.driver)
        homepage.search_click_areadevice_place()
        homepage.sleep(3)
        homepage.get_window_img()
        try:
            assert '场地管理' in homepage.find_tab_place()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))

        newsearch = PlaceSearch(self.driver)
        # 场地ID查询
        newsearch.placeid_search('22515')
        newsearch.search_button_click()
        newsearch.sleep(2)
        newsearch.clear_button_click()
        newsearch.sleep(2)
        # 场地名称查询
        newsearch.placename_search('福州展示仓01')
        newsearch.search_button_click()
        newsearch.sleep(2)
        newsearch.clear_button_click()
        newsearch.sleep(2)
        # 合伙人查询
        newsearch.partnername_search('直营仓库')
        newsearch.search_button_click()
        newsearch.sleep(2)
        newsearch.clear_button_click()
        newsearch.sleep(2)
        # 刷新页面
        newsearch.refresh()

    def test_i_company_search(self):
        """
        分公司管理查询
        :return:
        """
        homepage = AreadevicePage(self.driver)
        homepage.search_click_areadevice_company()
        homepage.sleep(3)
        homepage.get_window_img()
        try:
            assert '分公司管理' in homepage.find_tab_company()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))

        newsearch = CompanySearch(self.driver)
        # 分公司名称查询
        newsearch.companyname_search('上海分公司')
        newsearch.search_button_click()
        newsearch.sleep(2)
        newsearch.clear_button_click()
        newsearch.sleep(2)
        # 刷新页面
        newsearch.refresh()


if __name__ == '__main__':
    unittest.main()
