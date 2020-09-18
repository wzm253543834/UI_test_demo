# coding = utf-8
from framework.base_page import BasePage


class FinancePage(BasePage):

    menu_finance = "xpath=>//*[@id='app']/div/div/div[2]/aside/ul/li[6]/div"
    menu_finance_spendBillManage = "xpath=>//*[@id='app']/div/div/div[2]/aside/ul/li[6]/ul/li[1]"
    menu_finance_order = "xpath=>//*[@id='app']/div/div/div[2]/aside/ul/li[6]/ul/li[2]"
    menu_finance_buyCard = "xpath=>//*[@id='app']/div/div/div[2]/aside/ul/li[6]/ul/li[3]"
    menu_finance_sellingCoupons = "xpath=>//*[@id='app']/div/div/div[2]/aside/ul/li[6]/ul/li[4]"
    menu_finance_CardOrder = "xpath=>//*[@id='app']/div/div/div[2]/aside/ul/li[6]/ul/li[5]"
    menu_finance_recharge = "xpath=>//*[@id='app']/div/div/div[2]/aside/ul/li[6]/ul/li[6]"
    menu_finance_dayorder = "xpath=>//*[@id='app']/div/div/div[2]/aside/ul/li[6]/ul/li[7]"
    menu_finance_monthorder = "xpath=>//*[@id='app']/div/div/div[2]/aside/ul/li[6]/ul/li[8]"
    menu_finance_yearorder = "xpath=>//*[@id='app']/div/div/div[2]/aside/ul/li[6]/ul/li[9]"
    menu_finance_exporder = "xpath=>//*[@id='app']/div/div/div[2]/aside/ul/li[6]/ul/li[10]"
    menu_finance_refundorder = "xpath=>//*[@id='app']/div/div/div[2]/aside/ul/li[6]/ul/li[11]"
    menu_finance_checkAccountsDay = "xpath=>//*[@id='app']/div/div/div[2]/aside/ul/li[6]/ul/li[12]"
    menu_finance_checkAccounts = "xpath=>//*[@id='app']/div/div/div[2]/aside/ul/li[6]/ul/li[13]"
    menu_finance_placeMonthorder = "xpath=>//*[@id='app']/div/div/div[2]/aside/ul/li[6]/ul/li[14]"
    menu_finance_deviceMonthorder = "xpath=>//*[@id='app']/div/div/div[2]/aside/ul/li[6]/ul/li[15]"
    menu_finance_billDetails = "xpath=>//*[@id='app']/div/div/div[2]/aside/ul/li[6]/ul/li[16]"
    tab_spendBillManage = "xpath=>//*[@id='tab-181']"
    tab_order = "xpath=>//*[@id='tab-45']"
    tab_buyCard = "xpath=>//*[@id='tab-149']"
    tab_sellingCoupons = "xpath=>//*[@id='tab-152']"
    tab_CardOrder = "xpath=>//*[@id='tab-175']"
    tab_recharge = "xpath=>//*[@id='tab-46']"
    tab_dayorder = "xpath=>//*[@id='tab-47']"
    tab_monthorder = "xpath=>//*[@id='tab-48']"
    tab_yearorder = "xpath=>//*[@id='tab-49']"
    tab_exporder = "xpath=>//*[@id='tab-50']"
    tab_refundorder = "xpath=>//*[@id='tab-51']"
    tab_checkAccountsDay = "xpath=>//*[@id='tab-134']"
    tab_checkAccounts = "xpath=>//*[@id='tab-127']"
    tab_placeMonthorder = "xpath=>//*[@id='tab-142']"
    tab_deviceMonthorder = "xpath=>//*[@id='tab-147']"
    tab_billDetails = "xpath=>//*[@id='tab-184']"

    """
    财务管理各菜单地址及tab页地址
    """

    # 点击财务管理
    def search_click_finance(self):
        self.click(self.menu_finance)

    # 点击费用票据管理
    def search_click_finance_spendbillmanage(self):
        self.click(self.menu_finance_spendBillManage)

    # 获取费用票据管理tab名
    def find_tab_spendbillmanage(self):
        a = self.get_tab_title(self.tab_spendBillManage)
        return a

    # 点击订单流水
    def search_click_finance_order(self):
        self.click(self.menu_finance_order)

    # 获取订单流水tab名
    def find_tab_order(self):
        a = self.get_tab_title(self.tab_order)
        return a

    # 点击购卡流水
    def search_click_finance_buycard(self):
        self.click(self.menu_finance_buyCard)

    # 获取购卡流水tab名
    def find_tab_buycard(self):
        a = self.get_tab_title(self.tab_buyCard)
        return a

    # 点击卖券流水
    def search_click_finance_sellingcoupons(self):
        self.click(self.menu_finance_sellingCoupons)

    # 获取卖券流水tab名
    def find_tab_sellingcoupons(self):
        a = self.get_tab_title(self.tab_sellingCoupons)
        return a

    # 点击卡订单结算
    def search_click_finance_cardorder(self):
        self.click(self.menu_finance_CardOrder)

    # 获取卡订单结算tab名
    def find_tab_cardorder(self):
        a = self.get_tab_title(self.tab_CardOrder)
        return a

    # 点击充值订单
    def search_click_finance_recharge(self):
        self.click(self.menu_finance_recharge)

    # 获取充值订单tab名
    def find_tab_recharge(self):
        a = self.get_tab_title(self.tab_recharge)
        return a

    # 点击日报表
    def search_click_finance_dayorder(self):
        self.click(self.menu_finance_dayorder)

    # 获取日报表tab名
    def find_tab_dayorder(self):
        a = self.get_tab_title(self.tab_dayorder)
        return a

    # 点击月报表
    def search_click_finance_monthorder(self):
        self.click(self.menu_finance_monthorder)

    # 获取月报表tab名
    def find_tab_monthorder(self):
        a = self.get_tab_title(self.tab_monthorder)
        return a

    # 点击年报表
    def search_click_finance_yearorder(self):
        self.click(self.menu_finance_yearorder)

    # 获取年报表tab名
    def find_tab_yearorder(self):
        a = self.get_tab_title(self.tab_yearorder)
        return a

    # 点击异常订单
    def search_click_finance_exporder(self):
        self.click(self.menu_finance_exporder)

    # 获取异常订单tab名
    def find_tab_exporder(self):
        a = self.get_tab_title(self.tab_exporder)
        return a

    # 点击退款订单
    def search_click_finance_refundorder(self):
        self.click(self.menu_finance_refundorder)

    # 获取退款订单tab名
    def find_tab_refundorder(self):
        a = self.get_tab_title(self.tab_refundorder)
        return a

    # 点击财务对账（日）
    def search_click_finance_checkaccountsday(self):
        self.click(self.menu_finance_checkAccountsDay)

    # 获取财务对账（日）tab名
    def find_tab_checkaccountsday(self):
        a = self.get_tab_title(self.tab_checkAccountsDay)
        return a

    # 点击财务对账（月）
    def search_click_finance_checkaccounts(self):
        self.click(self.menu_finance_checkAccounts)

    # 获取财务对账（月）tab名
    def find_tab_checkaccounts(self):
        a = self.get_tab_title(self.tab_checkAccounts)
        return a

    # 点击场地月报表
    def search_click_finance_placemonthorder(self):
        self.click(self.menu_finance_placeMonthorder)

    # 获取场地月报表tab名
    def find_tab_placemonthorder(self):
        a = self.get_tab_title(self.tab_placeMonthorder)
        return a

    # 点击设备月报表
    def search_click_finance_devicemonthorder(self):
        self.click(self.menu_finance_deviceMonthorder)

    # 获取设备月报表tab名
    def find_tab_devicemonthorder(self):
        a = self.get_tab_title(self.tab_deviceMonthorder)
        return a

    # 点击账单明细表
    def search_click_finance_billdetails(self):
        self.click(self.menu_finance_billDetails)

    # 获取账单明细表tab名
    def find_tab_billdetails(self):
        a = self.get_tab_title(self.tab_billDetails)
        return a


class SpendBillManageSearch(BasePage):

    spendBillManage_taskid_search = "xpath=>//*[@id='search_list']/div[1]/div[1]/div/div/input"
    spendBillManage_areaid_search = "xpath=>//*[@id='search_list']/div[1]/div[2]/div/div/input"
    spendBillManage_areaname_search = "xpath=>//*[@id='search_list']/div[1]/div[3]/div/div/input"
    spendBillManage_payee_search = "xpath=>//*[@id='search_list']/div[1]/div[4]/div/div/input"
    spendBillManage_costtype_search = "xpath=>//*[@id='search_list']/div[1]/div[5]/div/div/div/input"
    spendBillManage_billregistrationstatus_search = "xpath=>//*[@id='search_list']/div[1]/div[6]/div/div/div/input"
    spendBillManage_applicationtime_search = "xpath=>//*[@id='search_list']/div[1]/div[7]/div/div/input[1]"
    spendBillManage_invoicenumber_search = "xpath=>//*[@id='search_list']/div[1]/div[8]/div/div/input"
    spendBillManage_search_button = "xpath=>//*[@id='search_list']/div[2]/div[1]/div/button"
    spendBillManage_empty_button = "xpath=>//*[@id='search_list']/div[2]/div[2]/div/button"
    spendBillManage_costtype = "xpath=>/html/body/div[3]/div[1]/div[1]/ul/li[1]"
    spendBillManage_billregistrationstatus = "xpath=>/html/body/div[4]/div[1]/div[1]/ul/li[1]"
    spendBillManage_applicationtime = "xpath=>/html/body/div[2]/div[1]/div/div[1]/table/tbody/tr[2]/td[3]/div"

    """
    费用票据管理各筛选项
    """

    # 任务ID查询
    def taskid_search(self, text):
        self.type(self.spendBillManage_taskid_search, text)

    # 网点ID查询
    def areaid_search(self, text):
        self.type(self.spendBillManage_areaid_search, text)

    # 网点名称查询
    def areaname_search(self, text):
        self.type(self.spendBillManage_areaname_search, text)

    # 收款单位查询
    def payee_search(self, text):
        self.type(self.spendBillManage_payee_search, text)

    # 费用类别查询
    def costtype_search(self):
        self.click(self.spendBillManage_costtype_search)
        self.sleep(2)
        self.click(self.spendBillManage_costtype)

    # 票据登记状态查询
    def billregistrationstatus_search(self):
        self.click(self.spendBillManage_billregistrationstatus_search)
        self.sleep(2)
        self.click(self.spendBillManage_billregistrationstatus)

    # 申请时间查询
    def applicationtime_search(self):
        self.click(self.spendBillManage_applicationtime_search)
        self.sleep(2)
        self.click(self.spendBillManage_applicationtime)
        self.click(self.spendBillManage_applicationtime)

    # 发票号码查询
    def invoicenumber_search(self, text):
        self.type(self.spendBillManage_invoicenumber_search, text)

    # 查询按钮
    def search_button_click(self):
        self.click(self.spendBillManage_search_button)

    # 清空按钮
    def empty_button_click(self):
        self.click(self.spendBillManage_empty_button)

    # 测试结果断言
    result_taskid = "xpath=>//*[@id='spendBillManage']/section/div[1]/div[3]/table/tbody/tr/td[2]/div"
    result_areaid = "xpath=>//*[@id='spendBillManage']/section/div[1]/div[3]/table/tbody/tr/td[3]/div"
    result_areaname = "xpath=>//*[@id='spendBillManage']/section/div[1]/div[3]/table/tbody/tr/td[4]/div"
    result_payee = "xpath=>//*[@id='spendBillManage']/section/div[1]/div[3]/table/tbody/tr/td[5]/div"
    # result_costtype = "xpath=>"
    result_billregistrationstatus = "xpath=>//*[@id='spendBillManage']/section/div[1]/div[3]/table/tbody/tr/td[8]/div"
    result_applicationtime = "xpath=>//*[@id='spendBillManage']/section/div[1]/div[3]/table/tbody/tr/td[9]/div"
    # result_invoicenumber = "xpath=>"

    # 断言任务ID查询结果
    def find_result_taskid(self):
        a = self.get_search_result(self.result_taskid)
        return a

    # 断言网点ID查询结果
    def find_result_areaid(self):
        a = self.get_search_result(self.result_areaid)
        return a

    # 断言网点名称查询结果
    def find_result_areaname(self):
        a = self.get_search_result(self.result_areaname)
        return a

    # 断言收款单位查询结果
    def find_result_payee(self):
        a = self.get_search_result(self.result_payee)
        return a

    # 断言票据登记状态查询结果
    def find_result_billregistrationstatus(self):
        a = self.get_search_result(self.result_billregistrationstatus)
        return a

    # 断言申请时间查询结果
    def find_result_applicationtime(self):
        a = self.get_search_result(self.result_applicationtime)
        return a


class OrderSearch(BasePage):

    order_creationtime_search = "xpath=>//*[@id='search_list']/div[1]/div/div/input"
    order_paymentmethod_search = "xpath=>//*[@id='search_list']/div[2]/div/div/div/input"
    order_ordernumber_search = "xpath=>//*[@id='search_list']/div[3]/div/div/input"
    order_orderstatus_search = "xpath=>//*[@id='search_list']/div[4]/div/div/div/input"
    order_transactionnumber_search = "xpath=>//*[@id='search_list']/div[5]/div/div/input"
    order_areaname_search = "xpath=>//*[@id='search_list']/div[6]/div/div/input"
    order_deviceid_search = "xpath=>//*[@id='search_list']/div[8]/div/div/input"
    order_activitytype_search = "xpath=>//*[@id='search_list']/div[9]/div/div/div/input"
    order_province_search = "xpath=>//*[@id='search_list']/div[10]/div/div/div/input"
    order_city_search = "xpath=>//*[@id='search_list']/div[11]/div/div/div/input"
    order_areawithdrawal_search = "xpath=>//*[@id='search_list']/div[12]/div/div/div/input"
    order_search_button = "xpath=>//*[@id='search_list']/div[6]/div/button"
    order_empty_button = "xpath=>//*[@id='search_list']/div[13]/div/button"
    order_creationtime = "xpath=>/html/body/div[2]/div[1]/div/div[2]/table[1]/tbody/tr[2]/td[1]/div"
    order_paymentmethod = "xpath=>/html/body/div[3]/div[1]/div[1]/ul/li[1]"
    order_orderstatus = "xpath=>/html/body/div[4]/div[1]/div[1]/ul/li[1]"
    order_activitytype = "xpath=>/html/body/div[5]/div[1]/div[1]/ul/li[1]"
    order_province = "xpath=>/html/body/div[6]/div[1]/div[1]/ul/li[1]"
    order_city = "xpath=>/html/body/div[7]/div[1]/div[1]/ul/li[1]"
    order_areawithdrawal = "xpath=>/html/body/div[8]/div[1]/div[1]/ul/li[1]"

    """
    订单流水各筛选项
    """

    # 创建时间查询
    def creationtime_search(self):
        self.click(self.order_creationtime_search)
        self.sleep(2)
        self.click(self.order_creationtime)

    # 付款方式查询
    def paymentmethod_search(self):
        self.click(self.order_paymentmethod_search)
        self.sleep(2)
        self.click(self.order_paymentmethod)

    # 订单号查询
    def ordernumber_search(self, text):
        self.type(self.order_ordernumber_search, text)

    # 订单状态查询
    def orderstatus_search(self):
        self.click(self.order_orderstatus_search)
        self.sleep(2)
        self.click(self.order_orderstatus)

    # 交易单号查询
    def transactionnumber_search(self, text):
        self.type(self.order_transactionnumber_search, text)

    # 网点名称查询
    def areaname_search(self, text):
        self.type(self.order_areaname_search, text)

    # 设备ID查询
    def deviceid_search(self, text):
        self.type(self.order_deviceid_search, text)

    # 活动类型查询
    def activitytype_search(self):
        self.click(self.order_activitytype_search)
        self.sleep(2)
        self.click(self.order_activitytype)

    # 省份查询
    def province_search(self):
        self.click(self.order_province_search)
        self.sleep(2)
        self.click(self.order_province)

    # 城市查询
    def city_search(self):
        self.click(self.order_province_search)
        self.sleep(2)
        self.click(self.order_province)
        self.sleep(2)
        self.click(self.order_city_search)
        self.sleep(2)
        self.click(self.order_city)

    # 网点提现查询
    def areawithdrawal_search(self):
        self.click(self.order_areawithdrawal_search)
        self.sleep(2)
        self.click(self.order_areawithdrawal)

    # 查询按钮
    def search_button_click(self):
        self.click(self.order_search_button)

    # 清空按钮
    def empty_button_click(self):
        self.click(self.order_empty_button)

    # 测试结果断言
    result_creationtime = "xpath=>//*[@id='app']/div/div/div[2]/div/div[2]/section/div[1]/div[3]/table/tbody/tr/td[19]/div"
    result_paymentmethod = "xpath=>//*[@id='app']/div/div/div[2]/div/div[2]/section/div[1]/div[3]/table/tbody/tr/td[18]/div"
    result_ordernumber = "xpath=>//*[@id='app']/div/div/div[2]/div/div[2]/section/div[1]/div[3]/table/tbody/tr/td[2]/div"
    result_orderstatus = "xpath=>//*[@id='app']/div/div/div[2]/div/div[2]/section/div[1]/div[3]/table/tbody/tr/td[6]/div"
    result_transactionnumber = "xpath=>//*[@id='app']/div/div/div[2]/div/div[2]/section/div[1]/div[3]/table/tbody/tr/td[3]/div"
    result_areaname = "xpath=>//*[@id='app']/div/div/div[2]/div/div[2]/section/div[1]/div[3]/table/tbody/tr/td[5]/div"
    result_deviceid = "xpath=>//*[@id='app']/div/div/div[2]/div/div[2]/section/div[1]/div[3]/table/tbody/tr/td[7]/div"
    result_activitytype = "xpath=>//*[@id='app']/div/div/div[2]/div/div[2]/section/div[1]/div[3]/table/tbody/tr/td[16]/div"
    result_province = "xpath=>//*[@id='app']/div/div/div[2]/div/div[2]/section/div[1]/div[3]/table/tbody/tr/td[11]/div"
    result_city = "xpath=>//*[@id='app']/div/div/div[2]/div/div[2]/section/div[1]/div[3]/table/tbody/tr/td[12]/div"
    # result_areawithdrawal = "xpath=>"

    # 断言创建时间查询结果
    def find_result_creationtime(self):
        a = self.get_search_result(self.result_creationtime)
        return a

    # 断言付款方式查询结果
    def find_result_paymentmethod(self):
        a = self.get_search_result(self.result_paymentmethod)
        return a

    # 断言订单号查询结果
    def find_result_ordernumber(self):
        a = self.get_search_result(self.result_ordernumber)
        return a

    # 断言订单状态查询结果
    def find_result_orderstatus(self):
        a = self.get_search_result(self.result_orderstatus)
        return a

    # 断言交易单号查询结果
    def find_result_transactionnumber(self):
        a = self.get_search_result(self.result_transactionnumber)
        return a

    # 断言网点名称查询结果
    def find_result_areaname(self):
        a = self.get_search_result(self.result_areaname)
        return a

    # 断言设备ID查询结果
    def find_result_deviceid(self):
        a = self.get_search_result(self.result_deviceid)
        return a

    # 断言活动类型查询结果
    def find_result_activitytype(self):
        a = self.get_search_result(self.result_activitytype)
        return a

    # 断言省份查询结果
    def find_result_province(self):
        a = self.get_search_result(self.result_province)
        return a

    # 断言城市查询结果
    def find_result_city(self):
        a = self.get_search_result(self.result_city)
        return a


class BuyCardSearch(BasePage):

    buyCard_creationtime_search = "xpath=>//*[@id='search_list']/div[1]/div/div/input[1]"
    buyCard_orderstatus_search = "xpath=>//*[@id='search_list']/div[2]/div/div/div/input"
    buyCard_ordernumber_search = "xpath=>//*[@id='search_list']/div[3]/div/div/input"
    buyCard_cardstatus_search = "xpath=>//*[@id='search_list']/div[4]/div/div/div/input"
    buyCard_paymethod_search = "xpath=>//*[@id='search_list']/div[5]/div/div/div/input"
    buyCard_orderamountlow_search = "xpath=>//*[@id='search_list']/div[7]/div/div[1]/input"
    buyCard_orderamounthigh_search = "xpath=>//*[@id='search_list']/div[7]/div/div[2]/input"
    buyCard_transactionnumber_search = "xpath=>//*[@id='search_list']/div[8]/div/div/input"
    buyCard_cardtype_search = "xpath=>//*[@id='search_list']/div[9]/div/div/div/input"
    buyCard_arearestrictiontype_search = "xpath=>//*[@id='search_list']/div[10]/div/div/div/input"
    buyCard_logisticsstatus_search = "xpath=>//*[@id='search_list']/div[11]/div/div/div/input"
    buyCard_search_button = "xpath=>//*[@id='search_list']/div[6]/div/button"
    buyCard_empty_button = "xpath=>//*[@id='search_list']/div[12]/div/button"
    buyCard_creationtime = "xpath=>/html/body/div[2]/div[1]/div/div[1]/table/tbody/tr[2]/td[1]/div"
    buyCard_orderstatus = "xpath=>/html/body/div[3]/div[1]/div[1]/ul/li[1]"
    buyCard_cardstatus = "xpath=>/html/body/div[4]/div[1]/div[1]/ul/li[1]"
    buyCard_paymethod = "xpath=>/html/body/div[5]/div[1]/div[1]/ul/li[1]"
    buyCard_cardtype = "xpath=>/html/body/div[6]/div[1]/div[1]/ul/li[8]"
    buyCard_arearestrictiontype = "xpath=>/html/body/div[7]/div[1]/div[1]/ul/li[1]"
    buyCard_logisticsstatus = "xpath=>/html/body/div[8]/div[1]/div[1]/ul/li[1]"

    """
    订单流水各筛选项
    """

    # 创建时间查询
    def creationtime_search(self):
        self.click(self.buyCard_creationtime_search)
        self.sleep(2)
        self.click(self.buyCard_creationtime)
        self.sleep(2)
        self.click(self.buyCard_creationtime)

    # 订单状态查询
    def orderstatus_search(self):
        self.click(self.buyCard_orderstatus_search)
        self.sleep(2)
        self.click(self.buyCard_orderstatus)

    # 订单号查询
    def ordernumber_search(self, text):
        self.type(self.buyCard_ordernumber_search, text)

    # 卡状态查询
    def cardstatus_search(self):
        self.click(self.buyCard_cardstatus_search)
        self.sleep(2)
        self.click(self.buyCard_cardstatus)

    # 支付方式查询
    def paymethod_search(self):
        self.click(self.buyCard_paymethod_search)
        self.sleep(2)
        self.click(self.buyCard_paymethod)

    # 订单金额（元）小查询
    def orderamountlow_search(self, text):
        self.type(self.buyCard_orderamountlow_search, text)

    # 订单金额（元）大查询
    def orderamounthigh_search(self, text):
        self.type(self.buyCard_orderamounthigh_search, text)

    # 交易单号查询
    def transactionnumber_search(self, text):
        self.type(self.buyCard_transactionnumber_search, text)

    # 卡类型查询
    def cardtype_search(self):
        self.click(self.buyCard_cardtype_search)
        self.sleep(2)
        self.click(self.buyCard_cardtype)

    # 区域限制类型查询
    def arearestrictiontype_search(self):
        self.click(self.buyCard_arearestrictiontype_search)
        self.sleep(2)
        self.click(self.buyCard_arearestrictiontype)

    # 物流状态查询
    def logisticsstatus_search(self):
        self.click(self.buyCard_logisticsstatus_search)
        self.sleep(2)
        self.click(self.buyCard_logisticsstatus)

    # 查询按钮
    def search_button_click(self):
        self.click(self.buyCard_search_button)

    # 清空按钮
    def empty_button_click(self):
        self.click(self.buyCard_empty_button)

    # 测试结果断言
    result_creationtime = "xpath=>//*[@id='app']/div/div/div[2]/div/div[2]/section/div[1]/div[3]/table/tbody/tr/td[19]/div"
    result_orderstatus = "xpath=>//*[@id='app']/div/div/div[2]/div/div[2]/section/div[1]/div[3]/table/tbody/tr/td[6]/div"
    result_ordernumber = "xpath=>//*[@id='app']/div/div/div[2]/div/div[2]/section/div[1]/div[3]/table/tbody/tr/td[2]/div"
    result_cardstatus = "xpath=>//*[@id='app']/div/div/div[2]/div/div[2]/section/div[1]/div[3]/table/tbody/tr/td[23]/div"
    result_paymethod = "xpath=>//*[@id='app']/div/div/div[2]/div/div[2]/section/div[1]/div[3]/table/tbody/tr/td[7]/div"
    result_orderamount = "xpath=>//*[@id='app']/div/div/div[2]/div/div[2]/section/div[1]/div[3]/table/tbody/tr/td[5]/div"
    result_transactionnumber = "xpath=>//*[@id='app']/div/div/div[2]/div/div[2]/section/div[1]/div[3]/table/tbody/tr/td[3]/div"
    result_cardtype = "xpath=>//*[@id='app']/div/div/div[2]/div/div[2]/section/div[1]/div[3]/table/tbody/tr/td[10]/div"
    result_arearestrictiontype = "xpath=>//*[@id='app']/div/div/div[2]/div/div[2]/section/div[1]/div[3]/table/tbody/tr/td[12]/div"
    # result_logisticsstatus = "xpath=>"

    # 断言创建时间查询结果
    def find_result_creationtime(self):
        a = self.get_search_result(self.result_creationtime)
        return a

    # 断言订单状态查询结果
    def find_result_orderstatus(self):
        a = self.get_search_result(self.result_orderstatus)
        return a

    # 断言订单号查询结果
    def find_result_ordernumber(self):
        a = self.get_search_result(self.result_ordernumber)
        return a

    # 断言卡状态查询结果
    def find_result_cardstatus(self):
        a = self.get_search_result(self.result_cardstatus)
        return a

    # 断言支付方式查询结果
    def find_result_paymethod(self):
        a = self.get_search_result(self.result_paymethod)
        return a

    # 断言订单金额（元）查询结果
    def find_result_orderamount(self):
        a = self.get_search_result(self.result_orderamount)
        return a

    # 断言交易单号查询结果
    def find_result_transactionnumber(self):
        a = self.get_search_result(self.result_transactionnumber)
        return a

    # 断言卡类型查询结果
    def find_result_cardtype(self):
        a = self.get_search_result(self.result_cardtype)
        return a

    # 断言区域限制类型查询结果
    def find_result_arearestrictiontype(self):
        a = self.get_search_result(self.result_arearestrictiontype)
        return a


class SellingCouponsSearch(BasePage):

    sellingCoupons_creationtime_search = "xpath=>//*[@id='search_list']/div[1]/div/div/input[1]"
    sellingCoupons_orderstatus_search = "xpath=>//*[@id='search_list']/div[2]/div/div/div/input"
    sellingCoupons_paymethod_search = "xpath=>//*[@id='search_list']/div[3]/div/div/div/input"
    sellingCoupons_partnername_search = "xpath=>//*[@id='search_list']/div[4]/div/div/input"
    sellingCoupons_areaname_search = "xpath=>//*[@id='search_list']/div[5]/div/div/input"
    sellingCoupons_promotionchannels_search = "xpath=>//*[@id='search_list']/div[7]/div/div/div/input"
    sellingCoupons_ordernumber_search = "xpath=>//*[@id='search_list']/div[8]/div/div/input"
    sellingCoupons_province_search = "xpath=>//*[@id='search_list']/div[9]/div/div/div/input"
    sellingCoupons_city_search = "xpath=>//*[@id='search_list']/div[10]/div/div/div/input"
    sellingCoupons_search_button = "xpath=>//*[@id='search_list']/div[5]/div/button"
    sellingCoupons_empty_button = "xpath=>//*[@id='search_list']/div[11]/div/button"
    sellingCoupons_creationtime = "xpath=>/html/body/div[2]/div[1]/div/div[1]/table/tbody/tr[2]/td[1]/div"
    sellingCoupons_orderstatus = "xpath=>/html/body/div[3]/div[1]/div[1]/ul/li[1]"
    sellingCoupons_paymethod = "xpath=>/html/body/div[4]/div[1]/div[1]/ul/li[1]"
    sellingCoupons_promotionchannels = "xpath=>/html/body/div[5]/div[1]/div[1]/ul/li[1]"
    sellingCoupons_province = "xpath=>/html/body/div[6]/div[1]/div[1]/ul/li[1]"
    sellingCoupons_city = "xpath=>/html/body/div[7]/div[1]/div[1]/ul/li[1]"

    """
    卖券流水各筛选项
    """

    # 创建时间查询
    def creationtime_search(self):
        self.click(self.sellingCoupons_creationtime_search)
        self.sleep(2)
        self.click(self.sellingCoupons_creationtime)
        self.sleep(2)
        self.click(self.sellingCoupons_creationtime)

    # 订单状态查询
    def orderstatus_search(self):
        self.click(self.sellingCoupons_orderstatus_search)
        self.sleep(2)
        self.click(self.sellingCoupons_orderstatus)

    # 支付方式查询
    def paymethod_search(self):
        self.click(self.sellingCoupons_paymethod_search)
        self.sleep(2)
        self.click(self.sellingCoupons_paymethod)

    # 合伙人查询
    def partnername_search(self, text):
        self.type(self.sellingCoupons_partnername_search, text)

    # 网点名称查询
    def areaname_search(self, text):
        self.type(self.sellingCoupons_areaname_search, text)

    # 推广渠道查询
    def promotionchannels_search(self):
        self.click(self.sellingCoupons_promotionchannels_search)
        self.sleep(2)
        self.click(self.sellingCoupons_promotionchannels)

    # 订单号查询
    def ordernumber_search(self, text):
        self.type(self.sellingCoupons_ordernumber_search, text)

    # 省份查询
    def province_search(self):
        self.click(self.sellingCoupons_province_search)
        self.sleep(2)
        self.click(self.sellingCoupons_province)

    # 城市查询
    def city_search(self):
        self.click(self.sellingCoupons_province_search)
        self.sleep(2)
        self.click(self.sellingCoupons_province)
        self.sleep(2)
        self.click(self.sellingCoupons_city_search)
        self.sleep(2)
        self.click(self.sellingCoupons_city)

    # 查询按钮
    def search_button_click(self):
        self.click(self.sellingCoupons_search_button)

    # 清空按钮
    def empty_button_click(self):
        self.click(self.sellingCoupons_empty_button)

    # 测试结果断言
    result_creationtime = "xpath=>//*[@id=‘sellingCoupons’]/div[1]/div[3]/table/tbody/tr/td[12]/div"
    result_orderstatus = "xpath=>//*[@id=‘sellingCoupons’]/div[1]/div[3]/table/tbody/tr/td[7]/div"
    result_paymethod = "xpath=>//*[@id=‘sellingCoupons’]/div[1]/div[3]/table/tbody/tr/td[8]/div"
    # result_partnername = "xpath=>"
    # result_areaname = "xpath=>"
    result_promotionchannels = "xpath=>//*[@id=‘sellingCoupons’]/div[1]/div[3]/table/tbody/tr/td[11]/div"
    result_ordernumber = "xpath=>//*[@id=‘sellingCoupons’]/div[1]/div[3]/table/tbody/tr/td[2]/div"
    # result_province = "xpath=>"
    # result_city = "xpath=>"

    # 断言创建时间查询结果
    def find_result_creationtime(self):
        a = self.get_search_result(self.result_creationtime)
        return a

    # 断言订单状态查询结果
    def find_result_orderstatus(self):
        a = self.get_search_result(self.result_orderstatus)
        return a

    # 断言支付方式查询结果
    def find_result_paymethod(self):
        a = self.get_search_result(self.result_paymethod)
        return a

    # 断言推广渠道查询结果
    def find_result_promotionchannels(self):
        a = self.get_search_result(self.result_promotionchannels)
        return a

    # 断言订单号查询结果
    def find_result_ordernumber(self):
        a = self.get_search_result(self.result_ordernumber)
        return a


class CardOrderSearch(BasePage):

    CardOrder_accountcheckingmonth_search = "xpath=>//*[@id='app']/div/div/div[2]/div/div[2]/div/div[1]/form/div[1]/div/div/input"
    CardOrder_massagetime_search = "xpath=>//*[@id='app']/div/div/div[2]/div/div[2]/div/div[1]/form/div[2]/div/div/input[1]"
    CardOrder_buycardtime_search = "xpath=>//*[@id='app']/div/div/div[2]/div/div[2]/div/div[1]/form/div[3]/div/div/input[1]"
    CardOrder_massageordernumber_search = "xpath=>//*[@id='app']/div/div/div[2]/div/div[2]/div/div[1]/form/div[5]/div/div/input"
    CardOrder_buycardordernumber_search = "xpath=>//*[@id='app']/div/div/div[2]/div/div[2]/div/div[1]/form/div[6]/div/div/input"
    CardOrder_cardtype_search = "xpath=>//*[@id='app']/div/div/div[2]/div/div[2]/div/div[1]/form/div[7]/div/div/div[2]/input"
    CardOrder_partnername_search = "xpath=>//*[@id='app']/div/div/div[2]/div/div[2]/div/div[1]/form/div[8]/div/div/input"
    CardOrder_search_button = "xpath=>//*[@id='app']/div/div/div[2]/div/div[2]/div/div[1]/form/div[4]/div/button"
    CardOrder_empty_button = "xpath=>//*[@id='app']/div/div/div[2]/div/div[2]/div/div[1]/form/div[9]/div/button"
    CardOrder_accountcheckingmonth = "xpath=>/html/body/div[2]/div[1]/div/div[2]/table[3]/tbody/tr[2]/td[3]/a"
    CardOrder_massagetime = "xpath=>/html/body/div[3]/div[1]/div/div[1]/table/tbody/tr[2]/td[1]/div"
    CardOrder_buycardtime = "xpath=>/html/body/div[4]/div[1]/div/div[1]/table/tbody/tr[2]/td[1]/div"
    CardOrder_cardtype = "xpath=>/html/body/div[5]/div[1]/div[1]/ul/li[8]"

    """
    卡订单结算各筛选项
    """

    # 核账月份查询
    def accountcheckingmonth_search(self):
        self.click(self.CardOrder_accountcheckingmonth_search)
        self.sleep(2)
        self.click(self.CardOrder_accountcheckingmonth)

    # 按摩时间查询
    def massagetime_search(self):
        self.click(self.CardOrder_massagetime_search)
        self.sleep(2)
        self.click(self.CardOrder_massagetime)
        self.sleep(2)
        self.click(self.CardOrder_massagetime)

    # 购卡时间查询
    def buycardtime_search(self):
        self.click(self.CardOrder_buycardtime_search)
        self.sleep(2)
        self.click(self.CardOrder_buycardtime)
        self.sleep(2)
        self.click(self.CardOrder_buycardtime)

    # 按摩订单号查询
    def massageordernumber_search(self, text):
        self.type(self.CardOrder_massageordernumber_search, text)

    # 购卡订单号查询
    def buycardordernumber_search(self, text):
        self.type(self.CardOrder_buycardordernumber_search, text)

    # 卡类型查询
    def cardtype_search(self):
        self.click(self.CardOrder_cardtype_search)
        self.sleep(2)
        self.click(self.CardOrder_cardtype)

    # 合伙人查询
    def partnername_search(self, text):
        self.type(self.CardOrder_partnername_search, text)

    # 查询按钮
    def search_button_click(self):
        self.click(self.CardOrder_search_button)

    # 清空按钮
    def empty_button_click(self):
        self.click(self.CardOrder_empty_button)

    # 测试结果断言
    # result_accountcheckingmonth = "xpath=>"
    result_massagetime = "xpath=>//*[@id='tableHeight']/div[3]/table/tbody/tr/td[18]/div"
    result_buycardtime = "xpath=>//*[@id='tableHeight']/div[3]/table/tbody/tr/td[5]/div"
    result_massageordernumber = "xpath=>//*[@id='tableHeight']/div[3]/table/tbody/tr/td[2]/div"
    result_buycardordernumber = "xpath=>//*[@id='tableHeight']/div[3]/table/tbody/tr/td[3]/div"
    result_cardtype = "xpath=>//*[@id='tableHeight']/div[3]/table/tbody/tr/td[7]/div"
    result_partnername = "xpath=>//*[@id='tableHeight']/div[3]/table/tbody/tr/td[17]/div"

    # 断言按摩时间查询结果
    def find_result_massagetime(self):
        a = self.get_search_result(self.result_massagetime)
        return a

    # 断言购卡时间查询结果
    def find_result_buycardtime(self):
        a = self.get_search_result(self.result_buycardtime)
        return a

    # 断言按摩订单号查询结果
    def find_result_massageordernumber(self):
        a = self.get_search_result(self.result_massageordernumber)
        return a

    # 断言购卡订单号查询结果
    def find_result_buycardordernumber(self):
        a = self.get_search_result(self.result_buycardordernumber)
        return a

    # 断言卡类型查询结果
    def find_result_cardtype(self):
        a = self.get_search_result(self.result_cardtype)
        return a

    # 断言合伙人查询结果
    def find_result_partnername(self):
        a = self.get_search_result(self.result_partnername)
        return a


class RechargeSearch(BasePage):

    recharge_creationtime_search = "xpath=>//*[@id='search_list']/div[1]/div/div/input[1]"
    recharge_orderstatus_search = "xpath=>//*[@id='search_list']/div[2]/div/div/div/input"
    recharge_ordernumber_search = "xpath=>//*[@id='search_list']/div[3]/div/div/input"
    recharge_transactionnumber_search = "xpath=>//*[@id='search_list']/div[4]/div/div/input"
    recharge_paymentaccountnumber_search = "xpath=>//*[@id='search_list']/div[5]/div/div/input"
    recharge_orderamountlow_search = "xpath=>//*[@id='search_list']/div[7]/div/div[1]/input"
    recharge_orderamounthigh_search = "xpath=>//*[@id='search_list']/div[7]/div/div[2]/input"
    recharge_channelsource_search = "xpath=>//*[@id='search_list']/div[8]/div/div/div/input"
    recharge_querycriteria_search = "xpath=>//*[@id='search_list']/div[9]/div/div/div/input"
    recharge_search_button = "xpath=>//*[@id='search_list']/div[6]/div/button"
    recharge_empty_button = "xpath=>//*[@id='search_list']/div[10]/div/button"
    recharge_creationtime = "xpath=>/html/body/div[2]/div[1]/div/div[1]/table/tbody/tr[2]/td[1]/div"
    recharge_orderstatus = "xpath=>/html/body/div[3]/div[1]/div[1]/ul/li[1]"
    recharge_channelsource = "xpath=>/html/body/div[4]/div[1]/div[1]/ul/li[1]"
    recharge_querycriteria = "xpath=>/html/body/div[5]/div[1]/div[1]/ul/li[1]"

    """
    充值订单各筛选项
    """

    # 创建时间查询
    def creationtime_search(self):
        self.click(self.recharge_creationtime_search)
        self.sleep(2)
        self.click(self.recharge_creationtime)
        self.sleep(2)
        self.click(self.recharge_creationtime)

    # 订单状态查询
    def orderstatus_search(self):
        self.click(self.recharge_orderstatus_search)
        self.sleep(2)
        self.click(self.recharge_orderstatus)

    # 订单号查询
    def ordernumber_search(self, text):
        self.type(self.recharge_ordernumber_search, text)

    # 交易单号查询
    def transactionnumber_search(self, text):
        self.type(self.recharge_transactionnumber_search, text)

    # 付款账号查询
    def paymentaccountnumber_search(self, text):
        self.type(self.recharge_paymentaccountnumber_search, text)

    # 订单金额（元）小查询
    def orderamountlow_search(self, text):
        self.type(self.recharge_orderamountlow_search, text)

    # 订单金额（元）大查询
    def orderamounthigh_search(self, text):
        self.type(self.recharge_orderamounthigh_search, text)

    # 渠道来源查询
    def channelsource_search(self):
        self.click(self.recharge_channelsource_search)
        self.sleep(2)
        self.click(self.recharge_channelsource)

    # 查询条件查询
    def querycriteria_search(self):
        self.click(self.recharge_querycriteria_search)
        self.sleep(2)
        self.click(self.recharge_querycriteria)

    # 查询按钮
    def search_button_click(self):
        self.click(self.recharge_search_button)

    # 清空按钮
    def empty_button_click(self):
        self.click(self.recharge_empty_button)

    # 测试结果断言
    result_creationtime = "xpath=>//*[@id='app']/div/div/div[2]/div/div[2]/section/div[1]/div[3]/table/tbody/tr/td[13]/div"
    result_orderstatus = "xpath=>//*[@id='app']/div/div/div[2]/div/div[2]/section/div[1]/div[3]/table/tbody/tr/td[7]/div"
    result_ordernumber = "xpath=>//*[@id='app']/div/div/div[2]/div/div[2]/section/div[1]/div[3]/table/tbody/tr/td[3]/div"
    result_transactionnumber = "xpath=>//*[@id='app']/div/div/div[2]/div/div[2]/section/div[1]/div[3]/table/tbody/tr/td[4]/div"
    result_paymentaccountnumber = "xpath=>//*[@id='app']/div/div/div[2]/div/div[2]/section/div[1]/div[3]/table/tbody/tr/td[9]/div"
    result_orderamount = "xpath=>//*[@id='app']/div/div/div[2]/div/div[2]/section/div[1]/div[3]/table/tbody/tr/td[5]/div"
    result_channelsource= "xpath=>//*[@id='app']/div/div/div[2]/div/div[2]/section/div[1]/div[3]/table/tbody/tr/td[12]/div"
    # result_querycriteria = "xpath=>"

    # 断言创建时间查询结果
    def find_result_creationtime(self):
        a = self.get_search_result(self.result_creationtime)
        return a

    # 断言订单状态查询结果
    def find_result_orderstatus(self):
        a = self.get_search_result(self.result_orderstatus)
        return a

    # 断言订单号查询结果
    def find_result_ordernumber(self):
        a = self.get_search_result(self.result_ordernumber)
        return a

    # 断言交易单号查询结果
    def find_result_transactionnumber(self):
        a = self.get_search_result(self.result_transactionnumber)
        return a

    # 断言付款账号查询结果
    def find_result_paymentaccountnumber(self):
        a = self.get_search_result(self.result_paymentaccountnumber)
        return a

    # 断言订单金额（元）查询结果
    def find_result_orderamount(self):
        a = self.get_search_result(self.result_orderamount)
        return a

    # 断言渠道来源查询结果
    def find_result_channelsource(self):
        a = self.get_search_result(self.result_channelsource)
        return a
