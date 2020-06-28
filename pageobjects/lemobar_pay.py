# coding = utf-8
from framework.base_page import BasePage


class PayPage(BasePage):

    menu_pay = "xpath=>//*[@id='app']/div/div/div[2]/aside/ul/li[2]/div"
    menu_pay_basepayment = "xpath=>//*[@id='app']/div/div/div[2]/aside/ul/li[2]/ul/li[1]"
    menu_pay_payment = "xpath=>//*[@id='app']/div/div/div[2]/aside/ul/li[2]/ul/li[2]"
    tab_basepayment = "xpath=>//*[@id='tab-10']"
    tab_payment = "xpath=>//*[@id='tab-11']"

    """
    支付管理各菜单地址及tab页地址
    """

    # 点击支付管理
    def search_click_pay(self):
        self.click(self.menu_pay)

    # 点击基础支付类型
    def search_click_pay_basepayment(self):
        self.click(self.menu_pay_basepayment)

    # 获取基础支付类型tab名
    def find_tab_basepayment(self):
        st = self.get_tab_title(self.tab_basepayment)
        return st

    # 点击支付组管理
    def search_click_pay_payment(self):
        self.click(self.menu_pay_payment)

    # 获取支付组管理tab名
    def find_tab_payment(self):
        st = self.get_tab_title(self.tab_payment)
        return st
