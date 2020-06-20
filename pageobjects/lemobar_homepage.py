# coding=utf-8
from framework.base_page import BasePage


class HomePage(BasePage):

    index_username = "xpath=>//*[@id='app']/section/div[2]/div/form/div[2]/div/div/input"
    index_password = "xpath=>//*[@id='app']/section/div[2]/div/form/div[3]/div/div/input"
    index_enter = "xpath=>//*[@id='app']/section/div[2]/div/form/div[7]/div/div/button"
    menu_lemobar_branch = "xpath=>//ul[@class='el-menu-vertical-demo el-menu']/li[1]"
    menu_lemobar_branch_branch = "xpath=>//span[text()='网点管理']"
    menu_lemobar_branch_price = "xpath=>//span[text()='价格管理']"

    def input_username(self, text):
        self.type(self.index_username, text)

    def input_password(self, text):
        self.type(self.index_password, text)

    def enter_homepage(self):
        self.click(self.index_enter)

    def search_click_branch(self):
        self.click(self.menu_lemobar_branch)

    def search_click_branch_branch(self):
        self.click(self.menu_lemobar_branch_branch)
