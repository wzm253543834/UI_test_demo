# coding = utf-8
from framework.base_page import BasePage


class ActivityPage(BasePage):

    menu_activity = "xpath=>//*[@id='app']/div/div/div[2]/aside/ul/li[5]/div"
    menu_activity_voucher = "xpath=>//*[@id='app']/div/div/div[2]/aside/ul/li[5]/ul/li[1]"
    menu_activity_coupon = "xpath=>//*[@id='app']/div/div/div[2]/aside/ul/li[5]/ul/li[2]"
    menu_activity_discount = "xpath=>//*[@id='app']/div/div/div[2]/aside/ul/li[5]/ul/li[3]"
    menu_activity_freediscount = "xpath=>//*[@id='app']/div/div/div[2]/aside/ul/li[5]/ul/li[4]"
    menu_activity_directRedEnvelopes = "xpath=>//*[@id='app']/div/div/div[2]/aside/ul/li[5]/ul/li[5]"
    menu_activity_retention = "xpath=>//*[@id='app']/div/div/div[2]/aside/ul/li[5]/ul/li[6]"
    menu_activity_cardActivity = "xpath=>//*[@id='app']/div/div/div[2]/aside/ul/li[5]/ul/li[7]"
    menu_activity_overtimeCoupon = "xpath=>//*[@id='app']/div/div/div[2]/aside/ul/li[5]/ul/li[8]"
    menu_activity_subscriptionActivity = "xpath=>//*[@id='app']/div/div/div[2]/aside/ul/li[5]/ul/li[9]"
    menu_activity_sellCoupon = "xpath=>//*[@id='app']/div/div/div[2]/aside/ul/li[5]/ul/li[10]"
    tab_voucher = "xpath=>//*[@id='tab-42']"
    tab_coupon = "xpath=>//*[@id='tab-43']"
    tab_discount = "xpath=>//*[@id='tab-107']"
    tab_freediscount = "xpath=>//*[@id='tab-108']"
    tab_directRedEnvelopes = "xpath=>//*[@id='tab-117']"
    tab_retention = "xpath=>//*[@id='tab-144']"
    tab_cardActivity = "xpath=>//*[@id='tab-150']"
    tab_overtimeCoupon = "xpath=>//*[@id='tab-153']"
    tab_subscriptionActivity = "xpath=>//*[@id='tab-157']"
    tab_sellCoupon = "xpath=>//*[@id='tab-161']"

    """
    活动管理各菜单地址及tab页地址
    """

    # 点击活动管理
    def search_click_activity(self):
        self.click(self.menu_activity)

    # 点击现金券管理
    def search_click_activity_voucher(self):
        self.click(self.menu_activity_voucher)

    # 获取现金券管理tab名
    def find_tab_voucher(self):
        a = self.get_tab_title(self.tab_voucher)
        return a

    # 点击优惠券管理
    def search_click_activity_coupon(self):
        self.click(self.menu_activity_coupon)

    # 获取优惠券管理tab名
    def find_tab_coupon(self):
        a = self.get_tab_title(self.tab_coupon)
        return a

    # 点击第二单折扣
    def search_click_activity_discount(self):
        self.click(self.menu_activity_discount)

    # 获取第二单折扣tab名
    def find_tab_discount(self):
        a = self.get_tab_title(self.tab_discount)
        return a

    # 点击闲时优惠
    def search_click_activity_freediscount(self):
        self.click(self.menu_activity_freediscount)

    # 获取闲时优惠tab名
    def find_tab_freediscount(self):
        a = self.get_tab_title(self.tab_freediscount)
        return a

    # 点击直通红包
    def search_click_activity_directredenvelopes(self):
        self.click(self.menu_activity_directRedEnvelopes)

    # 获取直通红包tab名
    def find_tab_directredenvelopes(self):
        a = self.get_tab_title(self.tab_directRedEnvelopes)
        return a

    # 点击挽留机制
    def search_click_activity_retention(self):
        self.click(self.menu_activity_retention)

    # 获取挽留机制tab名
    def find_tab_retention(self):
        a = self.get_tab_title(self.tab_retention)
        return a

    # 点击卡券活动
    def search_click_activity_cardactivity(self):
        self.click(self.menu_activity_cardActivity)

    # 获取卡券活动tab名
    def find_tab_cardactivity(self):
        a = self.get_tab_title(self.tab_cardActivity)
        return a

    # 点击加时券管理
    def search_click_activity_overtimecoupon(self):
        self.click(self.menu_activity_overtimeCoupon)

    # 获取加时券管理tab名
    def find_tab_overtimecoupon(self):
        a = self.get_tab_title(self.tab_overtimeCoupon)
        return a

    # 点击订阅活动管理
    def search_click_activity_subscriptionactivity(self):
        self.click(self.menu_activity_subscriptionActivity)

    # 获取订阅活动管理tab名
    def find_tab_subscriptionactivity(self):
        a = self.get_tab_title(self.tab_subscriptionActivity)
        return a

    # 点击卖券活动
    def search_click_activity_sellcoupon(self):
        self.click(self.menu_activity_sellCoupon)

    # 获取卖券活动tab名
    def find_tab_sellcoupon(self):
        a = self.get_tab_title(self.tab_sellCoupon)
        return a


class VoucherSearch(BasePage):

    voucher_activityid_search = "xpath=>//*[@id='search_list']/div[1]/div/div/input"
    voucher_activitytitle_search = "xpath=>//*[@id='search_list']/div[2]/div/div/input"
    voucher_activitystatus_search = "xpath=>//*[@id='search_list']/div[3]/div/div/div/input"
    voucher_distributionmethod_search = "xpath=>//*[@id='search_list']/div[4]/div/div/div/input"
    voucher_arearestrictiontype_search = "xpath=>//*[@id='search_list']/div[5]/div/div/div/input"
    voucher_vouchertype_search = "xpath=>//*[@id='search_list']/div[7]/div/div/div/input"
    voucher_vouchercode_search = "xpath=>//*[@id='search_list']/div[8]/div/div/input"
    voucher_search_button = "xpath=>//*[@id='search_list']/div[6]/div/button"
    voucher_empty_button = "xpath=>//*[@id='search_list']/div[9]/div/button"
    voucher_activitystatus = "xpath=>/html/body/div[2]/div[1]/div[1]/ul/li[1]"
    voucher_distributionmethod = "xpath=>/html/body/div[3]/div[1]/div[1]/ul/li[1]"
    voucher_arearestrictiontype = "xpath=>/html/body/div[4]/div[1]/div[1]/ul/li[1]"
    voucher_vouchertype = "xpath=>/html/body/div[5]/div[1]/div[1]/ul/li[1]"

    """
    现金券管理各筛选项
    """

    # 活动ID查询
    def activityid_search(self, text):
        self.type(self.voucher_activityid_search, text)

    # 活动标题查询
    def activitytitle_search(self, text):
        self.type(self.voucher_activitytitle_search, text)

    # 活动状态查询
    def activitystatus_search(self):
        self.click(self.voucher_activitystatus_search)
        self.sleep(2)
        self.click(self.voucher_activitystatus)

    # 发放方式查询
    def distributionmethod_search(self):
        self.click(self.voucher_distributionmethod_search)
        self.sleep(2)
        self.click(self.voucher_distributionmethod)

    # 区域限制类型查询
    def arearestrictiontype_search(self):
        self.click(self.voucher_arearestrictiontype_search)
        self.sleep(2)
        self.click(self.voucher_arearestrictiontype)

    # 现金券类型查询
    def vouchertype_search(self):
        self.click(self.voucher_vouchertype_search)
        self.sleep(2)
        self.click(self.voucher_vouchertype)

    # 现金券码查询
    def vouchercode_search(self, text):
        self.type(self.voucher_vouchercode_search, text)

    # 查询按钮
    def search_button_click(self):
        self.click(self.voucher_search_button)

    # 清空按钮
    def empty_button_click(self):
        self.click(self.voucher_empty_button)

    # 测试结果断言
    result_activityid = "xpath=>//*[@id='app']/div/div/div[2]/div/div[2]/section/div[1]/div[3]/table/tbody/tr/td[2]/div"
    result_activitytitle = "xpath=>//*[@id='app']/div/div/div[2]/div/div[2]/section/div[1]/div[3]/table/tbody/tr/td[3]/div"
    result_activitystatus = "xpath=>//*[@id='app']/div/div/div[2]/div/div[2]/section/div[1]/div[3]/table/tbody/tr/td[9]/div"
    result_distributionmethod = "xpath=>//*[@id='app']/div/div/div[2]/div/div[2]/section/div[1]/div[3]/table/tbody/tr/td[7]/div"
    result_arearestrictiontype = "xpath=>//*[@id='app']/div/div/div[2]/div/div[2]/section/div[1]/div[3]/table/tbody/tr/td[8]/div"
    result_vouchertype = "xpath=>//*[@id='app']/div/div/div[2]/div/div[2]/section/div[1]/div[3]/table/tbody/tr/td[4]/div"
    # result_vouchercode = "xpath=>"

    # 断言活动ID查询结果
    def find_result_activityid(self):
        a = self.get_search_result(self.result_activityid)
        return a

    # 断言活动标题查询结果
    def find_result_activitytitle(self):
        a = self.get_search_result(self.result_activitytitle)
        return a

    # 断言活动状态查询结果
    def find_result_activitystatus(self):
        a = self.get_search_result(self.result_activitystatus)
        return a

    # 断言发放方式查询结果
    def find_result_distributionmethod(self):
        a = self.get_search_result(self.result_distributionmethod)
        return a

    # 断言区域限制类型查询结果
    def find_result_arearestrictiontype(self):
        a = self.get_search_result(self.result_arearestrictiontype)
        return a

    # 断言现金券类型查询结果
    def find_result_vouchertype(self):
        a = self.get_search_result(self.result_vouchertype)
        return a


class CouponSearch(BasePage):

    coupon_activityid_search = "xpath=>//*[@id='search_list']/div[1]/div/div/input"
    coupon_activitytitle_search = "xpath=>//*[@id='search_list']/div[2]/div/div/input"
    coupon_activitytype_search = "xpath=>//*[@id='search_list']/div[3]/div/div/div/input"
    coupon_activityenablestatus_search = "xpath=>//*[@id='search_list']/div[4]/div/div/div/input"
    coupon_search_button = "xpath=>//*[@id='search_list']/div[5]/div/button[1]"
    coupon_empty_button = "xpath=>//*[@id='search_list']/div[5]/div/button[2]"
    coupon_activitytype = "xpath=>/html/body/div[2]/div[1]/div[1]/ul/li[1]"
    coupon_activityenablestatus = "xpath=>/html/body/div[3]/div[1]/div[1]/ul/li[1]"

    """
    优惠券管理各筛选项
    """

    # 活动ID查询
    def activityid_search(self, text):
        self.type(self.coupon_activityid_search, text)

    # 活动标题查询
    def activitytitle_search(self, text):
        self.type(self.coupon_activitytitle_search, text)

    # 活动类型查询
    def activitytype_search(self):
        self.click(self.coupon_activitytype_search)
        self.sleep(2)
        self.click(self.coupon_activitytype)

    # 活动启用状态查询
    def activityenablestatus_search(self):
        self.click(self.coupon_activityenablestatus_search)
        self.sleep(2)
        self.click(self.coupon_activityenablestatus)

    # 查询按钮
    def search_button_click(self):
        self.click(self.coupon_search_button)

    # 清空按钮
    def empty_button_click(self):
        self.click(self.coupon_empty_button)

    # 测试结果断言
    # result_activityid = "xpath=>"
    result_activitytitle = "xpath=>//*[@id='app']/div/div/div[2]/div/div[2]/section/div[1]/div[3]/table/tbody/tr/td[3]/div"
    result_activitytype = "xpath=>//*[@id='app']/div/div/div[2]/div/div[2]/section/div[1]/div[3]/table/tbody/tr/td[2]/div"
    result_activityenablestatus = "xpath=>//*[@id='app']/div/div/div[2]/div/div[2]/section/div[1]/div[3]/table/tbody/tr/td[11]/div/i"

    # 断言活动标题查询结果
    def find_result_activitytitle(self):
        a = self.get_search_result(self.result_activitytitle)
        return a

    # 断言活动类型查询结果
    def find_result_activitytype(self):
        a = self.get_search_result(self.result_activitytype)
        return a

    # 断言活动启用状态查询结果
    def find_result_activityenablestatus(self):
        a = self.get_search_result_icon(self.result_activityenablestatus)
        return a


class DiscountSearch(BasePage):

    discount_discounttitle_search = "xpath=>//*[@id='search_list']/div[1]/div/div/input"
    discount_isenable_search = "xpath=>//*[@id='search_list']/div[2]/div/div/div/input"
    discount_search_button = "xpath=>//*[@id='search_list']/div[3]/div/button[1]"
    discount_empty_button = "xpath=>//*[@id='search_list']/div[3]/div/button[2]"
    discount_isenable =  "xpath=>/html/body/div[2]/div[1]/div[1]/ul/li[1]"

    """
    第二单折扣各筛选项
    """

    # 折扣标题查询
    def discounttitle_search(self, text):
        self.type(self.discount_discounttitle_search, text)

    # 是否启用查询
    def isenable_search(self):
        self.click(self.discount_isenable_search)
        self.sleep(2)
        self.click(self.discount_isenable)

    # 查询按钮
    def search_button_click(self):
        self.click(self.discount_search_button)

    # 清空按钮
    def empty_button_click(self):
        self.click(self.discount_empty_button)

    # 测试结果断言
    result_discounttitle = "xpath=>//*[@id='app']/div/div/div[2]/div/div[2]/section/div[1]/div[3]/table/tbody/tr/td[2]/div"
    result_isenable = "xpath=>//*[@id='app']/div/div/div[2]/div/div[2]/section/div[1]/div[3]/table/tbody/tr/td[11]/div/i"

    # 断言折扣标题查询结果
    def find_result_discounttitle(self):
        a = self.get_search_result(self.result_discounttitle)
        return a

    # 断言是否启用查询结果
    def find_result_isenable(self):
        a = self.get_search_result_icon(self.result_isenable)
        return a


class FreeDiscountSearch(BasePage):

    freediscount_freeactivitytitle_search = "xpath=>//*[@id='search_list']/div[1]/div/div/input"
    freediscount_isenable_search = "xpath=>//*[@id='search_list']/div[2]/div/div/div/input"
    freediscount_search_button = "xpath=>//*[@id='search_list']/div[3]/div/button[1]"
    freediscount_empty_button = "xpath=>//*[@id='search_list']/div[3]/div/button[2]"
    freediscount_isenable = "xpath=>/html/body/div[2]/div[1]/div[1]/ul/li[1]"

    """
    闲时优惠各筛选项
    """

    # 闲时活动标题查询
    def freeactivitytitle_search(self, text):
        self.type(self.freediscount_freeactivitytitle_search, text)

    # 是否启用查询
    def isenable_search(self):
        self.click(self.freediscount_isenable_search)
        self.sleep(2)
        self.click(self.freediscount_isenable)

    # 查询按钮
    def search_button_click(self):
        self.click(self.freediscount_search_button)

    # 清空按钮
    def empty_button_click(self):
        self.click(self.freediscount_empty_button)

    # 测试结果断言
    result_freeactivitytitle = "xpath=>//*[@id='app']/div/div/div[2]/div/div[2]/section/div[1]/div[3]/table/tbody/tr/td[2]/div"
    result_isenable = "xpath=>//*[@id='app']/div/div/div[2]/div/div[2]/section/div[1]/div[3]/table/tbody/tr/td[7]/div/i"

    # 断言闲时活动标题查询结果
    def find_result_freeactivitytitle(self):
        a = self.get_search_result(self.result_freeactivitytitle)
        return a

    # 断言是否启用查询结果
    def find_result_isenable(self):
        a = self.get_search_result_icon(self.result_isenable)
        return a


class DirectRedEnvelopesSearch(BasePage):

    directRedEnvelopes_activityid_search = "xpath=>//*[@id='search_list']/div[1]/div/div/input"
    directRedEnvelopes_activitytitle_search = "xpath=>//*[@id='search_list']/div[2]/div/div/input"
    directRedEnvelopes_coupontype_search = "xpath=>//*[@id='search_list']/div[3]/div/div/div/input"
    directRedEnvelopes_activityenablestatus_search = "xpath=>//*[@id='search_list']/div[4]/div/div/div/input"
    directRedEnvelopes_search_button = "xpath=>//*[@id='search_list']/div[5]/div/button[1]"
    directRedEnvelopes_empty_button = "xpath=>//*[@id='search_list']/div[5]/div/button[2]"
    directRedEnvelopes_coupontype = "xpath=>/html/body/div[2]/div[1]/div[1]/ul/li[1]"
    directRedEnvelopes_activityenablestatus = "xpath=>/html/body/div[3]/div[1]/div[1]/ul/li[1]"

    """
    直通红包各筛选项
    """

    # 活动ID查询
    def activityid_search(self, text):
        self.type(self.directRedEnvelopes_activityid_search, text)

    # 活动标题查询
    def activitytitle_search(self, text):
        self.type(self.directRedEnvelopes_activitytitle_search, text)

    # 优惠券类型查询
    def coupontype_search(self):
        self.click(self.directRedEnvelopes_coupontype_search)
        self.sleep(2)
        self.click(self.directRedEnvelopes_coupontype)

    # 活动启用状态查询
    def activityenablestatus_search(self):
        self.click(self.directRedEnvelopes_activityenablestatus_search)
        self.sleep(2)
        self.click(self.directRedEnvelopes_activityenablestatus)

    # 查询按钮
    def search_button_click(self):
        self.click(self.directRedEnvelopes_search_button)

    # 清空按钮
    def empty_button_click(self):
        self.click(self.directRedEnvelopes_empty_button)

    # 测试结果断言
    result_activityid = "xpath=>//*[@id='app']/div/div/div[2]/div/div[2]/section/div[1]/div[3]/table/tbody/tr/td[2]/div"
    result_activitytitle = "xpath=>//*[@id='app']/div/div/div[2]/div/div[2]/section/div[1]/div[3]/table/tbody/tr/td[4]/div"
    result_coupontype = "xpath=>//*[@id='app']/div/div/div[2]/div/div[2]/section/div[1]/div[3]/table/tbody/tr/td[3]/div"
    result_activityenablestatus = "xpath=>//*[@id='app']/div/div/div[2]/div/div[2]/section/div[1]/div[3]/table/tbody/tr/td[11]/div/i"

    # 断言活动ID查询结果
    def find_result_activityid(self):
        a = self.get_search_result(self.result_activityid)
        return a

    # 断言活动标题查询结果
    def find_result_activitytitle(self):
        a = self.get_search_result(self.result_activitytitle)
        return a

    # 断言优惠券类型查询结果
    def find_result_coupontype(self):
        a = self.get_search_result(self.result_coupontype)
        return a

    # 断言活动启用状态查询结果
    def find_result_activityenablestatus(self):
        a = self.get_search_result_icon(self.result_activityenablestatus)
        return a


class RetentionSearch(BasePage):

    retention_title_search = "xpath=>//*[@id='search_list']/div[1]/div/div/input"
    retention_enablestatus_search = "xpath=>//*[@id='search_list']/div[2]/div/div/div/input"
    retention_search_button = "xpath=>//*[@id='search_list']/div[3]/div/button[1]"
    retention_empty_button = "xpath=>//*[@id='search_list']/div[3]/div/button[2]"
    retention_enablestatus = "xpath=>/html/body/div[2]/div[1]/div[1]/ul/li[1]"

    """
    挽留机制各筛选项
    """

    # 标题查询
    def title_search(self, text):
        self.type(self.retention_title_search, text)

    # 启用状态查询
    def enablestatus_search(self):
        self.click(self.retention_enablestatus_search)
        self.sleep(2)
        self.click(self.retention_enablestatus)

    # 查询按钮
    def search_button_click(self):
        self.click(self.retention_search_button)

    # 清空按钮
    def empty_button_click(self):
        self.click(self.retention_empty_button)

    # 测试结果断言
    result_title = "xpath=>//*[@id='app']/div/div/div[2]/div/div[2]/section/div[1]/div[3]/table/tbody/tr/td[2]/div"
    result_enablestatus = "xpath=>//*[@id='app']/div/div/div[2]/div/div[2]/section/div[1]/div[3]/table/tbody/tr/td[6]/div/i"

    # 断言标题查询结果
    def find_result_title(self):
        a = self.get_search_result(self.result_title)
        return a

    # 断言启用状态查询结果
    def find_result_enablestatus(self):
        a = self.get_search_result_icon(self.result_enablestatus)
        return a


class CardActivitySearch(BasePage):

    cardActivity_title_search = "xpath=>//*[@id='search_list']/div[1]/div/div/input"
    cardActivity_arearestrictiontype_search = "xpath=>//*[@id='search_list']/div[2]/div/div/div/input"
    cardActivity_enablestatus_search = "xpath=>//*[@id='search_list']/div[3]/div/div/div/input"
    cardActivity_search_button = "xpath=>//*[@id='search_list']/div[4]/div/button[1]"
    cardActivity_empty_button = "xpath=>//*[@id='search_list']/div[4]/div/button[2]"
    cardActivity_arearestrictiontype = "xpath=>/html/body/div[2]/div[1]/div[1]/ul/li[1]"
    cardActivity_enablestatus = "xpath=>/html/body/div[3]/div[1]/div[1]/ul/li[1]"

    """
    卡券活动各筛选项
    """

    # 标题查询
    def title_search(self, text):
        self.type(self.cardActivity_title_search, text)

    # 区域限制类型查询
    def arearestrictiontype_search(self):
        self.click(self.cardActivity_arearestrictiontype_search)
        self.sleep(2)
        self.click(self.cardActivity_arearestrictiontype)

    # 启用状态查询
    def enablestatus_search(self):
        self.click(self.cardActivity_enablestatus_search)
        self.sleep(2)
        self.click(self.cardActivity_enablestatus)

    # 查询按钮
    def search_button_click(self):
        self.click(self.cardActivity_search_button)

    # 清空按钮
    def empty_button_click(self):
        self.click(self.cardActivity_empty_button)

    # 测试结果断言
    result_title = "xpath=>//*[@id='app']/div/div/div[2]/div/div[2]/section/div[1]/div[3]/table/tbody/tr/td[2]/div"
    result_arearestrictiontype = "xpath=>//*[@id='app']/div/div/div[2]/div/div[2]/section/div[1]/div[3]/table/tbody/tr/td[4]/div"
    result_enablestatus = "xpath=>//*[@id='app']/div/div/div[2]/div/div[2]/section/div[1]/div[3]/table/tbody/tr/td[9]/div/i"

    # 断言标题查询结果
    def find_result_title(self):
        a = self.get_search_result(self.result_title)
        return a

    # 断言区域限制类型查询结果
    def find_result_arearestrictiontype(self):
        a = self.get_search_result(self.result_arearestrictiontype)
        return a

    # 断言启用状态查询结果
    def find_result_enablestatus(self):
        a = self.get_search_result_icon(self.result_enablestatus)
        return a
