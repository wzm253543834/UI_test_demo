# coding = utf-8
from framework.base_page import BasePage


class AreadevicePage(BasePage):

    menu_areadevice = "xpath=>//ul[@class='el-menu-vertical-demo el-menu']/li[1]"
    menu_areadevice_area = "xpath=>//ul[@class='el-menu-vertical-demo el-menu']/li[1]/ul/li[1]"
    menu_areadevice_price = "xpath=>//ul[@class='el-menu-vertical-demo el-menu']/li[1]/ul/li[2]"
    menu_areadevice_devicelist = "xpath=>//ul[@class='el-menu-vertical-demo el-menu']/li[1]/ul/li[3]"
    menu_areadevice_deviceInfo = "xpath=>//ul[@class='el-menu-vertical-demo el-menu']/li[1]/ul/li[4]"
    menu_areadevice_epdevicelist = "xpath=>//ul[@class='el-menu-vertical-demo el-menu']/li[1]/ul/li[5]"
    menu_areadevice_contract = "xpath=>//ul[@class='el-menu-vertical-demo el-menu']/li[1]/ul/li[6]"
    menu_areadevice_place = "xpath=>//ul[@class='el-menu-vertical-demo el-menu']/li[1]/ul/li[7]"
    menu_areadevice_company = "xpath=>//ul[@class='el-menu-vertical-demo el-menu']/li[1]/ul/li[8]"
    tab_area = "xpath=>//*[@id='tab-2']"
    tab_price = "xpath=>//*[@id='tab-3']"
    tab_devicelist = "xpath=>//*[@id='tab-4']"
    tab_deviceInfo = "xpath=>//*[@id='tab-151']"
    tab_epdevicelist = "xpath=>//*[@id='tab-7']"
    tab_contract = "xpath=>//*[@id='tab-109']"
    tab_place = "xpath=>//*[@id='tab-120']"
    tab_company = "xpath=>//*[@id='tab-126']"

    """
    网点设备各菜单地址及tab页地址
    """

    # 点击网点设备
    def search_click_areadevice(self):
        self.click(self.menu_areadevice)

    # 点击网点管理
    def search_click_areadevice_area(self):
        self.click(self.menu_areadevice_area)

    # 获取网点管理tab名
    def find_tab_area(self):
        st = self.get_tab_title(self.tab_area)
        return st

    # 点击价格管理
    def search_click_areadevice_price(self):
        self.click(self.menu_areadevice_price)

    # 获取价格管理tab名
    def find_tab_price(self):
        st = self.get_tab_title(self.tab_price)
        return st

    # 点击设备列表
    def search_click_areadevice_devicelist(self):
        self.click(self.menu_areadevice_devicelist)

    # 获取设备列表tab名
    def find_tab_devicelist(self):
        st = self.get_tab_title(self.tab_devicelist)
        return st

    # 点击设备信息
    def search_click_areadevice_deviceInfo(self):
        self.click(self.menu_areadevice_deviceInfo)

    # 获取设备信息tab名
    def find_tab_deviceInfo(self):
        st = self.get_tab_title(self.tab_deviceInfo)
        return st

    # 点击异常设备列表
    def search_click_areadevice_epdevicelist(self):
        self.click(self.menu_areadevice_epdevicelist)

    # 获取异常设备列表tab名
    def find_tab_epdevicelist(self):
        st = self.get_tab_title(self.tab_epdevicelist)
        return st

    # 点击合同预警
    def search_click_areadevice_contract(self):
        self.click(self.menu_areadevice_contract)

    # 获取合同预警tab名
    def find_tab_contract(self):
        st = self.get_tab_title(self.tab_contract)
        return st

    # 点击场地管理
    def search_click_areadevice_place(self):
        self.click(self.menu_areadevice_place)

    # 获取场地管理tab名
    def find_tab_place(self):
        st = self.get_tab_title(self.tab_place)
        return st

    # 点击分公司管理
    def search_click_areadevice_company(self):
        self.click(self.menu_areadevice_company)

    # 获取分公司管理tab名
    def find_tab_company(self):
        st = self.get_tab_title(self.tab_company)
        return st


class AreaSearch(BasePage):

    area_areaid_search = "xpath=>//*[@id='search_list']/div[1]/div/div/input"
    area_areaname_search = "xpath=>//*[@id='search_list']/div[2]/div/div/input"
    area_companyname_search = "xpath=>//*[@id='search_list']/div[3]/div/div/div/input"
    area_areaenablestatus_search = "xpath=>//*[@id='search_list']/div[4]/div/div/div/input"
    area_besideareastatus_search = "xpath=>//*[@id='search_list']/div[5]/div/div/div/input"
    area_partnername_search = "xpath=>//*[@id='search_list']/div[7]/div/div/input"
    area_devicemodel_search = "xpath=>//*[@id='search_list']/div[8]/div/div/div/input"
    area_partnertype_search = "xpath=>//*[@id='search_list']/div[9]/div/div/div/input"
    area_placename_search = "xpath=>//*[@id='search_list']/div[10]/div/div/input"
    area_iswarehouse_search = "xpath=>//*[@id='search_list']/div[11]/div/div/div/input"
    area_search_button = "xpath=>//*[@id='search_list']/div[6]/div/button"
    area_clear_button = "xpath=>//*[@id='search_list']/div[12]/div/button"
    area_companyname = "xpath=>/html/body/div[2]/div[1]/div[1]/ul/li[7]"
    area_areaenablestatus = "xpath=>/html/body/div[3]/div[1]/div[1]/ul/li[1]"
    area_besideareastatus = "xpath=>/html/body/div[4]/div[1]/div[1]/ul/li[1]"
    area_devicemodel = "xpath=>/html/body/div[5]/div[1]/div[1]/ul/li[1]"
    area_partnertype = "xpath=>/html/body/div[6]/div[1]/div[1]/ul/li[1]"
    area_iswarehouse = "xpath=>/html/body/div[7]/div[1]/div[1]/ul/li[1]"

    """
    网点管理各筛选项
    """

    # 网点ID查询
    def areaid_search(self, text):
        self.type(self.area_areaid_search, text)

    # 网点名称查询
    def areaname_search(self, text):
        self.type(self.area_areaname_search, text)

    # 分公司名称查询
    def companyname_search(self):
        self.click(self.area_companyname_search)
        self.click(self.area_companyname)

    # 网点启用状态查询
    def areaenablestatus_search(self):
        self.click(self.area_areaenablestatus_search)
        self.click(self.area_areaenablestatus)

    # 周边网点状态查询
    def besideareastatus_search(self):
        self.click(self.area_besideareastatus_search)
        self.click(self.area_besideareastatus)

    # 合伙人查询
    def partnername_search(self, text):
        self.type(self.area_partnername_search, text)

    # 设备型号查询
    def devicemodel_search(self):
        self.click(self.area_devicemodel_search)
        self.click(self.area_devicemodel)

    # 合作类型查询
    def partnertype_search(self):
        self.click(self.area_partnertype_search)
        self.click(self.area_partnertype)

    # 场地名称查询
    def placename_search(self, text):
        self.type(self.area_placename_search, text)

    # 是否仓库查询
    def iswarehouse_search(self):
        self.click(self.area_iswarehouse_search)
        self.click(self.area_iswarehouse)

    # 查询按钮
    def search_button_click(self):
        self.click(self.area_search_button)

    # 清空按钮
    def clear_button_click(self):
        self.click(self.area_clear_button)


class PriceSearch(BasePage):

    price_wakeupbodyprice_search = "xpath=>//*[@id='search_list']/div[1]/div/div/input"
    price_passbreathbloodprice_search = "xpath=>//*[@id='search_list']/div[2]/div/div/input"
    price_diastolemeridiansprice_search = "xpath=>//*[@id='search_list']/div[3]/div/div/input"
    price_priceid_search = "xpath=>//*[@id='search_list']/div[4]/div/div/input"
    price_isenable_search = "xpath=>//*[@id='search_list']/div[5]/div/div/div/input"
    price_wakeupbodytime_search = "xpath=>//*[@id='search_list']/div[7]/div/div/input"
    price_passbreathbloodtime_search = "xpath=>//*[@id='search_list']/div[8]/div/div/input"
    price_diastolemeridianstime_search = "xpath=>//*[@id='search_list']/div[9]/div/div/input"
    price_pricename_search = "xpath=>//*[@id='search_list']/div[10]/div/div/input"
    price_search_button = "xpath=>//*[@id='search_list']/div[6]/div/button"
    price_clear_button = "xpath=>//*[@id='search_list']/div[11]/div/button"
    price_isenable = "xpath=>/html/body/div[2]/div[1]/div[1]/ul/li[1]"

    """
    价格管理各筛选项
    """

    # 唤醒身体价格查询
    def wakeupbodyprice_search(self, text):
        self.type(self.price_wakeupbodyprice_search, text)

    # 通行气血价格查询
    def passbreathbloodprice_search(self, text):
        self.type(self.price_passbreathbloodprice_search, text)

    # 舒张筋骨价格查询
    def diastolemeridiansprice_search(self, text):
        self.type(self.price_diastolemeridiansprice_search, text)

    # 价格ID查询
    def priceid_search(self, text):
        self.type(self.price_priceid_search, text)

    # 是否启用查询
    def isenable_search(self):
        self.click(self.price_isenable_search)
        self.click(self.price_isenable)

    # 唤醒身体时长查询
    def wakeupbodytime_search(self, text):
        self.type(self.price_wakeupbodytime_search, text)

    # 通行气血时长查询
    def passbreathbloodtime_search(self, text):
        self.type(self.price_passbreathbloodtime_search, text)

    # 舒张筋骨时长查询
    def diastolemeridianstime_search(self, text):
        self.type(self.price_diastolemeridianstime_search, text)

    # 价格名称查询
    def pricename_search(self, text):
        self.type(self.price_pricename_search, text)

    # 查询按钮
    def search_button_click(self):
        self.click(self.price_search_button)

    # 清空按钮
    def clear_button_click(self):
        self.click(self.price_clear_button)


class DevicelistSearch(BasePage):

    devicelist_deviceid_search = "xpath=>//*[@id='search_list']/div[1]/div/div/input"
    devicelist_devicename_search = "xpath=>//*[@id='search_list']/div[2]/div/div/input"
    devicelist_devicemodel_search = "xpath=>//*[@id='search_list']/div[3]/div/div/div/input"
    devicelist_areaid_search = "xpath=>//*[@id='search_list']/div[4]/div/div/input"
    devicelist_areaname_search = "xpath=>//*[@id='search_list']/div[5]/div/div/input"
    devicelist_partnername_search = "xpath=>//*[@id='search_list']/div[7]/div/div/input"
    devicelist_devicestatus_search = "xpath=>//*[@id='search_list']/div[8]/div/div/div/input"
    devicelist_delivertime_search = "xpath=>//*[@id='search_list']/div[9]/div/div/input[1]"
    devicelist_deviceisenablestatus_search = "xpath=>//*[@id='search_list']/div[10]/div/div/div/input"
    devicelist_movetime_search = "xpath=>//*[@id='search_list']/div[11]/div/div/input"
    devicelist_isinwarehouse_search = "xpath=>//*[@id='search_list']/div[13]/div/div/div/input"
    devicelist_tag_search = "xpath=>//*[@id='search_list']/div[14]/div/div/input"
    devicelist_isscrap_search = "xpath=>//*[@id='search_list']/div[15]/div/div/div/input"
    devicelist_search_button = "xpath=>//*[@id='search_list']/div[6]/div/button"
    devicelist_clear_button = "xpath=>//*[@id='search_list']/div[12]/div/button"
    devicelist_devicemodel = "xpath=>/html/body/div[2]/div[1]/div[1]/ul/li[1]"
    devicelist_devicestatus = "xpath=>/html/body/div[3]/div[1]/div[1]/ul/li[1]"
    devicelist_delivertime = "xpath=>/html/body/div[4]/div[1]/div/div[1]/table/tbody/tr[5]/td[3]"
    devicelist_deviceisenablestatus = "xpath=>/html/body/div[5]/div[1]/div[1]/ul/li[1]"
    devicelist_isinwarehouse = "xpath=>/html/body/div[6]/div[1]/div[1]/ul/li[1]"
    devicelist_isscrap = "xpath=>/html/body/div[7]/div[1]/div[1]/ul/li[1]"

    """
    设备列表各筛选项
    """

    # 设备ID查询
    def deviceid_search(self, text):
        self.type(self.devicelist_deviceid_search, text)

    # 设备名称查询
    def devicename_search(self, text):
        self.type(self.devicelist_devicename_search, text)

    # 设备型号查询
    def devicemodel_search(self):
        self.click(self.devicelist_devicemodel_search)
        self.click(self.devicelist_devicemodel)

    # 网点ID查询
    def areaid_search(self, text):
        self.type(self.devicelist_areaid_search, text)

    # 网点名称查询
    def areaname_search(self, text):
        self.type(self.devicelist_areaname_search, text)

    # 合伙人查询
    def partnername_search(self, text):
        self.type(self.devicelist_partnername_search, text)

    # 设备状态查询
    def devicestatus_search(self):
        self.click(self.devicelist_devicestatus_search)
        self.click(self.devicelist_devicestatus)

    # 发货时间查询
    def delivertime_search(self):
        self.click(self.devicelist_delivertime_search)
        self.click(self.devicelist_delivertime)

    # 设备启用状态查询
    def deviceisenablestatus_search(self):
        self.click(self.devicelist_deviceisenablestatus_search)
        self.click(self.devicelist_deviceisenablestatus)

    # 移机时间（大于）查询
    def movetime_search(self, text):
        self.type(self.devicelist_movetime_search, text)

    # 是否在仓查询
    def isinwarehouse_search(self):
        self.click(self.devicelist_isinwarehouse_search)
        self.click(self.devicelist_isinwarehouse)

    # 标签查询
    def tag_search(self, text):
        self.type(self.devicelist_tag_search, text)

    # 是否报废查询
    def isscrap_search(self):
        self.click(self.devicelist_isscrap_search)
        self.click(self.devicelist_isscrap)

    # 查询按钮
    def search_button_click(self):
        self.click(self.devicelist_search_button)

    # 清空按钮
    def clear_button_click(self):
        self.click(self.devicelist_clear_button)


class DeviceInfoSearch(BasePage):

    deviceInfo_deviceid_search = "xpath=>//*[@id='search_list']/div[1]/div/div/input"
    deviceInfo_devicemodel_search = "xpath=>//*[@id='search_list']/div[2]/div/div/div/input"
    deviceInfo_areaid_search = "xpath=>//*[@id='search_list']/div[3]/div/div/input"
    deviceInfo_areaname_search = "xpath=>//*[@id='search_list']/div[4]/div/div/input"
    deviceInfo_devicestatus_search = "xpath=>//*[@id='search_list']/div[6]/div/div/div/input"
    deviceInfo_isenable_search = "xpath=>//*[@id='search_list']/div[7]/div/div/div/input"
    deviceInfo_simcardnumber_search = "xpath=>//*[@id='search_list']/div[8]/div/div/input"
    deviceInfo_search_button = "xpath=>//*[@id='search_list']/div[5]/div/button"
    deviceInfo_clear_button = "xpath=>//*[@id='search_list']/div[9]/div/button"
    deviceInfo_devicemodel = "xpath=>/html/body/div[2]/div[1]/div[1]/ul/li[1]"
    deviceInfo_devicestatus = "xpath=>/html/body/div[3]/div[1]/div[1]/ul/li[1]"
    deviceInfo_isenable = "xpath=>/html/body/div[4]/div[1]/div[1]/ul/li[1]"

    """
    设备信息各筛选项
    """

    # 设备ID查询
    def deviceid_search(self, text):
        self.type(self.deviceInfo_deviceid_search, text)

    # 设备型号查询
    def devicemodel_search(self):
        self.click(self.deviceInfo_devicemodel_search)
        self.click(self.deviceInfo_devicemodel)

    # 网点ID查询
    def areaid_search(self, text):
        self.type(self.deviceInfo_areaid_search, text)

    # 网点名称查询
    def areaname_search(self, text):
        self.type(self.deviceInfo_areaname_search, text)

    # 设备状态查询
    def devicestatus_search(self):
        self.click(self.deviceInfo_devicestatus_search)
        self.click(self.deviceInfo_devicestatus)

    # 是否启用查询
    def isenable_search(self):
        self.click(self.deviceInfo_isenable_search)
        self.click(self.deviceInfo_isenable)

    # SIM卡号查询
    def simcardnumber_search(self, text):
        self.type(self.deviceInfo_simcardnumber_search, text)

    # 查询按钮
    def search_button_click(self):
        self.click(self.deviceInfo_search_button)

    # 清空按钮
    def clear_button_click(self):
        self.click(self.deviceInfo_clear_button)


class EpdevicelistSearch(BasePage):

    epdevicelist_deviceid_search = "xpath=>//*[@id='search_list']/div[1]/div/div/input"
    epdevicelist_devicename_search = "xpath=>//*[@id='search_list']/div[2]/div/div/input"
    epdevicelist_devicemodel_search = "xpath=>//*[@id='search_list']/div[3]/div/div/div/input"
    epdevicelist_areaid_search = "xpath=>//*[@id='search_list']/div[4]/div/div/input"
    epdevicelist_areaname_search = "xpath=>//*[@id='search_list']/div[5]/div/div/input"
    epdevicelist_partnername_search = "xpath=>//*[@id='search_list']/div[7]/div/div/input"
    epdevicelist_delivertime_search = "xpath=>//*[@id='search_list']/div[8]/div/div/input[1]"
    epdevicelist_search_button = "xpath=>//*[@id='search_list']/div[6]/div/button"
    epdevicelist_clear_button = "xpath=>//*[@id='search_list']/div[9]/div/button"
    epdevicelist_devicemodel = "xpath=>/html/body/div[2]/div[1]/div[1]/ul/li[1]"
    epdevicelist_delivertime = "xpath=>/html/body/div[3]/div[1]/div/div[1]/table/tbody/tr[5]/td[3]"

    """
    异常设备列表各筛选项
    """

    # 设备ID查询
    def deviceid_search(self, text):
        self.type(self.epdevicelist_deviceid_search, text)

    # 设备名称查询
    def devicename_search(self, text):
        self.type(self.epdevicelist_devicename_search, text)

    # 设备型号查询
    def devicemodel_search(self):
        self.click(self.epdevicelist_devicemodel_search)
        self.click(self.epdevicelist_devicemodel)

    # 网点ID查询
    def areaid_search(self, text):
        self.type(self.epdevicelist_areaid_search, text)

    # 网点名称查询
    def areaname_search(self, text):
        self.type(self.epdevicelist_areaname_search, text)

    # 合伙人查询
    def partnername_search(self, text):
        self.type(self.epdevicelist_partnername_search, text)

    # 发货时间查询
    def delivertime_search(self):
        self.click(self.epdevicelist_delivertime_search)
        self.click(self.epdevicelist_delivertime)

    # 查询按钮
    def search_button_click(self):
        self.click(self.epdevicelist_search_button)

    # 清空按钮
    def clear_button_click(self):
        self.click(self.epdevicelist_clear_button)


class ContractSearch(BasePage):

    contract_partnername_search = "xpath=>//*[@id='search_list']/div[1]/div/div/input"
    contract_areaname_search = "xpath=>//*[@id='search_list']/div[2]/div/div/input"
    contract_search_button = "xpath=>//*[@id='search_list']/div[3]/div/button[1]"
    contract_clear_button = "xpath=>//*[@id='search_list']/div[3]/div/button[2]"

    """
    合同预警各筛选项
    """

    # 合伙人查询
    def partnername_search(self, text):
        self.type(self.contract_partnername_search, text)

    # 网点名称查询
    def areaname_search(self, text):
        self.type(self.contract_areaname_search, text)

    # 查询按钮
    def search_button_click(self):
        self.click(self.contract_search_button)

    # 清空按钮
    def clear_button_click(self):
        self.click(self.contract_clear_button)


class PlaceSearch(BasePage):

    place_placeid_search = "xpath=>//*[@id='search_list']/div[1]/div/div/input"
    place_placename_search = "xpath=>//*[@id='search_list']/div[2]/div/div/input"
    place_partnername_search = "xpath=>//*[@id='search_list']/div[3]/div/div/input"
    place_search_button = "xpath=>//*[@id='search_list']/div[4]/div/button[1]"
    place_clear_button = "xpath=>//*[@id='search_list']/div[4]/div/button[2]"

    """
    场地管理各筛选项
    """

    # 场地ID查询
    def placeid_search(self, text):
        self.type(self.place_placeid_search, text)

    # 场地名称查询
    def placename_search(self, text):
        self.type(self.place_placename_search, text)

    # 合伙人查询
    def partnername_search(self, text):
        self.type(self.place_partnername_search, text)

    # 查询按钮
    def search_button_click(self):
        self.click(self.place_search_button)

    # 清空按钮
    def clear_button_click(self):
        self.click(self.place_clear_button)
