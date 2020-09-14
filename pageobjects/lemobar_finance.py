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
