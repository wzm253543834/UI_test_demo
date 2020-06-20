# coding = utf-8
from framework.base_page import BasePage


class BranchPage(BasePage):

    menu_lemobar_branch = "xpath=>//ul[@class='el-menu-vertical-demo el-menu']/li[1]"
    menu_lemobar_branch_branch = "xpath=>//ul[@class='el-menu-vertical-demo el-menu']/li[1]/ul/li[1]"
    menu_lemobar_branch_price = "xpath=>//ul[@class='el-menu-vertical-demo el-menu']/li[1]/ul/li[2]"
    menu_lemobar_branch_equipment = "xpath=>//ul[@class='el-menu-vertical-demo el-menu']/li[1]/ul/li[3]"
    menu_lemobar_branch_equipmessage = "xpath=>//ul[@class='el-menu-vertical-demo el-menu']/li[1]/ul/li[4]"
    menu_lemobar_branch_abequipment = "xpath=>//ul[@class='el-menu-vertical-demo el-menu']/li[1]/ul/li[5]"
    menu_lemobar_branch_contractwarn = "xpath=>//ul[@class='el-menu-vertical-demo el-menu']/li[1]/ul/li[6]"
    menu_lemobar_branch_sitemanage = "xpath=>//ul[@class='el-menu-vertical-demo el-menu']/li[1]/ul/li[7]"
    menu_lemobar_branch_officemanage = "xpath=>//ul[@class='el-menu-vertical-demo el-menu']/li[1]/ul/li[8]"
    lemobar_tab_branch = "xpath=>//*[@id='tab-2']"

    def find_tab_branch(self):
        self.get_tab_title(self.lemobar_tab_branch)

    def search_click_branch(self):
        self.click(self.menu_lemobar_branch)

    def search_click_branch_branch(self):
        self.click(self.menu_lemobar_branch_branch)

    def search_click_branch_price(self):
        self.click(self.menu_lemobar_branch_price)

    def search_click_branch_equipment(self):
        self.click(self.menu_lemobar_branch_equipment)

    def search_click_branch_equipmessage(self):
        self.click(self.menu_lemobar_branch_equipmessage)

    def search_click_branch_abequipment(self):
        self.click(self.menu_lemobar_branch_abequipment)

    def search_click_branch_contractwarn(self):
        self.click(self.menu_lemobar_branch_contractwarn)

    def search_click_branch_sitemanage(self):
        self.click(self.menu_lemobar_branch_sitemanage)

    def search_click_branch_officemanage(self):
        self.click(self.menu_lemobar_branch_officemanage)
