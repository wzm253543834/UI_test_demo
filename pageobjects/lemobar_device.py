# coding = utf-8
from framework.base_page import BasePage


class DevicePage(BasePage):

    menu_device = "xpath=>//*[@id='app']/div/div/div[2]/aside/ul/li[4]/div"
    menu_device_deviceBatch = "//*[@id='app']/div/div/div[2]/aside/ul/li[4]/ul/li[1]"
    menu_device_deviceFactory = "xpath=>//*[@id='app']/div/div/div[2]/aside/ul/li[4]/ul/li[2]"
    menu_device_deviceCustomer = "xpath=>//*[@id='app']/div/div/div[2]/aside/ul/li[4]/ul/li[3]"
    menu_device_deviceType = "xpath=>//*[@id='app']/div/div/div[2]/aside/ul/li[4]/ul/li[4]"
    tab_deviceBatch = "xpath=>//*[@id='tab-35']"
    tab_deviceFactory = "xpath=>//*[@id='tab-94']"
    tab_deviceCustomer = "xpath=>//*[@id='tab-38']"
    tab_deviceType = "xpath=>//*[@id='tab-39']"

    """
    设备管理各菜单地址及tab页地址
    """

    # 点击设备管理
    def search_click_divice(self):
        self.click(self.menu_device)

    # 点击设备批次
    def search_click_divice_devicebatch(self):
        self.click(self.menu_device_deviceBatch)

    # 获取设备批次tab名
    def find_tab_devicebatch(self):
        a = self.get_tab_title(self.tab_deviceBatch)
        return a

    # 点击设备工厂
    def search_click_divice_devicefactory(self):
        self.click(self.menu_device_deviceFactory)

    # 获取设备工厂tab名
    def find_tab_devicefactory(self):
        a = self.get_tab_title(self.tab_deviceFactory)
        return a

    # 点击客户数据
    def search_click_divice_devicecstomer(self):
        self.click(self.menu_device_deviceCustomer)

    # 获取客户数据tab名
    def find_tab_devicecustomer(self):
        a = self.get_tab_title(self.tab_deviceCustomer)
        return a

    # 点击设备型号
    def search_click_divice_devicetype(self):
        self.click(self.menu_device_deviceType )

    # 获取设备型号tab名
    def find_tab_devicetype(self):
        a = self.get_tab_title(self.tab_deviceType )
        return a


class DeviceBatchSearch(BasePage):

    deviceBatch_batchname_search = "xpath=>//*[@id='search_list']/div[1]/div/div/input"
    deviceBatch_batchid_search = "xpath=>//*[@id='search_list']/div[2]/div/div/input"
    deviceBatch_factoryname_search = "xpath=>//*[@id='search_list']/div[3]/div/div/input"
    deviceBatch_devicetypename_search = "xpath=>//*[@id='search_list']/div[4]/div/div/input"
    deviceBatch_customername_search = "xpath=>//*[@id='search_list']/div[5]/div/div/input"
    deviceBatch_search_button = "xpath=>//*[@id='search_list']/div[6]/div/button[1]"
    deviceBatch_empty_button = "xpath=>//*[@id='search_list']/div[6]/div/button[2]"

    """
    设备批次各筛选项
    """

    # 批次名称查询
    def batchname_search(self, text):
        self.type(self.deviceBatch_batchid_search, text)

    # 批次ID查询
    def batchid_search(self, text):
        self.type(self.deviceBatch_factoryname_search, text)

    # 工厂名称查询
    def factoryname_search(self, text):
        self.type(self.deviceBatch_factoryname_search, text)

    # 设备类型名称查询
    def devicetypename_search(self, text):
        self.type(self.deviceBatch_devicetypename_search, text)

    # 客户名称查询
    def customername_search(self, text):
        self.type(self.deviceBatch_customername_search, text)

    # 查询按钮
    def search_button_click(self):
        self.click(self.deviceBatch_search_button)

    # 清空按钮
    def empty_button_click(self):
        self.click(self.deviceBatch_empty_button)

    # 测试结果断言
    result_batchname = "xpath=>//*[@id='app']/div/div/div[2]/div/div[2]/section/div[1]/div[3]/table/tbody/tr/td[2]/div"
    result_batchid = "xpath=>//*[@id='app']/div/div/div[2]/div/div[2]/section/div[1]/div[3]/table/tbody/tr/td[3]/div"
    result_factoryname = "xpath=>//*[@id='app']/div/div/div[2]/div/div[2]/section/div[1]/div[3]/table/tbody/tr/td[5]/div"
    result_devicetypename = "xpath=>//*[@id='app']/div/div/div[2]/div/div[2]/section/div[1]/div[3]/table/tbody/tr/td[6]/div"
    result_customername = "xpath=>//*[@id='app']/div/div/div[2]/div/div[2]/section/div[1]/div[3]/table/tbody/tr/td[7]/div"

    # 批次名称查询结果
    def find_result_batchname(self):
        a = self.get_search_result(self.result_batchname)
        return a

    # 批次ID查询结果
    def find_result_batchid(self):
        a = self.get_search_result(self.result_batchid)
        return a

    # 工厂名称查询结果
    def find_result_factoryname(self):
        a = self.get_search_result(self.result_factoryname)
        return a

    # 设备类型名称查询结果
    def find_result_devicetypename(self):
        a = self.get_search_result(self.result_devicetypename)
        return a

    # 客户名称查询结果
    def find_result_customername(self):
        a = self.get_search_result(self.result_customername)
        return a
