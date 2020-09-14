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
