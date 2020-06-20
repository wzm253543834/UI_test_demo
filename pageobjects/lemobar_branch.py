# coding = utf-8
from framework.base_page import BasePage


class BranchPage(BasePage):

    menu_lemobar_branch = "xpath=>//ul[@class='el-menu-vertical-demo el-menu']/li[1]"
    menu_lemobar_branch_branch = "xpath=>//span[text()='网点管理']"
    menu_lemobar_branch_price = "xpath=>//span[text()='价格管理']"
    menu_lemobar_branch_equipment = "xpath=>//span[text()='设备管理']"
    menu_lemobar_branch_equipmessage = "xpath=>//span[text()='设备信息']"
    menu_lemobar_branch_abequipment = "xpath=>//span[text()='异常设备管理']"
    menu_lemobar_branch_contractwarn = "xpath=>//span[text()='合同预警']"
    menu_lemobar_branch_sitemanage = "xpath=>//span[text()='场地管理']"
    menu_lemobar_branch_officemanage = "xpath=>//span[text()='分公司管理']"

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
