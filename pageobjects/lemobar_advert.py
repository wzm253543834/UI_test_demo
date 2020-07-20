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


class AdvertSearch(BasePage):

    advert_advertid_search = "xpath=>//*[@id='search_list']/div[1]/div/div/input"
    advert_adverttitle_search = "xpath=>//*[@id='search_list']/div[2]/div/div/input"
    advert_isenable_search = "xpath=>//*[@id='search_list']/div[3]/div/div/div[1]/input"
    advert_search_button = "xpath=>//*[@id='search_list']/div[4]/div/button[1]"
    advert_click_button = "xpath=>//*[@id='search_list']/div[4]/div/button[2]"
    advert_isenable = "xpath=>/html/body/div[2]/div[1]/div[1]/ul/li[1]"

    """
    广告管理各筛选项
    """

    # 广告ID查询
    def advertid_search(self, text):
        self.type(self.advert_advertid_search, text)

    # 广告标题查询
    def adverttitle_search(self, text):
        self.type(self.advert_adverttitle_search, text)

    # 是否启用查询
    def isenable_search(self):
        self.click(self.advert_isenable_search)
        self.sleep(2)
        self.click(self.advert_isenable)

    # 查询按钮
    def search_button_click(self):
        self.click(self.advert_search_button)

    # 清空按钮
    def click_button_click(self):
        self.click(self.advert_click_button)

    # 测试结果断言
    result_advertid = "xpath=>//*[@id='app']/div/div/div[2]/div/div[2]/section/div[1]/div[3]/table/tbody/tr/td[2]/div"
    result_adverttitle = "xpath=>//*[@id='app']/div/div/div[2]/div/div[2]/section/div[1]/div[3]/table/tbody/tr/td[3]/div"
    result_isenable = "xpath=>//*[@id='app']/div/div/div[2]/div/div[2]/section/div[1]/div[3]/table/tbody/tr/td[6]/div/i"

    # 断言广告ID查询结果
    def find_result_advertid(self):
        a = self.get_search_result(self.result_advertid)
        return a

    # 断言广告标题查询结果
    def find_result_adverttitle(self):
        a = self.get_search_result(self.result_adverttitle)
        return a

    # 断言是否启用查询结果
    def find_result_isenable(self):
        a = self.get_search_result_icon(self.result_isenable)
        return a


class AdvertScheduleSearch(BasePage):

    advertSchedule_begintime_search = "xpath=>//*[@id='search_list']/div[1]/div/div/input"
    advertSchedule_endtime_search = "xpath=>//*[@id='search_list']/div[2]/div/div/input"
    advertSchedule_areaid_search = "xpath=>//*[@id='search_list']/div[3]/div/div/input"
    advertSchedule_areaname_search = "xpath=>//*[@id='search_list']/div[4]/div/div/input"
    advertSchedule_isenable_search = "xpath=>//*[@id='search_list']/div[5]/div/div/div[1]/input"
    advertSchedule_effecttype_search = "xpath=>//*[@id='search_list']/div[7]/div/div/div[1]/input"
    advertSchedule_effectchannel_search = "xpath=>//*[@id='search_list']/div[8]/div/div/div/input"
    advertSchedule_search_button = "xpath=>//*[@id='search_list']/div[6]/div/button"
    advertSchedule_click_button = "xpath=>//*[@id='search_list']/div[9]/div/button"
    advertSchedule_begintime = "xpath=>/html/body/div[3]/div[1]/div/div[2]/table[1]/tbody/tr[3]/td[3]/div"
    advertSchedule_endtime = "xpath=>/html/body/div[3]/div[1]/div/div[2]/table[1]/tbody/tr[3]/td[2]/div"
    advertSchedule_isenable = "xpath=>/html/body/div[4]/div[1]/div[1]/ul/li[1]"
    advertSchedule_effecttype = "xpath=>/html/body/div[5]/div[1]/div[1]/ul/li[1]"
    advertSchedule_effectchannel = "xpath=>/html/body/div[6]/div[1]/div[1]/ul/li[1]"

    """
    广告排期各筛选项
    """

    # 开始日期查询
    def begintime_search(self):
        self.click(self.advertSchedule_begintime_search)
        self.sleep(2)
        self.click(self.advertSchedule_begintime)

    # 结束日期查询
    def endtime_search(self):
        self.click(self.advertSchedule_endtime_search)
        self.sleep(2)
        self.click(self.advertSchedule_endtime)

    # 网点ID查询
    def areaid_search(self, text):
        self.type(self.advertSchedule_areaid_search, text)

    # 网点名称查询
    def areaname_search(self, text):
        self.type(self.advertSchedule_areaname_search, text)

    # 是否可用查询
    def isenable_search(self):
        self.click(self.advertSchedule_isenable_search)
        self.sleep(2)
        self.click(self.advertSchedule_isenable)

    # 作用类型查询
    def effecttype_search(self):
        self.click(self.advertSchedule_effecttype_search)
        self.sleep(2)
        self.click(self.advertSchedule_effecttype)

    # 作用渠道查询
    def effectchannel_search(self):
        self.click(self.advertSchedule_effectchannel_search)
        self.sleep(2)
        self.click(self.advertSchedule_effectchannel)

    # 查询按钮
    def search_button_click(self):
        self.click(self.advertSchedule_search_button)

    # 清空按钮
    def click_button_click(self):
        self.click(self.advertSchedule_click_button)

    # 测试结果断言
    result_begintime = "xpath=>//*[@id='app']/div/div/div[2]/div/div[2]/section/div[2]/div/div[3]/table/tbody/tr/td[6]/div"
    result_endtime = "xpath=>//*[@id='app']/div/div/div[2]/div/div[2]/section/div[2]/div/div[3]/table/tbody/tr/td[7]/div"
    result_isenable= "xpath=>//*[@id='app']/div/div/div[2]/div/div[2]/section/div[2]/div/div[3]/table/tbody/tr/td[9]/div/i"
    result_effecttype = "xpath=>//*[@id='app']/div/div/div[2]/div/div[2]/section/div[2]/div/div[3]/table/tbody/tr/td[4]/div"
    result_effectchannel = "xpath=>//*[@id='app']/div/div/div[2]/div/div[2]/section/div[2]/div/div[3]/table/tbody/tr/td[5]/div"

    # 断言开始日期查询结果
    def find_result_begintime(self):
        a = self.get_search_result(self.result_begintime)
        return a

    # 断言结束日期查询结果
    def find_result_endtime(self):
        a = self.get_search_result(self.result_endtime)
        return a

    # 断言是否可用查询结果
    def find_result_isenable(self):
        a = self.get_search_result_icon(self.result_isenable)
        return a

    # 断言作用类型查询结果
    def find_result_effecttype(self):
        a = self.get_search_result(self.result_effecttype)
        return a

    # 断言作用渠道查询结果
    def find_result_effectchannel(self):
        a = self.get_search_result(self.result_effectchannel)
        return a


class BrandMapSearch(BasePage):

    brandMap_brandMapid_search = "xpath=>//*[@id='search_list']/div[1]/div/div/input"
    brandMap_brandMaptitle_search = "xpath=>//*[@id='search_list']/div[2]/div/div/input"
    brandMap_isenable_search = "xpath=>//*[@id='search_list']/div[3]/div/div/div[1]/input"
    brandMap_effectchannel_search = "xpath=>//*[@id='search_list']/div[4]/div/div/div[1]/input"
    brandMap_search_button = "xpath=>//*[@id='search_list']/div[5]/div/button[1]"
    brandMap_click_button = "xpath=>//*[@id='search_list']/div[5]/div/button[2]"
    brandMap_isenable = "xpath=>/html/body/div[4]/div[1]/div[1]/ul/li[1]"
    brandMap_effectchannel = "xpath=>/html/body/div[5]/div[1]/div[1]/ul/li[1]"

    """
    支付页背景图各筛选项
    """

    # 背景图ID查询
    def brandmapid_search(self, text):
        self.type(self.brandMap_brandMapid_search, text)

    # 背景图标题查询
    def brandmaptitle_search(self, text):
        self.type(self.brandMap_brandMaptitle_search, text)

    # 是否启用查询
    def isenable_search(self):
        self.click(self.brandMap_isenable_search)
        self.sleep(2)
        self.click(self.brandMap_isenable)

    # 作用渠道查询
    def effectchannel_search(self):
        self.click(self.brandMap_effectchannel_search)
        self.sleep(2)
        self.click(self.brandMap_effectchannel)

    # 查询按钮
    def search_button_click(self):
        self.click(self.brandMap_search_button)

    # 清空按钮
    def click_button_click(self):
        self.click(self.brandMap_click_button)

    # 测试结果断言
    result_brandMapid = "xpath=>//*[@id='app']/div/div/div[2]/div/div[2]/section/div[1]/div[3]/table/tbody/tr/td[2]/div"
    result_brandMaptitle = "xpath=>//*[@id='app']/div/div/div[2]/div/div[2]/section/div[1]/div[3]/table/tbody/tr/td[3]/div"
    result_isenable = "xpath=>//*[@id='app']/div/div/div[2]/div/div[2]/section/div[1]/div[3]/table/tbody/tr/td[7]/div/i"
    result_effectchannel = "xpath=>//*[@id='app']/div/div/div[2]/div/div[2]/section/div[1]/div[3]/table/tbody/tr/td[6]/div"

    # 断言背景图ID查询结果
    def find_result_brandmapid(self):
        a = self.get_search_result(self.result_brandMapid)
        return a

    # 断言背景图标题查询结果
    def find_result_brandmaptitle(self):
        a = self.get_search_result(self.result_brandMaptitle)
        return a

    # 断言是否启用查询结果
    def find_result_isenable(self):
        a = self.get_search_result(self.result_isenable)
        return a

    # 断言作用渠道查询结果
    def find_result_effectchannel(self):
        a = self.get_search_result(self.result_effectchannel)
        return a


class CountDownSearch(BasePage):

    countDown_popupid_search = "xpath=>//*[@id='search_list']/div[1]/div/div/input"
    countDown_popupname_search = "xpath=>//*[@id='search_list']/div[2]/div/div/input"
    countDown_effectivestatus_search = "xpath=>//*[@id='search_list']/div[3]/div/div/div[2]/input"
    countDown_effectchannel_search = "xpath=>//*[@id='search_list']/div[4]/div/div/div[1]/input"
    countDown_popuptype_search = "xpath=>//*[@id='search_list']/div[5]/div/div/div[1]/input"
    countDown_search_button = "xpath=>//*[@id='search_list']/div[6]/div/button[1]"
    countDown_click_button = "xpath=>//*[@id='search_list']/div[6]/div/button[2]"
    countDown_effectivestatus = "xpath=>/html/body/div[4]/div[1]/div[1]/ul/li[1]"
    countDown_effectchannel = "xpath=>/html/body/div[5]/div[1]/div[1]/ul/li[1]"
    countDown_popuptype = "xpath=>/html/body/div[6]/div[1]/div[1]/ul/li[1]"

    """
    倒计时页弹窗各筛选项
    """

    # 弹窗ID查询
    def popupid_search(self, text):
        self.type(self.countDown_popupid_search, text)

    # 弹窗名称查询
    def popupname_search(self, text):
        self.type(self.countDown_popupname_search, text)

    # 生效状态查询
    def effectivestatus_search(self):
        self.click(self.countDown_effectivestatus_search)
        self.sleep(2)
        self.click(self.countDown_effectivestatus)

    # 作用渠道查询
    def effectchannel_search(self):
        self.click(self.countDown_effectchannel_search)
        self.sleep(2)
        self.click(self.countDown_effectchannel)

    # 弹窗类型查询
    def popuptype_search(self):
        self.click(self.countDown_popuptype_search)
        self.sleep(2)
        self.click(self.countDown_popuptype)

    # 查询按钮
    def search_button_click(self):
        self.click(self.countDown_search_button)

    # 清空按钮
    def click_button_click(self):
        self.click(self.countDown_click_button)

    # 测试结果断言
    result_popupid = "xpath=>//*[@id='countDown']/div[1]/div[3]/table/tbody/tr/td[2]/div"
    result_popupname = "xpath=>//*[@id='countDown']/div[1]/div[3]/table/tbody/tr/td[3]/div"
    result_effectivestatus = "xpath=>//*[@id='countDown']/div[1]/div[3]/table/tbody/tr[1]/td[9]/div/span"
    result_effectchannel = "xpath=>//*[@id='countDown']/div[1]/div[3]/table/tbody/tr[1]/td[6]/div/span"
    result_popuptype = "xpath=>//*[@id='countDown']/div[1]/div[3]/table/tbody/tr[1]/td[4]/div/span"

    # 断言弹窗ID查询结果
    def find_result_popupid(self):
        a = self.get_search_result(self.result_popupid)
        return a

    # 断言弹窗名称查询结果
    def find_result_popupname(self):
        a = self.get_search_result(self.result_popupname)
        return a

    # 断言生效状态查询结果
    def find_result_effectivestatus(self):
        a = self.get_search_result(self.result_effectivestatus)
        return a

    # 断言作用渠道查询结果
    def find_result_effectchannel(self):
        a = self.get_search_result(self.result_effectchannel)
        return a

    # 断言弹窗类型查询结果
    def find_result_popuptype(self):
        a = self.get_search_result(self.result_popuptype)
        return a
