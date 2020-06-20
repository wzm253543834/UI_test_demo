# coding = utf-8
from framework.base_page import BasePage


class BranchPage(BasePage):

    menu_lemobar_branch = "xpath=>//ul[@class='el-menu-vertical-demo el-menu']/li[1]"
    menu_lemobar_branch_branch = "xpath=>//span[text()='网点管理']"
    menu_lemobar_branch_price = "xpath=>//span[text()='价格管理']"

    def search_click_branch(self):
        self.click(self.menu_lemobar_branch)

    def search_click_branch_branch(self):
        self.click(self.menu_lemobar_branch_branch)

    def search_click_branch_price(self):
        self.click(self.menu_lemobar_branch_price)
