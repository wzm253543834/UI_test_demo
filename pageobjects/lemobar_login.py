# coding = utf-8
from framework.base_page import BasePage
from framework.verificationcode import VerificationCode


class HomePage(BasePage):

    index_username = "xpath=>//*[@id='app']/section/div[2]/div/form/div[2]/div/div/input"
    index_password = "xpath=>//*[@id='app']/section/div[2]/div/form/div[3]/div/div/input"
    index_code = "xpath=>//*[@id='app']/section/div[2]/div/form/div[5]/div[1]/div/div/input"
    index_code_img = "selector_selector=>#img"
    index_enter = "xpath=>//*[@id='app']/section/div[2]/div/form/div[7]/div/div/button"

    # 清空验证码窗口
    def empty_code(self):
        self.clear(self.index_code)

    # 输入账号
    def input_username(self, text):
        self.type(self.index_username, text)

    # 输入密码
    def input_password(self, text):
        self.type(self.index_password, text)

    # 识别验证码
    def code_find(self):
        vercode = VerificationCode(self.driver)
        code_text = vercode.image_str(self.index_code_img)
        return code_text

    # 输入识别的验证码
    def input_verificationcode(self):
        text = self.code_find()
        self.type(self.index_code, text)

    # 输入验证码
    def input_vcode(self, text):
        self.type(self.index_code, text)

    # 点击登录按钮
    def click_login_button(self):
        self.click(self.index_enter)

    # 账号登录
    def login(self):
        self.input_username('wzm')
        self.input_password('a645765783')
        self.empty_code()
        # self.input_vcode('1111')
        # self.input_verificationcode()
        self.sleep(15)
        self.click_login_button()
        self.sleep(5)
