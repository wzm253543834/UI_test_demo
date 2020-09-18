# coding = utf-8
import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.lemobar_login import HomePage
from pageobjects.lemobar_finance import FinancePage
from pageobjects.lemobar_finance import SpendBillManageSearch
from pageobjects.lemobar_finance import OrderSearch
from pageobjects.lemobar_finance import BuyCardSearch
from pageobjects.lemobar_finance import SellingCouponsSearch
from pageobjects.lemobar_finance import CardOrderSearch
from pageobjects.lemobar_finance import RechargeSearch


class FinancePageSearch(unittest.TestCase):

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

    def test_b_spendbillmanage_search(self):
        """
        费用票据管理查询
        :return:
        """
        homepage = FinancePage(self.driver)
        homepage.search_click_finance()
        homepage.sleep(3)
        homepage.search_click_finance_spendbillmanage()
        homepage.sleep(3)
        homepage.get_window_img()
        try:
            assert '费用票据管理' in homepage.find_tab_spendbillmanage()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))

        newsearch = SpendBillManageSearch(self.driver)

        # 申请时间查询
        newsearch.applicationtime_search()
        newsearch.search_button_click()
        newsearch.sleep(2)
        try:
            assert '2020-07-20' in newsearch.find_result_applicationtime()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))
        newsearch.empty_button_click()
        newsearch.sleep(2)

        # 任务ID查询
        newsearch.applicationtime_search()
        newsearch.taskid_search('70245')
        newsearch.search_button_click()
        newsearch.sleep(2)
        try:
            assert '70245' in newsearch.find_result_taskid()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))
        newsearch.empty_button_click()
        newsearch.sleep(2)

        # 网点ID查询
        newsearch.applicationtime_search()
        newsearch.areaid_search('6179')
        newsearch.search_button_click()
        newsearch.sleep(2)
        try:
            assert '6179' in newsearch.find_result_areaid()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))
        newsearch.empty_button_click()
        newsearch.sleep(2)

        # 网点名称查询
        newsearch.applicationtime_search()
        newsearch.areaname_search('福州')
        newsearch.search_button_click()
        newsearch.sleep(2)
        try:
            assert '福州' in newsearch.find_result_areaname()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))
        newsearch.empty_button_click()
        newsearch.sleep(2)

        # 收款单位查询
        newsearch.applicationtime_search()
        newsearch.payee_search('福州')
        newsearch.search_button_click()
        newsearch.sleep(2)
        try:
            assert '福州' in newsearch.find_result_payee()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))
        newsearch.empty_button_click()
        newsearch.sleep(2)

        # 费用类别查询
        newsearch.applicationtime_search()
        newsearch.costtype_search()
        newsearch.search_button_click()
        newsearch.sleep(2)
        newsearch.empty_button_click()
        newsearch.sleep(2)

        # 票据登记状态查询
        newsearch.applicationtime_search()
        newsearch.billregistrationstatus_search()
        newsearch.search_button_click()
        newsearch.sleep(2)
        try:
            assert '待录入' in newsearch.find_result_billregistrationstatus()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))
        newsearch.empty_button_click()
        newsearch.sleep(2)

        # 发票号码查询
        newsearch.applicationtime_search()
        newsearch.invoicenumber_search('1222222')
        newsearch.search_button_click()
        newsearch.sleep(2)
        newsearch.empty_button_click()
        newsearch.sleep(2)

        # 刷新页面
        homepage.refresh()

    def test_c_order_search(self):
        """
        订单流水查询
        :return:
        """
        homepage = FinancePage(self.driver)
        homepage.search_click_finance_order()
        homepage.sleep(3)
        homepage.get_window_img()
        try:
            assert '订单流水' in homepage.find_tab_order()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))

        newsearch = OrderSearch(self.driver)

        # 创建时间查询
        newsearch.creationtime_search()
        newsearch.search_button_click()
        newsearch.sleep(2)
        try:
            assert '2020-08-30' in newsearch.find_result_creationtime()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))
        newsearch.empty_button_click()
        newsearch.sleep(2)

        # 付款方式查询
        newsearch.paymentmethod_search()
        newsearch.search_button_click()
        newsearch.sleep(2)
        try:
            assert '支付宝' in newsearch.find_result_paymentmethod()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))
        newsearch.empty_button_click()
        newsearch.sleep(2)

        # 订单号查询
        newsearch.ordernumber_search('JW020083010673685184602767365')
        newsearch.search_button_click()
        newsearch.sleep(2)
        try:
            assert 'JW020083010673685184602767365' in newsearch.find_result_ordernumber()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))
        newsearch.empty_button_click()
        newsearch.sleep(2)

        # 订单状态查询
        newsearch.orderstatus_search()
        newsearch.search_button_click()
        newsearch.sleep(2)
        try:
            assert '新订单' in newsearch.find_result_orderstatus()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))
        newsearch.empty_button_click()
        newsearch.sleep(2)

        # 交易单号查询
        newsearch.transactionnumber_search('4200000722202008303467942842')
        newsearch.search_button_click()
        newsearch.sleep(2)
        try:
            assert '4200000722202008303467942842' in newsearch.find_result_transactionnumber()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))
        newsearch.empty_button_click()
        newsearch.sleep(2)

        # 网点名称查询
        newsearch.areaname_search('福州')
        newsearch.search_button_click()
        newsearch.sleep(2)
        try:
            assert '福州' in newsearch.find_result_areaname()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))
        newsearch.empty_button_click()
        newsearch.sleep(2)

        # 设备ID查询
        newsearch.deviceid_search('101401025')
        newsearch.search_button_click()
        newsearch.sleep(2)
        try:
            assert '101401025' in newsearch.find_result_deviceid()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))
        newsearch.empty_button_click()
        newsearch.sleep(2)

        # 活动类型查询
        newsearch.activitytype_search()
        newsearch.search_button_click()
        newsearch.sleep(2)
        try:
            assert '未参与活动' in newsearch.find_result_activitytype()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))
        newsearch.empty_button_click()
        newsearch.sleep(2)

        # 省份查询
        newsearch.province_search()
        newsearch.search_button_click()
        newsearch.sleep(2)
        try:
            assert '北京市' in newsearch.find_result_province()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))
        newsearch.empty_button_click()
        newsearch.sleep(2)

        # 城市查询
        newsearch.city_search()
        newsearch.search_button_click()
        newsearch.sleep(2)
        try:
            assert '东城区' in newsearch.find_result_city()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))
        newsearch.empty_button_click()
        newsearch.sleep(2)

        # 网点提现查询
        newsearch.areawithdrawal_search()
        newsearch.search_button_click()
        newsearch.sleep(2)
        newsearch.empty_button_click()
        newsearch.sleep(2)

        # 刷新页面
        homepage.refresh()

    def test_d_buycard_search(self):
        """
        购卡流水查询
        :return:
        """
        homepage = FinancePage(self.driver)
        homepage.search_click_finance_buycard()
        homepage.sleep(3)
        homepage.get_window_img()
        try:
            assert '购卡流水' in homepage.find_tab_buycard()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))

        newsearch = BuyCardSearch(self.driver)

        # 创建时间查询
        newsearch.creationtime_search()
        newsearch.search_button_click()
        newsearch.sleep(2)
        try:
            assert '2020-08-30' in newsearch.find_result_creationtime()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))
        newsearch.empty_button_click()
        newsearch.sleep(2)

        # 订单状态查询
        newsearch.creationtime_search()
        newsearch.orderstatus_search()
        newsearch.search_button_click()
        newsearch.sleep(2)
        try:
            assert '未付款' in newsearch.find_result_orderstatus()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))
        newsearch.empty_button_click()
        newsearch.sleep(2)

        # 订单号查询
        newsearch.creationtime_search()
        newsearch.ordernumber_search('W002008251065475916450398208')
        newsearch.search_button_click()
        newsearch.sleep(2)
        try:
            assert 'W002008251065475916450398208' in newsearch.find_result_ordernumber()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))
        newsearch.empty_button_click()
        newsearch.sleep(2)

        # 卡状态查询
        newsearch.creationtime_search()
        newsearch.cardstatus_search()
        newsearch.search_button_click()
        newsearch.sleep(2)
        try:
            assert '未生效' in newsearch.find_result_cardstatus()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))
        newsearch.empty_button_click()
        newsearch.sleep(2)

        # 支付方式查询
        newsearch.creationtime_search()
        newsearch.paymethod_search()
        newsearch.search_button_click()
        newsearch.sleep(2)
        try:
            assert '支付宝' in newsearch.find_result_paymethod()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))
        newsearch.empty_button_click()
        newsearch.sleep(2)

        # 订单金额（元）查询
        newsearch.creationtime_search()
        newsearch.orderamountlow_search('10')
        newsearch.orderamounthigh_search('10')
        newsearch.search_button_click()
        newsearch.sleep(2)
        try:
            assert '10' in newsearch.find_result_orderamount()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))
        newsearch.empty_button_click()
        newsearch.sleep(2)

        # 交易单号查询
        newsearch.creationtime_search()
        newsearch.transactionnumber_search('4200000712202008245469688745')
        newsearch.search_button_click()
        newsearch.sleep(2)
        try:
            assert '4200000712202008245469688745' in newsearch.find_result_transactionnumber()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))
        newsearch.empty_button_click()
        newsearch.sleep(2)

        # 卡类型查询
        newsearch.creationtime_search()
        newsearch.cardtype_search()
        newsearch.search_button_click()
        newsearch.sleep(2)
        try:
            assert '次卡' in newsearch.find_result_cardtype()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))
        newsearch.empty_button_click()
        newsearch.sleep(2)

        # 区域限制类型查询
        newsearch.creationtime_search()
        newsearch.arearestrictiontype_search()
        newsearch.search_button_click()
        newsearch.sleep(2)
        try:
            assert '网点' in newsearch.find_result_arearestrictiontype()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))
        newsearch.empty_button_click()
        newsearch.sleep(2)

        # 物流状态查询
        newsearch.creationtime_search()
        newsearch.logisticsstatus_search()
        newsearch.search_button_click()
        newsearch.sleep(2)
        newsearch.empty_button_click()
        newsearch.sleep(2)

        # 刷新页面
        homepage.refresh()

    def test_e_sellingcoupons_search(self):
        """
        卖券流水查询
        :return:
        """
        homepage = FinancePage(self.driver)
        homepage.search_click_finance_sellingcoupons()
        homepage.sleep(3)
        homepage.get_window_img()
        try:
            assert '卖券流水' in homepage.find_tab_sellingcoupons()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))

        newsearch = SellingCouponsSearch(self.driver)

        # 创建时间查询
        newsearch.creationtime_search()
        newsearch.search_button_click()
        newsearch.sleep(2)
        try:
            assert '2020-08-30' in newsearch.find_result_creationtime()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))
        newsearch.empty_button_click()
        newsearch.sleep(2)

        # 订单状态查询
        newsearch.orderstatus_search()
        newsearch.search_button_click()
        newsearch.sleep(2)
        try:
            assert '新订单' in newsearch.find_result_orderstatus()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))
        newsearch.empty_button_click()
        newsearch.sleep(2)

        # 支付方式查询
        newsearch.paymethod_search()
        newsearch.search_button_click()
        newsearch.sleep(2)
        try:
            assert '微信支付' in newsearch.find_result_paymethod()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))
        newsearch.empty_button_click()
        newsearch.sleep(2)

        # 合伙人查询
        newsearch.partnername_search('福州')
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

        # 推广渠道查询
        newsearch.promotionchannels_search()
        newsearch.search_button_click()
        newsearch.sleep(2)
        try:
            assert '乐摩吧' in newsearch.find_result_promotionchannels()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))
        newsearch.empty_button_click()
        newsearch.sleep(2)

        # 订单号查询
        newsearch.ordernumber_search('W002008301067218951718731776')
        newsearch.search_button_click()
        newsearch.sleep(2)
        try:
            assert 'W002008301067218951718731776' in newsearch.find_result_ordernumber()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))
        newsearch.empty_button_click()
        newsearch.sleep(2)

        # 省份查询
        newsearch.province_search()
        newsearch.search_button_click()
        newsearch.sleep(2)
        newsearch.empty_button_click()
        newsearch.sleep(2)

        # 城市查询
        newsearch.city_search()
        newsearch.search_button_click()
        newsearch.sleep(2)
        newsearch.empty_button_click()
        newsearch.sleep(2)

        # 刷新页面
        homepage.refresh()

    def test_f_cardorder_search(self):
        """
        卡订单结算查询
        :return:
        """
        homepage = FinancePage(self.driver)
        homepage.search_click_finance_cardorder()
        homepage.sleep(3)
        homepage.get_window_img()
        try:
            assert '卡订单结算' in homepage.find_tab_cardorder()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))

        newsearch = CardOrderSearch(self.driver)

        # 核账月份查询
        newsearch.accountcheckingmonth_search()
        newsearch.search_button_click()
        newsearch.sleep(2)
        newsearch.empty_button_click()
        newsearch.sleep(2)

        # 按摩时间查询
        newsearch.massagetime_search()
        newsearch.search_button_click()
        newsearch.sleep(2)
        try:
            assert '2020-08-30' in newsearch.find_result_massagetime()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))
        newsearch.empty_button_click()
        newsearch.sleep(2)

        # 购卡时间查询
        newsearch.buycardtime_search()
        newsearch.search_button_click()
        newsearch.sleep(2)
        try:
            assert '2020-08-30' in newsearch.find_result_buycardtime()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))
        newsearch.empty_button_click()
        newsearch.sleep(2)

        # 按摩订单号查询
        newsearch.massageordernumber_search('KC020071010488384637278126087')
        newsearch.search_button_click()
        newsearch.sleep(2)
        try:
            assert 'KC020071010488384637278126087' in newsearch.find_result_massageordernumber()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))
        newsearch.empty_button_click()
        newsearch.sleep(2)

        # 购卡订单号查询
        newsearch.buycardordernumber_search('W002006281044488609958363136')
        newsearch.search_button_click()
        newsearch.sleep(2)
        try:
            assert 'W002006281044488609958363136' in newsearch.find_result_buycardordernumber()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))
        newsearch.empty_button_click()
        newsearch.sleep(2)

        # 卡类型查询
        newsearch.cardtype_search()
        newsearch.search_button_click()
        newsearch.sleep(2)
        try:
            assert '次卡' in newsearch.find_result_cardtype()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))
        newsearch.empty_button_click()
        newsearch.sleep(2)

        # 合伙人查询
        newsearch.partnername_search('福州')
        newsearch.search_button_click()
        newsearch.sleep(2)
        try:
            assert '福州' in newsearch.find_result_partnername()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))
        newsearch.empty_button_click()
        newsearch.sleep(2)

        # 刷新页面
        homepage.refresh()

    def test_g_recharge_search(self):
        """
        充值订单查询
        :return:
        """
        homepage = FinancePage(self.driver)
        homepage.search_click_finance_recharge()
        homepage.sleep(3)
        homepage.get_window_img()
        try:
            assert '充值订单' in homepage.find_tab_recharge()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))

        newsearch = RechargeSearch(self.driver)

        # 创建时间查询
        newsearch.creationtime_search()
        newsearch.search_button_click()
        newsearch.sleep(2)
        try:
            assert '2020-08-30' in newsearch.find_result_creationtime()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))
        newsearch.empty_button_click()
        newsearch.sleep(2)

        # 订单状态查询
        newsearch.orderstatus_search()
        newsearch.search_button_click()
        newsearch.sleep(2)
        try:
            assert '未付款' in newsearch.find_result_orderstatus()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))
        newsearch.empty_button_click()
        newsearch.sleep(2)

        # 订单号查询
        newsearch.ordernumber_search('W002007261595777397123')
        newsearch.search_button_click()
        newsearch.sleep(2)
        try:
            assert 'W002007261595777397123' in newsearch.find_result_ordernumber()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))
        newsearch.empty_button_click()
        newsearch.sleep(2)

        # 交易单号查询
        newsearch.transactionnumber_search('4200000714202007267732703998')
        newsearch.search_button_click()
        newsearch.sleep(2)
        try:
            assert '4200000714202007267732703998' in newsearch.find_result_transactionnumber()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))
        newsearch.empty_button_click()
        newsearch.sleep(2)

        # 付款账号查询
        newsearch.paymentaccountnumber_search('oSgG-wcfLq1pk9bwLDfCIDV1VL_o')
        newsearch.search_button_click()
        newsearch.sleep(2)
        try:
            assert 'oSgG-wcfLq1pk9bwLDfCIDV1VL_o' in newsearch.find_result_paymentaccountnumber()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))
        newsearch.empty_button_click()
        newsearch.sleep(2)

        # 订单金额（元）查询
        newsearch.orderamountlow_search('10')
        newsearch.orderamounthigh_search('10')
        newsearch.search_button_click()
        newsearch.sleep(2)
        try:
            assert '10' in newsearch.find_result_orderamount()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))
        newsearch.empty_button_click()
        newsearch.sleep(2)

        # 渠道来源查询
        newsearch.channelsource_search()
        newsearch.search_button_click()
        newsearch.sleep(2)
        try:
            assert 'H5支付页' in newsearch.find_result_channelsource()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))
        newsearch.empty_button_click()
        newsearch.sleep(2)

        # 查询条件查询
        newsearch.querycriteria_search()
        newsearch.search_button_click()
        newsearch.sleep(2)
        newsearch.empty_button_click()
        newsearch.sleep(2)

        # 刷新页面
        homepage.refresh()


if __name__ == '__main__':
    unittest.main()
