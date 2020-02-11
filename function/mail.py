#encoding=utf-8

import zmail
from function.Logfz import Log

def send_mail(mail_file):
    # 发送邮件

    # 你的邮件内容
    mail_content = {
        'subject': '自动化测试报告!',    # 邮件标题
        'content_text': '测试报告结果查看!',  # 邮件正文
        'attachments': mail_file ,          # 附件：最好使用绝对路径
    }

    # 使用你的邮件账户名和密码登录服务器
    server = zmail.server('dy061951@163.com', 'dy061951')
    # 发送邮件
    server.send_mail('245405102@qq.com', mail_content)
    # 给多个邮箱发送
    # server.send_mail(['555555@qq.com','666666@qq.com'], mail_content)
    Log().info("邮件发送成功")

