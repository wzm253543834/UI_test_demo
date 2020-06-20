# coding = utf-8
from framework.base_page import BasePage


class HomePage(BasePage):

    index_username = "xpath=>//*[@id='app']/section/div[2]/div/form/div[2]/div/div/input"
    index_password = "xpath=>//*[@id='app']/section/div[2]/div/form/div[3]/div/div/input"
    index_enter = "xpath=>//*[@id='app']/section/div[2]/div/form/div[7]/div/div/button"

    def input_username(self, text):
        self.type(self.index_username, text)

    def input_password(self, text):
        self.type(self.index_password, text)

    def enter_lemobar_homepage(self):
        self.click(self.index_enter)

    def login(self):
        self.input_username('wangzm')
        self.input_password('a645765783')
        self.sleep(20)
        self.enter_lemobar_homepage()
        self.sleep(5)
