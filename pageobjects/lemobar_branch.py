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

    def search_click_branch(self):
        self.click(self.menu_branch)

    def search_click_branch_branch(self):
        self.click(self.menu_branch_branch)

    def find_tab_branch(self):
        st = self.get_tab_title(self.tab_branch)
        return st

    def search_click_branch_price(self):
        self.click(self.menu_branch_price)

    def find_tab_price(self):
        st = self.get_tab_title(self.tab_price)
        return st

    def search_click_branch_equipment(self):
        self.click(self.menu_branch_equipment)

    def find_tab_equipment(self):
        st = self.get_tab_title(self.tab_abequipment)
        return st

    def search_click_branch_equipmessage(self):
        self.click(self.menu_branch_equipmessage)

    def find_tab_equipmessage(self):
        st = self.get_tab_title(self.tab_equipmessage)
        return st

    def search_click_branch_abequipment(self):
        self.click(self.menu_branch_abequipment)

    def find_tab_abequipment(self):
        st = self.get_tab_title(self.tab_abequipment)
        return st

    def search_click_branch_contractwarn(self):
        self.click(self.menu_branch_contractwarn)

    def find_tab_contractwarn(self):
        st = self.get_tab_title(self.tab_contractwarn)
        return st

    def search_click_branch_sitemanage(self):
        self.click(self.menu_branch_sitemanage)

    def find_tab_sitemanage(self):
        st = self.get_tab_title(self.tab_sitemanage)
        return st

    def search_click_branch_officemanage(self):
        self.click(self.menu_branch_officemanage)

    def find_tab_officemanage(self):
        st = self.get_tab_title(self.tab_officemanage)
        return st
