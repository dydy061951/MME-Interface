#encoding=utf-8

import unittest,os,time
from function.mail import send_mail
from function.HTMLTestRunner import HTMLTestRunner

if __name__ == '__main__':

    # 默认的测试用例加载器 defaultTestLoader
    suite = unittest.defaultTestLoader.discover('./case/cs_agent', pattern='test_courseInfo.py')
    # （控制台）执行集合test用例文件
    # unittest.TextTestRunner().run(suite)


    # 测试报告输出测试结果
    now = time.strftime("%Y%m%d_%H%M%S")
    # 指定测试报告的路径
    base_path = os.path.dirname(__file__)
    report_path = base_path + "/report/report" + now + ".html"
    file = open(report_path, 'wb')
    # 测试报告运行用例并输出
    HTMLTestRunner(file, 1, "接口测试报告", "测试环境:Window 10 ").run(suite)
    file.close()

    # 发送邮件
    mailFile_list=[base_path + "/report/report" + now + ".html",base_path + "/data/test_agent.xlsx"]
    send_mail(mailFile_list)


