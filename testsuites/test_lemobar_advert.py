# coding = utf-8
import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.lemobar_login import HomePage
from pageobjects.lemobar_advert import AdvertPage
from pageobjects.lemobar_advert import AdvertSearch
from pageobjects.lemobar_advert import AdvertScheduleSearch
from pageobjects.lemobar_advert import BrandMapSearch
from pageobjects.lemobar_advert import CountDownSearch


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

        newsearch = AdvertSearch(self.driver)

        # 广告ID查询
        newsearch.advertid_search('1')
        newsearch.search_button_click()
        newsearch.sleep(2)
        try:
            assert '1' in newsearch.find_result_advertid()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))
        newsearch.empty_button_click()
        newsearch.sleep(2)

        # 广告标题查询
        newsearch.adverttitle_search('眼部按摩仪')
        newsearch.search_button_click()
        newsearch.sleep(2)
        try:
            assert '眼部按摩仪' in newsearch.find_result_adverttitle()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))
        newsearch.empty_button_click()
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
        newsearch.empty_button_click()
        newsearch.sleep(2)

        # 刷新页面
        homepage.refresh()

    def test_c_advertschedule_search(self):
        """
        广告排期查询
        :return:
        """
        homepage = AdvertPage(self.driver)
        homepage.search_click_advert_advertschedule()
        homepage.sleep(3)
        homepage.get_window_img()
        try:
            assert '广告排期' in homepage.find_tab_advertschedule()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))

        newsearch = AdvertScheduleSearch(self.driver)

        # 开始日期查询
        newsearch.begintime_search()
        newsearch.search_button_click()
        newsearch.sleep(2)
        try:
            assert '2020-07-01' in newsearch.find_result_begintime()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))
        newsearch.empty_button_click()
        newsearch.sleep(2)

        # 结束日期查询
        newsearch.endtime_search()
        newsearch.search_button_click()
        newsearch.sleep(2)
        try:
            assert '2020-07-31' in newsearch.find_result_endtime()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))
        newsearch.empty_button_click()
        newsearch.sleep(2)

        # 网点ID查询
        newsearch.areaid_search('22515')
        newsearch.search_button_click()
        newsearch.sleep(2)
        newsearch.empty_button_click()
        newsearch.sleep(2)

        # 网点名称查询
        newsearch.areaname_search('福州')
        newsearch.search_button_click()
        newsearch.sleep(2)
        newsearch.empty_button_click()
        newsearch.sleep(2)

        # 是否可用查询
        newsearch.isenable_search()
        newsearch.search_button_click()
        newsearch.sleep(2)
        try:
            assert 'el-icon-circle-check' in newsearch.find_result_isenable()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))
        newsearch.empty_button_click()
        newsearch.sleep(2)

        # 作用类型查询
        newsearch.effecttype_search()
        newsearch.search_button_click()
        newsearch.sleep(2)
        try:
            assert '支付页' in newsearch.find_result_effecttype()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))
        newsearch.empty_button_click()
        newsearch.sleep(2)

        # 作用渠道查询
        newsearch.effectchannel_search()
        newsearch.search_button_click()
        newsearch.sleep(2)
        try:
            assert '微信H5' in newsearch.find_result_effectchannel()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))
        newsearch.empty_button_click()
        newsearch.sleep(2)

        # 刷新页面
        homepage.refresh()

    def test_d_brandmap_search(self):
        """
        支付页背景图查询
        :return:
        """
        homepage = AdvertPage(self.driver)
        homepage.search_click_advert_brandmap()
        homepage.sleep(3)
        homepage.get_window_img()
        try:
            assert '支付页背景图' in homepage.find_tab_brandmap()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))

        newsearch = BrandMapSearch(self.driver)

        # 背景图ID查询
        newsearch.brandmapid_search('7')
        newsearch.search_button_click()
        newsearch.sleep(2)
        try:
            assert '7' in newsearch.find_result_brandmapid()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))
        newsearch.empty_button_click()
        newsearch.sleep(2)

        # 背景图标题查询
        newsearch.brandmaptitle_search('湖北')
        newsearch.search_button_click()
        newsearch.sleep(2)
        try:
            assert '湖北' in newsearch.find_result_brandmaptitle()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))
        newsearch.empty_button_click()
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
        newsearch.empty_button_click()
        newsearch.sleep(2)

        # 作用渠道查询
        newsearch.effectchannel_search()
        newsearch.search_button_click()
        newsearch.sleep(2)
        try:
            assert '微信H5' in newsearch.find_result_effectchannel()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))
        newsearch.empty_button_click()
        newsearch.sleep(2)

        # 刷新页面
        homepage.refresh()

    def test_e_countdown_search(self):
        """
        倒计时页弹窗查询
        :return:
        """
        homepage = AdvertPage(self.driver)
        homepage.search_click_advert_countdown()
        homepage.sleep(3)
        homepage.get_window_img()
        try:
            assert '支付页背景图' in homepage.find_tab_countdown()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))

        newsearch = CountDownSearch(self.driver)

        # 弹窗ID查询
        newsearch.popupid_search('120')
        newsearch.search_button_click()
        newsearch.sleep(2)
        try:
            assert '120' in newsearch.find_result_popupid()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))
        newsearch.empty_button_click()
        newsearch.sleep(2)

        # 弹窗名称查询
        newsearch.popupname_search('测试')
        newsearch.search_button_click()
        newsearch.sleep(2)
        try:
            assert '测试' in newsearch.find_result_popupname()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))
        newsearch.empty_button_click()
        newsearch.sleep(2)

        # 生效状态查询
        newsearch.effectivestatus_search()
        newsearch.search_button_click()
        newsearch.sleep(2)
        try:
            assert '生效中' in newsearch.find_result_effectivestatus()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))
        newsearch.empty_button_click()
        newsearch.sleep(2)

        # 作用渠道查询
        newsearch.effectchannel_search()
        newsearch.search_button_click()
        newsearch.sleep(2)
        try:
            assert '微信H5' or '不限' in newsearch.find_result_effectchannel()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))
        newsearch.empty_button_click()
        newsearch.sleep(2)

        # 弹窗类型查询
        newsearch.popuptype_search()
        newsearch.search_button_click()
        newsearch.sleep(2)
        try:
            assert '活动弹窗' in newsearch.find_result_popuptype()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))
        newsearch.empty_button_click()
        newsearch.sleep(2)

        # 刷新页面
        homepage.refresh()


if __name__ == '__main__':
    unittest.main()
