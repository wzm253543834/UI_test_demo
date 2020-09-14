# coding = utf-8
import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.lemobar_login import HomePage
from pageobjects.lemobar_activity import ActivityPage
from pageobjects.lemobar_activity import VoucherSearch
from pageobjects.lemobar_activity import CouponSearch
from pageobjects.lemobar_activity import DiscountSearch
from pageobjects.lemobar_activity import FreeDiscountSearch
from pageobjects.lemobar_activity import DirectRedEnvelopesSearch
from pageobjects.lemobar_activity import RetentionSearch
from pageobjects.lemobar_activity import CardActivitySearch
from pageobjects.lemobar_activity import OvertimeCouponSearch
from pageobjects.lemobar_activity import SubscriptionActivitySearch
from pageobjects.lemobar_activity import SellCouponSearch


class ActivityPageSearch(unittest.TestCase):

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

    def test_b_voucher_search(self):
        """
        现金券管理查询
        :return:
        """
        homepage = ActivityPage(self.driver)
        homepage.search_click_activity()
        homepage.sleep(3)
        homepage.search_click_activity_voucher()
        homepage.sleep(3)
        homepage.get_window_img()
        try:
            assert '现金券管理' in homepage.find_tab_voucher()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))

        newsearch = VoucherSearch(self.driver)

        # 活动ID查询
        newsearch.activityid_search('36680')
        newsearch.search_button_click()
        newsearch.sleep(2)
        try:
            assert '36680' in newsearch.find_result_activityid()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))
        newsearch.empty_button_click()
        newsearch.sleep(2)

        # 活动标题查询
        newsearch.activitytitle_search('测试合同非自营大场景2测试券')
        newsearch.search_button_click()
        newsearch.sleep(2)
        try:
            assert '测试合同非自营大场景2测试券' in newsearch.find_result_activitytitle()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))
        newsearch.empty_button_click()
        newsearch.sleep(2)

        # 活动状态查询
        newsearch.activitystatus_search()
        newsearch.search_button_click()
        newsearch.sleep(2)
        try:
            assert '未生效' in newsearch.find_result_activitystatus()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))
        newsearch.empty_button_click()
        newsearch.sleep(2)

        # 发放方式查询
        newsearch.distributionmethod_search()
        newsearch.search_button_click()
        newsearch.sleep(2)
        try:
            assert '用户领取' in newsearch.find_result_distributionmethod()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))
        newsearch.empty_button_click()
        newsearch.sleep(2)

        # 区域限制类型查询
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

        # 现金券类型查询
        newsearch.vouchertype_search()
        newsearch.search_button_click()
        newsearch.sleep(2)
        try:
            assert '普通现金券' in newsearch.find_result_vouchertype()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))
        newsearch.empty_button_click()
        newsearch.sleep(2)

        # 现金券码查询
        newsearch.vouchercode_search('294650991021')
        newsearch.search_button_click()
        newsearch.sleep(2)
        newsearch.empty_button_click()
        newsearch.sleep(2)

        # 刷新页面
        homepage.refresh()

    def test_c_coupon_search(self):
        """
        优惠券管理查询
        :return:
        """
        homepage = ActivityPage(self.driver)
        homepage.search_click_activity_coupon()
        homepage.sleep(3)
        homepage.get_window_img()
        try:
            assert '优惠券管理' in homepage.find_tab_coupon()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))

        newsearch = CouponSearch(self.driver)

        # 活动ID查询
        newsearch.activityid_search('1257')
        newsearch.search_button_click()
        newsearch.sleep(2)
        newsearch.empty_button_click()
        newsearch.sleep(2)

        # 活动标题查询
        newsearch.activitytitle_search('测试')
        newsearch.search_button_click()
        newsearch.sleep(2)
        try:
            assert '测试' in newsearch.find_result_activitytitle()
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
            assert '现金红包' in newsearch.find_result_activitytype()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))
        newsearch.empty_button_click()
        newsearch.sleep(2)

        # 活动启用状态查询
        newsearch.activityenablestatus_search()
        newsearch.search_button_click()
        newsearch.sleep(2)
        try:
            assert 'el-icon-circle-check' in newsearch.find_result_activityenablestatus()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))
        newsearch.empty_button_click()
        newsearch.sleep(2)

        # 刷新页面
        homepage.refresh()

    def test_d_discount_search(self):
        """
        第二单折扣查询
        :return:
        """
        homepage = ActivityPage(self.driver)
        homepage.search_click_activity_discount()
        homepage.sleep(3)
        homepage.get_window_img()
        try:
            assert '第二单折扣' in homepage.find_tab_discount()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))

        newsearch = DiscountSearch(self.driver)

        # 折扣标题查询
        newsearch.discounttitle_search('测试')
        newsearch.search_button_click()
        newsearch.sleep(2)
        try:
            assert '测试' in newsearch.find_result_discounttitle()
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

    def test_e_freediscount_search(self):
        """
        闲时优惠查询
        :return:
        """
        homepage = ActivityPage(self.driver)
        homepage.search_click_activity_freediscount()
        homepage.sleep(3)
        homepage.get_window_img()
        try:
            assert '闲时优惠' in homepage.find_tab_freediscount()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))

        newsearch = FreeDiscountSearch(self.driver)

        # 闲时活动标题查询
        newsearch.freeactivitytitle_search('测试')
        newsearch.search_button_click()
        newsearch.sleep(2)
        try:
            assert '测试' in newsearch.find_result_freeactivitytitle()
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

    def test_f_directredenvelopes_search(self):
        """
        直通红包查询
        :return:
        """
        homepage = ActivityPage(self.driver)
        homepage.search_click_activity_directredenvelopes()
        homepage.sleep(3)
        homepage.get_window_img()
        try:
            assert '直通红包' in homepage.find_tab_directredenvelopes()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))

        newsearch = DirectRedEnvelopesSearch(self.driver)

        # 活动ID查询
        newsearch.activityid_search('1312')
        newsearch.search_button_click()
        newsearch.sleep(2)
        try:
            assert '1312' in newsearch.find_result_activityid()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))
        newsearch.empty_button_click()
        newsearch.sleep(2)

        # 活动标题查询
        newsearch.activitytitle_search('测试')
        newsearch.search_button_click()
        newsearch.sleep(2)
        try:
            assert '测试' in newsearch.find_result_activitytitle()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))
        newsearch.empty_button_click()
        newsearch.sleep(2)

        # 优惠券类型查询
        newsearch.coupontype_search()
        newsearch.search_button_click()
        newsearch.sleep(2)
        try:
            assert '满减券' in newsearch.find_result_coupontype()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))
        newsearch.empty_button_click()
        newsearch.sleep(2)

        # 活动启用状态查询
        newsearch.activityenablestatus_search()
        newsearch.search_button_click()
        newsearch.sleep(2)
        try:
            assert 'el-icon-circle-check' in newsearch.find_result_activityenablestatus()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))
        newsearch.empty_button_click()
        newsearch.sleep(2)

        # 刷新页面
        homepage.refresh()

    def test_g_retention_search(self):
        """
        挽留机制查询
        :return:
        """
        homepage = ActivityPage(self.driver)
        homepage.search_click_activity_retention()
        homepage.sleep(3)
        homepage.get_window_img()
        try:
            assert '挽留机制' in homepage.find_tab_retention()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))

        newsearch = RetentionSearch(self.driver)

        # 标题查询
        newsearch.title_search('测试')
        newsearch.search_button_click()
        newsearch.sleep(2)
        try:
            assert '测试' in newsearch.find_result_title()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))
        newsearch.empty_button_click()
        newsearch.sleep(2)

        # 启用状态查询
        newsearch.enablestatus_search()
        newsearch.search_button_click()
        newsearch.sleep(2)
        try:
            assert 'el-icon-circle-check' in newsearch.find_result_enablestatus()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))
        newsearch.empty_button_click()
        newsearch.sleep(2)

        # 刷新页面
        homepage.refresh()

    def test_h_cardactivity_search(self):
        """
        卡券活动查询
        :return:
        """
        homepage = ActivityPage(self.driver)
        homepage.search_click_activity_cardactivity()
        homepage.sleep(3)
        homepage.get_window_img()
        try:
            assert '卡券活动' in homepage.find_tab_cardactivity()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))

        newsearch = CardActivitySearch(self.driver)

        # 标题查询
        newsearch.title_search('测试')
        newsearch.search_button_click()
        newsearch.sleep(2)
        try:
            assert '测试' in newsearch.find_result_title()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))
        newsearch.empty_button_click()
        newsearch.sleep(2)

        # 区域限制类型查询
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

        # 启用状态查询
        newsearch.enablestatus_search()
        newsearch.search_button_click()
        newsearch.sleep(2)
        try:
            assert 'el-icon-circle-check' in newsearch.find_result_enablestatus()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))
        newsearch.empty_button_click()
        newsearch.sleep(2)

        # 刷新页面
        homepage.refresh()

    def test_i_overtimecoupon_search(self):
        """
        加时券管理查询
        :return:
        """
        homepage = ActivityPage(self.driver)
        homepage.search_click_activity_overtimecoupon()
        homepage.sleep(3)
        homepage.get_window_img()
        try:
            assert '加时券管理' in homepage.find_tab_overtimecoupon()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))

        newsearch = OvertimeCouponSearch(self.driver)

        # 活动ID查询
        newsearch.activityid_search('42')
        newsearch.search_button_click()
        newsearch.sleep(2)
        try:
            assert '42' in newsearch.find_result_activityid()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))
        newsearch.empty_button_click()
        newsearch.sleep(2)

        # 活动标题查询
        newsearch.activitytitle_search('测试')
        newsearch.search_button_click()
        newsearch.sleep(2)
        try:
            assert '测试' in newsearch.find_result_activitytitle()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))
        newsearch.empty_button_click()
        newsearch.sleep(2)

        # 活动启用状态查询
        newsearch.activityenablestatus_search()
        newsearch.search_button_click()
        newsearch.sleep(2)
        try:
            assert 'el-icon-circle-check' in newsearch.find_result_activityenablestatus()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))
        newsearch.empty_button_click()
        newsearch.sleep(2)

        # 刷新页面
        homepage.refresh()

    def test_j_subscriptionactivity_search(self):
        """
        订阅活动管理查询
        :return:
        """
        homepage = ActivityPage(self.driver)
        homepage.search_click_activity_subscriptionactivity()
        homepage.sleep(3)
        homepage.get_window_img()
        try:
            assert '订阅活动管理' in homepage.find_tab_subscriptionactivity()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))

        newsearch = SubscriptionActivitySearch(self.driver)

        # 活动ID查询
        newsearch.activityid_search('4')
        newsearch.search_button_click()
        newsearch.sleep(2)
        try:
            assert '4' in newsearch.find_result_activityid()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))
        newsearch.empty_button_click()
        newsearch.sleep(2)

        # 活动标题查询
        newsearch.activitytitle_search('测试')
        newsearch.search_button_click()
        newsearch.sleep(2)
        try:
            assert '测试' in newsearch.find_result_activitytitle()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))
        newsearch.empty_button_click()
        newsearch.sleep(2)

        # 活动启用状态查询
        newsearch.activityenablestatus_search()
        newsearch.search_button_click()
        newsearch.sleep(2)
        try:
            assert 'el-icon-circle-check' in newsearch.find_result_activityenablestatus()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))
        newsearch.empty_button_click()
        newsearch.sleep(2)

        # 刷新页面
        homepage.refresh()

    def test_k_sellcoupon_search(self):
        """
        卖券活动查询
        :return:
        """
        homepage = ActivityPage(self.driver)
        homepage.search_click_activity_sellcoupon()
        homepage.sleep(3)
        homepage.get_window_img()
        try:
            assert '卖券活动' in homepage.find_tab_sellcoupon()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))

        newsearch = SellCouponSearch(self.driver)

        # 活动ID查询
        newsearch.activityid_search('34')
        newsearch.search_button_click()
        newsearch.sleep(2)
        try:
            assert '34' in newsearch.find_result_activityid()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))
        newsearch.empty_button_click()
        newsearch.sleep(2)

        # 活动标题查询
        newsearch.activitytitle_search('测试')
        newsearch.search_button_click()
        newsearch.sleep(2)
        try:
            assert '测试' in newsearch.find_result_activitytitle()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))
        newsearch.empty_button_click()
        newsearch.sleep(2)

        # 活动启用状态查询
        newsearch.activityenablestatus_search()
        newsearch.search_button_click()
        newsearch.sleep(2)
        try:
            assert 'el-icon-circle-check' in newsearch.find_result_activityenablestatus()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))
        newsearch.empty_button_click()
        newsearch.sleep(2)

        # 刷新页面
        homepage.refresh()


if __name__ == '__main__':
    unittest.main()
