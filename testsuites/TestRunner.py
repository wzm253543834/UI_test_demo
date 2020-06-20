# coding = utf-8
import unittest
# import os
import time
# import HtmlTestRunner
from BeautifulReport import BeautifulReport

# 设置报告文件保存路径 HtmlTestRunner
# report_path = os.path.dirname(os.path.abspath('')) + '/test_report/'

# 获取系统当前时间
now = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time.time()))

# 设置报告名称格式 HtmlTestRunner
# HtmlFile = report_path + now + 'HTMLtemplat.html'
# fp = open(HtmlFile, 'w', encoding='UTF-8')

# 构建suite
test_dir = "testsuites"
suite = unittest.TestLoader().discover(test_dir, pattern='test*.py', top_level_dir=None)

if __name__ == '__main__':

    # 执行用例
    # runner = unittest.TextTestRunner()

    # 初始化一个HtmlTestRunner实例对象，用来生成报告
    # runner = HtmlTestRunner.HTMLTestRunner(stream=fp, report_title=u'某某项目测试报告', descriptions=u'用例测试情况')

    # 开始执行测试套件
    # runner.run(suite)

    runner = BeautifulReport(suite)
    runner.report(filename='./test_report/测试报告' + now, description='乐摩吧项目测试用例')
