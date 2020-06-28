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

    def search_click_pay(self):
        self.click(self.menu_pay)

