# coding = utf-8
from framework.base_page import BasePage


class AdvertPage(BasePage):

    menu_advert = "xpath=>//*[@id='app']/div/div/div[2]/aside/ul/li[3]/div"
    menu_advert_advert = "xpath=>//*[@id='app']/div/div/div[2]/aside/ul/li[3]/ul/li[1]"
    menu_advert_advertSchedule = "xpath=>//*[@id='app']/div/div/div[2]/aside/ul/li[3]/ul/li[2]"
    menu_advert_brandMap = "xpath=>//*[@id='app']/div/div/div[2]/aside/ul/li[3]/ul/li[3]"
    menu_advert_countDown = "xpath=>//*[@id='app']/div/div/div[2]/aside/ul/li[3]/ul/li[4]"
    tab_advert = "xpath=>//*[@id='tab-78']"
    tab_advertSchedule = "xpath=>//*[@id='tab-79']"
    tab_brandMap = "xpath=>//*[@id='tab-131']"
    tab_countDown = "xpath=>//*[@id='tab-135']"

    """
    广告管理各菜单地址及tab页地址
    """

    # 点击广告管理
    def search_click_advert(self):
        self.click(self.menu_advert)

    # 点击广告管理
    def search_click_advert_advert(self):
        self.click(self.menu_advert_advert)

    # 获取广告管理tab名
    def find_tab_advert(self):
        a = self.get_tab_title(self.tab_advert)
        return a

    # 点击广告排期
    def search_click_advert_advertschedule(self):
        self.click(self.menu_advert_advertSchedule)

    # 获取广告排期tab名
    def find_tab_advertschedule(self):
        a = self.get_tab_title(self.tab_advertSchedule)
        return a

    # 点击支付页背景图
    def search_click_advert_brandmap(self):
        self.click(self.menu_advert_brandMap)

    # 获取支付页背景图tab名
    def find_tab_brandmap(self):
        a = self.get_tab_title(self.tab_brandMap)
        return a

    # 点击倒计时页弹窗
    def search_click_advert_countdown(self):
        self.click(self.menu_advert_countDown)

    # 获取倒计时页弹窗tab名
    def find_tab_countdown(self):
        a = self.get_tab_title(self.tab_countDown)
        return a
