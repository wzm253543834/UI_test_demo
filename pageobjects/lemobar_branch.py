# coding = utf-8
from framework.base_page import BasePage


class BranchPage(BasePage):

    menu_branch = "xpath=>//ul[@class='el-menu-vertical-demo el-menu']/li[1]"
    menu_branch_branch = "xpath=>//ul[@class='el-menu-vertical-demo el-menu']/li[1]/ul/li[1]"
    menu_branch_price = "xpath=>//ul[@class='el-menu-vertical-demo el-menu']/li[1]/ul/li[2]"
    menu_branch_equipment = "xpath=>//ul[@class='el-menu-vertical-demo el-menu']/li[1]/ul/li[3]"
    menu_branch_equipmessage = "xpath=>//ul[@class='el-menu-vertical-demo el-menu']/li[1]/ul/li[4]"
    menu_branch_abequipment = "xpath=>//ul[@class='el-menu-vertical-demo el-menu']/li[1]/ul/li[5]"
    menu_branch_contractwarn = "xpath=>//ul[@class='el-menu-vertical-demo el-menu']/li[1]/ul/li[6]"
    menu_branch_sitemanage = "xpath=>//ul[@class='el-menu-vertical-demo el-menu']/li[1]/ul/li[7]"
    menu_branch_officemanage = "xpath=>//ul[@class='el-menu-vertical-demo el-menu']/li[1]/ul/li[8]"
    tab_branch = "xpath=>//*[@id='tab-2']"
    tab_price = "xpath=>//*[@id='tab-3']"
    tab_equipment = "xpath=>//*[@id='tab-4']"
    tab_equipmessage = "xpath=>//*[@id='tab-151']"
    tab_abequipment = "xpath=>//*[@id='tab-7']"
    tab_contractwarn = "xpath=>//*[@id='tab-109']"
    tab_sitemanage = "xpath=>//*[@id='tab-120']"
    tab_officemanage = "xpath=>//*[@id='tab-126']"

    """
    网点设备各菜单地址及tab页地址
    """

    # 点击网点设备
    def search_click_branch(self):
        self.click(self.menu_branch)

    # 点击网点管理
    def search_click_branch_branch(self):
        self.click(self.menu_branch_branch)

    # 获取网点管理tab名
    def find_tab_branch(self):
        st = self.get_tab_title(self.tab_branch)
        return st

    # 点击价格管理
    def search_click_branch_price(self):
        self.click(self.menu_branch_price)

    # 获取价格管理tab名
    def find_tab_price(self):
        st = self.get_tab_title(self.tab_price)
        return st

    # 点击设备列表
    def search_click_branch_equipment(self):
        self.click(self.menu_branch_equipment)

    # 获取设备列表tab名
    def find_tab_equipment(self):
        st = self.get_tab_title(self.tab_equipment)
        return st

    # 点击设备信息
    def search_click_branch_equipmessage(self):
        self.click(self.menu_branch_equipmessage)

    # 获取设备信息tab名
    def find_tab_equipmessage(self):
        st = self.get_tab_title(self.tab_equipmessage)
        return st

    # 点击异常设备列表
    def search_click_branch_abequipment(self):
        self.click(self.menu_branch_abequipment)

    # 获取异常设备列表tab名
    def find_tab_abequipment(self):
        st = self.get_tab_title(self.tab_abequipment)
        return st

    # 点击合同预警
    def search_click_branch_contractwarn(self):
        self.click(self.menu_branch_contractwarn)

    # 获取合同预警tab名
    def find_tab_contractwarn(self):
        st = self.get_tab_title(self.tab_contractwarn)
        return st

    # 点击场地管理
    def search_click_branch_sitemanage(self):
        self.click(self.menu_branch_sitemanage)

    # 获取场地管理tab名
    def find_tab_sitemanage(self):
        st = self.get_tab_title(self.tab_sitemanage)
        return st

    # 点击分公司管理
    def search_click_branch_officemanage(self):
        self.click(self.menu_branch_officemanage)

    # 获取分公司管理tab名
    def find_tab_officemanage(self):
        st = self.get_tab_title(self.tab_officemanage)
        return st


class BranchSearch(BasePage):

    branch_branchid_search = "xpath=>//*[@id='search_list']/div[1]/div/div/input"
    branch_branchname_search = "xpath=>//*[@id='search_list']/div[2]/div/div/input"
    branch_officename_search = "xpath=>//*[@id='search_list']/div[3]/div/div/div/input"
    branch_branchenablestatus_search = "xpath=>//*[@id='search_list']/div[4]/div/div/div/input"
    branch_besidebranchstatus_search = "xpath=>//*[@id='search_list']/div[5]/div/div/div/input"
    branch_partnername_search = "xpath=>//*[@id='search_list']/div[7]/div/div/input"
    branch_equipmentmodel_search = "xpath=>//*[@id='search_list']/div[8]/div/div/div/input"
    branch_partnertype_search = "xpath=>//*[@id='search_list']/div[9]/div/div/div/input"
    branch_sitename_search = "xpath=>//*[@id='search_list']/div[10]/div/div/input"
    branch_iswarehouse_search = "xpath=>//*[@id='search_list']/div[11]/div/div/div/input"
    branch_search_button = "xpath=>//*[@id='search_list']/div[6]/div/button"
    branch_clear_button = "xpath=>//*[@id='search_list']/div[12]/div/button"
    branch_officename_fuzhou = "xpath=>/html/body/div[2]/div[1]/div[1]/ul/li[7]"
    branch_branchenablestatus = "xpath=>/html/body/div[3]/div[1]/div[1]/ul/li[1]"
    branch_besidebranchstatus = "xpath=>/html/body/div[4]/div[1]/div[1]/ul/li[1]"
    branch_equipmentmodel = "xpath=>/html/body/div[5]/div[1]/div[1]/ul/li[1]"
    branch_partnertype = "xpath=>/html/body/div[6]/div[1]/div[1]/ul/li[1]"
    branch_iswarehouse = "xpath=>/html/body/div[7]/div[1]/div[1]/ul/li[1]"

    """
    网点管理各筛选项
    """

    # 网点ID查询
    def branchid_search(self, text):
        self.type(self.branch_branchid_search, text)

    # 网点名称查询
    def branchname_search(self, text):
        self.type(self.branch_branchname_search, text)

    # 分公司名称查询
    def officename_search(self):
        self.click(self.branch_officename_search)
        self.click(self.branch_officename_fuzhou)

    # 网点启用状态查询
    def branchenablestatus_search(self):
        self.click(self.branch_branchenablestatus_search)
        self.click(self.branch_branchenablestatus)

    # 周边网点状态查询
    def besidebranchstatus_search(self):
        self.click(self.branch_besidebranchstatus_search)
        self.click(self.branch_besidebranchstatus)

    # 合伙人查询
    def partnername_search(self, text):
        self.type(self.branch_partnername_search, text)

    # 设备型号查询
    def equipmentmodel_search(self):
        self.click(self.branch_equipmentmodel_search)
        self.click(self.branch_equipmentmodel)

    # 合作类型查询
    def partnertype_search(self):
        self.click(self.branch_partnertype_search)
        self.click(self.branch_partnertype)

    # 场地名称查询
    def sitename_search(self, text):
        self.type(self.branch_sitename_search, text)

    # 是否仓库查询
    def iswarehouse_search(self):
        self.click(self.branch_iswarehouse_search)
        self.click(self.branch_iswarehouse)

    # 查询按钮
    def search_button_click(self):
        self.click(self.branch_search_button)

    # 清空按钮
    def clear_button_click(self):
        self.click(self.branch_clear_button)


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

    # 价格id查询
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


class EquipmentSearch(BasePage):

    equipment_equipmentid_search = "xpath=>//*[@id='search_list']/div[1]/div/div/input"
    equipment_equipmentname_search = "xpath=>//*[@id='search_list']/div[2]/div/div/input"
    equipment_equipmentmodel_search = "xpath=>//*[@id='search_list']/div[3]/div/div/div/input"
    equipment_branchid_search = "xpath=>//*[@id='search_list']/div[4]/div/div/input"
    equipment_branchname_search = "xpath=>//*[@id='search_list']/div[5]/div/div/input"
    equipment_partnername_search = "xpath=>//*[@id='search_list']/div[7]/div/div/input"
    equipment_equipmentstatus_search = "xpath=>//*[@id='search_list']/div[8]/div/div/div/input"
    equipment_delivertime_search = "xpath=>//*[@id='search_list']/div[9]/div/div/input[1]"
    equipment_equipmentisenablestatus_search = "xpath=>//*[@id='search_list']/div[10]/div/div/div/input"
    equipment_movetime_search = "xpath=>//*[@id='search_list']/div[11]/div/div/input"
    equipment_isinwarehouse_search = "xpath=>//*[@id='search_list']/div[13]/div/div/div/input"
    equipment_tag_search = "xpath=>//*[@id='search_list']/div[14]/div/div/input"
    equipment_isscrap_search = "xpath=>//*[@id='search_list']/div[15]/div/div/div/input"
    equipment_search_button = "xpath=>//*[@id='search_list']/div[6]/div/button"
    equipment_clear_button = "xpath=>//*[@id='search_list']/div[12]/div/button"
    equipment_equipmentmodel = "xpath=>/html/body/div[2]/div[1]/div[1]/ul/li[1]"
    equipment_equipmentstatus = "xpath=>/html/body/div[3]/div[1]/div[1]/ul/li[1]"
    equipment_delivertime = "xpath=>/html/body/div[4]/div[1]/div/div[1]/table/tbody/tr[5]/td[3]"
    equipment_equipmentisenablestatus = "xpath=>/html/body/div[5]/div[1]/div[1]/ul/li[1]"
    equipment_isinwarehouse = "xpath=>/html/body/div[6]/div[1]/div[1]/ul/li[1]"
    equipment_isscrap = "xpath=>/html/body/div[7]/div[1]/div[1]/ul/li[1]"

    """
    设备列表各筛选项
    """

    # 设备ID查询
    def equipmentid_search(self, text):
        self.type(self.equipment_equipmentid_search, text)

    # 设备名称查询
    def equipmentname_search(self, text):
        self.type(self.equipment_equipmentname_search, text)

    # 设备型号查询
    def equipmentmodel_search(self):
        self.click(self.equipment_equipmentmodel_search)
        self.click(self.equipment_equipmentmodel)

    # 网点ID查询
    def branchid_search(self, text):
        self.type(self.equipment_branchid_search, text)

    # 网点名称查询
    def branchname_search(self, text):
        self.type(self.equipment_branchname_search, text)

    # 合伙人查询
    def partnername_search(self, text):
        self.type(self.equipment_partnername_search, text)

    # 设备状态查询
    def equipmentstatus_search(self):
        self.click(self.equipment_equipmentstatus_search)
        self.click(self.equipment_equipmentstatus)

    # 发货时间查询
    def delivertime_search(self):
        self.click(self.equipment_delivertime_search)
        self.click(self.equipment_delivertime)

    # 设备启用状态查询
    def equipmentisenablestatus_search(self):
        self.click(self.equipment_equipmentisenablestatus_search)
        self.click(self.equipment_equipmentisenablestatus)

    # 移机时间（大于）查询
    def movetime_search(self, text):
        self.type(self.equipment_movetime_search, text)

    # 是否在仓查询
    def isinwarehouse_search(self):
        self.click(self.equipment_isinwarehouse_search)
        self.click(self.equipment_isinwarehouse)

    # 标签查询
    def tag_search(self, text):
        self.type(self.equipment_tag_search, text)

    # 是否报废查询
    def isscrap_search(self):
        self.click(self.equipment_isscrap_search)
        self.click(self.equipment_isscrap)

    # 查询按钮
    def search_button_click(self):
        self.click(self.equipment_search_button)

    # 清空按钮
    def clear_button_click(self):
        self.click(self.equipment_clear_button)


class EquipmessageSearch(BasePage):

    equipmessage_equipmentid_search = "xpath=>//*[@id='search_list']/div[1]/div/div/input"
    equipmessage_equipmentmodel_search = "xpath=>//*[@id='search_list']/div[2]/div/div/div/input"
    equipmessage_branchid_search = "xpath=>//*[@id='search_list']/div[3]/div/div/input"
    equipmessage_branchname_search = "xpath=>//*[@id='search_list']/div[4]/div/div/input"
    equipmessage_equipmentstatus_search = "xpath=>//*[@id='search_list']/div[6]/div/div/div/input"
    equipmessage_isenable_search = "xpath=>//*[@id='search_list']/div[7]/div/div/div/input"
    equipmessage_simcardnumber_search = "xpath=>//*[@id='search_list']/div[8]/div/div/input"
    equipmessage_search_button = "xpath=>//*[@id='search_list']/div[5]/div/button"
    equipmessage_clear_button = "xpath=>//*[@id='search_list']/div[9]/div/button"
    equipmessage_equipmentmodel = "xpath=>/html/body/div[2]/div[1]/div[1]/ul/li[1]"
    equipmessage_equipmentstatus = "xpath=>/html/body/div[3]/div[1]/div[1]/ul/li[1]"
    equipmessage_isenable = "xpath=>/html/body/div[4]/div[1]/div[1]/ul/li[1]"

    """
    设备信息各筛选项
    """

    # 设备ID查询
    def equipmentid_search(self, text):
        self.type(self.equipmessage_branchid_search, text)

    # 设备型号查询
    def equipmentmodel_search(self):
        self.click(self.equipmessage_equipmentmodel_search)
        self.click(self.equipmessage_equipmentmodel)

    # 网点ID查询
    def branchid_search(self, text):
        self.type(self.equipmessage_branchid_search, text)

    # 网点名称查询
    def branchname_search(self, text):
        self.type(self.equipmessage_branchname_search, text)

    # 设备状态查询
    def equipmentstatus_search(self):
        self.click(self.equipmessage_equipmentstatus_search)
        self.click(self.equipmessage_equipmentstatus)

    # 是否启用查询
    def isenable_search(self):
        self.click(self.equipmessage_isenable_search)
        self.click(self.equipmessage_isenable)

    # SIM卡号查询
    def simcardnumber_search(self, text):
        self.type(self.equipmessage_simcardnumber_search, text)

    # 查询按钮
    def search_button_click(self):
        self.click(self.equipmessage_search_button)

    # 清空按钮
    def clear_button_click(self):
        self.click(self.equipmessage_clear_button)


class AbequipmentSearch(BasePage):

    abequipment_equipmentid_search = "xpath=>//*[@id='search_list']/div[1]/div/div/input"
    abequipment_equipmentname_search = "xpath=>//*[@id='search_list']/div[2]/div/div/input"
    abequipment_equipmentmodel_search = "xpath=>//*[@id='search_list']/div[3]/div/div/div/input"
    abequipment_branchid_search = "xpath=>//*[@id='search_list']/div[4]/div/div/input"
    abequipment_branchname_search = "xpath=>//*[@id='search_list']/div[5]/div/div/input"
    abequipment_partnername_search = "xpath=>//*[@id='search_list']/div[7]/div/div/input"
    abequipment_delivertime_search = "xpath=>//*[@id='search_list']/div[8]/div/div/input[1]"
    abequipment_search_button = "xpath=>//*[@id='search_list']/div[6]/div/button"
    abequipment_clear_button = "xpath=>//*[@id='search_list']/div[9]/div/button"
    abequipment_equipmentmodel = "xpath=>/html/body/div[2]/div[1]/div[1]/ul/li[1]"
    abequipment_delivertime = "xpath=>/html/body/div[3]/div[1]/div/div[1]/table/tbody/tr[5]/td[3]"

    """
    异常设备列表各筛选项
    """

    # 设备ID查询
    def equipmentid_search(self, text):
        self.type(self.abequipment_equipmentid_search, text)

    # 设备名称查询
    def equipmentname_search(self, text):
        self.type(self.abequipment_equipmentname_search, text)

    # 设备型号查询
    def equipmentmodel_search(self):
        self.click(self.abequipment_equipmentmodel_search)
        self.click(self.abequipment_equipmentmodel)

    # 网点ID查询
    def branchid_search(self, text):
        self.type(self.abequipment_branchid_search, text)

    # 网点名称查询
    def branchname_search(self, text):
        self.type(self.abequipment_branchname_search, text)

    # 合伙人查询
    def partnername_search(self, text):
        self.type(self.abequipment_partnername_search, text)

    # 发货时间查询
    def delivertime_search(self):
        self.click(self.abequipment_delivertime_search)
        self.click(self.abequipment_delivertime)

    # 查询按钮
    def search_button_click(self):
        self.click(self.abequipment_search_button)

    # 清空按钮
    def clear_button_click(self):
        self.click(self.abequipment_clear_button)
