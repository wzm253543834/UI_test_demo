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
        a = self.get_tab_title(self.tab_basepayment)
        return a

    # 点击支付组管理
    def search_click_pay_payment(self):
        self.click(self.menu_pay_payment)

    # 获取支付组管理tab名
    def find_tab_payment(self):
        a = self.get_tab_title(self.tab_payment)
        return a


class BasepaymentSearch(BasePage):

    basepayment_id_search = "xpath=>//*[@id='search_list']/div[1]/div/div/input"
    basepayment_typename_search = "xpath=>//*[@id='search_list']/div[2]/div/div/input"
    basepayment_isenable_search = "xpath=>//*[@id='search_list']/div[3]/div/div/div/input"
    basepayment_search_button = "xpath=>//*[@id='search_list']/div[4]/div/button[1]"
    basepayment_empty_button = "xpath=>//*[@id='search_list']/div[4]/div/button[2]"
    basepayment_isenable = "xpath=>/html/body/div[2]/div[1]/div[1]/ul/li[1]"

    """
    基础支付类型各筛选项
    """

    # ID查询
    def id_search(self, text):
        self.type(self.basepayment_id_search, text)

    # 类型名称查询
    def typename_search(self, text):
        self.type(self.basepayment_typename_search, text)

    # 是否启用查询
    def isenable_search(self):
        self.click(self.basepayment_isenable_search)
        self.sleep(2)
        self.click(self.basepayment_isenable)

    # 查询按钮
    def search_button_click(self):
        self.click(self.basepayment_search_button)

    # 清空按钮
    def empty_button_click(self):
        self.click(self.basepayment_empty_button)

    # 测试结果断言
    result_id = "xpath=>//*[@id='app']/div/div/div[2]/div/div[2]/section/div[1]/div[3]/table/tbody/tr/td[2]/div"
    result_typename = "xpath=>//*[@id='app']/div/div/div[2]/div/div[2]/section/div[1]/div[3]/table/tbody/tr/td[3]/div"
    result_isenable = "xpath=>//*[@id='app']/div/div/div[2]/div/div[2]/section/div[1]/div[3]/table/tbody/tr/td[8]/div/i"

    # 断言ID查询结果
    def find_result_id(self):
        a = self.get_search_result(self.result_id)
        return a

    # 断言类型名称查询结果
    def find_result_typename(self):
        a = self.get_search_result(self.result_typename)
        return a

    # 断言是否启用查询结果
    def find_result_isenable(self):
        a = self.get_search_result_icon(self.result_isenable)
        return a


class PaymentSearch(BasePage):

    payment_paymentid_search = "xpath=>//*[@id='search_list']/div[1]/div/div/input"
    payment_paymentname_search = "xpath=>//*[@id='search_list']/div[2]/div/div/input"
    payment_isenable_search = "xpath=>//*[@id='search_list']/div[3]/div/div/div[1]/input"
    payment_search_button = "xpath=>//*[@id='search_list']/div[4]/div/button[1]"
    payment_empty_button = "xpath=>//*[@id='search_list']/div[4]/div/button[2]"
    payment_isenable = "xpath=>/html/body/div[2]/div[1]/div[1]/ul/li[1]"

    """
    支付组管理各筛选项
    """

    # 支付组ID查询
    def paymentid_search(self, text):
        self.type(self.payment_paymentid_search, text)

    # 支付组名称查询
    def paymentname_search(self, text):
        self.type(self.payment_paymentname_search, text)

    # 是否启用查询
    def isenable_search(self):
        self.click(self.payment_isenable_search)
        self.sleep(2)
        self.click(self.payment_isenable)

    # 查询按钮
    def search_button_click(self):
        self.click(self.payment_search_button)

    # 清空按钮
    def empty_button_click(self):
        self.click(self.payment_empty_button)

    # 测试结果断言
    result_paymentid = "xpath=>//*[@id='app']/div/div/div[2]/div/div[2]/section/div[1]/div[3]/table/tbody/tr/td[2]/div"
    result_paymentname = "xpath=>//*[@id='app']/div/div/div[2]/div/div[2]/section/div[1]/div[3]/table/tbody/tr/td[3]/div"
    result_isenable = "xpath=>//*[@id='app']/div/div/div[2]/div/div[2]/section/div[1]/div[3]/table/tbody/tr/td[5]/div/i"

    # 断言支付组ID查询结果
    def find_result_paymentid(self):
        a = self.get_search_result(self.result_paymentid)
        return a

    # 断言支付组名称查询结果
    def find_result_paymentname(self):
        a = self.get_search_result(self.result_paymentname)
        return a

    # 断言是否启用查询结果
    def find_result_isenable(self):
        a = self.get_search_result_icon(self.result_isenable)
        return a
