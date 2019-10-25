#encoding=utf-8

import smtplib
import unittest
# HTMLTestRunner是基于unittest框架的一个扩展, 可以自己在网上自行下载
import os
import time
from email.header import Header
from email.mime.text import MIMEText
# from lib.HTMLTestRunner import HTMLTestRunner



def send_mail(path):
    f = open(path, 'rb')
    mail_body = f.read()    # 读取html报告的内容,作为邮件的正文
    f.close()

    # 发邮件, 把二进制的内容转成MIME格式
    # MIME是对邮件协议的一个扩展, 使 邮件不仅支持文本,还支持多种格式, 比如图片,音频, 二进制文件等
    msg = MIMEText(mail_body, 'html', 'utf-8')
    # msg是字典的类型
    msg['Subject'] = Header("自动化测试报告",'utf-8')
    # 如果想用客户端软件或者自己写代码登录邮箱,很多类型的邮件,需要单独设置一个客户端授权码
    msg['From'] = 'bwftest126@126.com'
    msg['To'] = 'changchengxc@126.com'

    #开始发邮件
    #步骤:
    #1.打开登录页面, 即连接邮箱服务器
    # 126邮箱支持这三种协议pop3, smtp, imap
    # 我们要选一种传输协议,用来发邮件, smtp 简单邮件传输协议
    # 首先导入smtplib的代码库
    smtp = smtplib.SMTP()   # 实例化一个SMTP类的对象
    smtp.connect("smtp.126.com")  # 链接126邮箱的 服务器地址
    #2.登录邮箱
    smtp.login('bwftest126@126.com','abc123asd654')
    #3.发送邮件
    # 注意msg是MIME类型,需要转成String类型再发送
    smtp.sendmail('bwftest126@126.com', 'changchengxc@126.com', msg.as_string())
    #4.退出邮箱
    smtp.quit()
    print('email has sent out!')

if __name__ == '__main__':
    # str 是String  f是format格式
    # strftime()通过这个方法可以定义时间的格式
    # Y year年, m month月, d day日, H hour 小时, M minute分, S second秒
    now = time.strftime("%Y-%m-%d_%H-%M-%S")

    suite = unittest.defaultTestLoader.discover('./day5', '*Test.py')
    # unittest.TextTestRunner() 文本测试用运行器
    # 现在用html的测试用例运行器
    # html的测试用例运行器最终会生成一个html格式的测试报告
    # 我们是不是至少要指定测试报告的路径啊
    base_path = os.path.dirname(__file__)
    path = base_path + "/report/report" + now + ".html"
    file = open(path, 'wb')
    HTMLTestRunner(file,1, "海盗商城测试报告", "测试环境:Window Server 2008 + Chrome").run(suite)
    file.close()
    # 我们要把html报告作为邮件正文, 发邮件
    send_mail(path)
    # 这时生成的测试报告, 只显示类名和方法名,只能给专业的人士看
    # 我们应该相关的手动测试用例的标题加到我们的测试报告
    # 我们自动化测试用例是从手功测试用例中挑出来的,手工测试用例怎么写,我们就怎么编写代码, 所以我们的代码里应该可以体现手功测试用例的标题
    # 新的测试报告会覆盖原来的测试报告, 如果想把所有的测试报告保存起来怎么做
    # 加一个时间戳,按照当前时间计算一个数字,把数字作为文件名的一部分,就避免了文件名重复的问题
    # 现在我们的html格式的测试报告生成了, 当测试用例全部执行完成, 我们应该生成一封提醒邮件, 通知所有关心测试结果的人