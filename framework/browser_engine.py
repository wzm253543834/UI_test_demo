# coding = utf-8
import configparser
import os.path
from selenium import webdriver
from framework.logger import Logger

logger = Logger(logger="BrowserEngine").getlog()


class BrowserEngine(object):

    dir = os.path.dirname(os.path.abspath('.'))    # 注意相对路径获取方法
    chrome_driver_path = dir + '/tools/chromedriver.exe'
    ie_driver_path = dir + '/tools/IEDriverServer.exe'
    firefox_driver_path = dir + '/tools/geckodriver.exe'

    def __init__(self, driver):
        self.driver = driver

    # 从config.ini文件读取相关的测试地址和浏览器
    def open_browser(self, driver):
        config = configparser.ConfigParser()
        # file_path = os.path.dirname(os.getcwd()) + '/config/config.ini'
        file_path = os.path.dirname(os.path.abspath('.')) + '/config/config.ini'
        config.read(file_path)
        # config.read(file_path, encoding='UTF-8')  # 如果代码中有中文注释，用这个，不然报解码错误
        browser = config.get("browserType", "browserName")
        logger.info("你选择 %s 浏览器.", browser)
        url = config.get("testServer", "URL")
        logger.info("测试服务器地址是: %s", url)

        if browser == "Firefox":
            driver = webdriver.Firefox(self.firefox_driver_path)
            logger.info("启动 Firefox 浏览器.")
        elif browser == "Chrome":
            driver = webdriver.Chrome(self.chrome_driver_path)
            logger.info("启动 Chrome 浏览器.")
        elif browser == "IE":
            driver = webdriver.Ie(self.ie_driver_path)
            logger.info("启动 IE 浏览器.")

        driver.get(url)
        logger.info("打开链接: %s", url)
        driver.maximize_window()
        logger.info("当前窗口最大化.")
        driver.implicitly_wait(10)
        logger.info("隐式等待10秒.")
        return driver

    def quit_browser(self):
        logger.info("现在，关闭并退出浏览器.")
        self.driver.quit()
