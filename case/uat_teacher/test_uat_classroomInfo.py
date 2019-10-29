#encoding=utf-8
import unittest

from case.uat_teacher.uat_teacher_function import *
from function.Logfz import Log


class ClassroomInfo(unittest.TestCase):
    # 班课列表、消息通知、课程概览 模块测试

    @classmethod
    def setUpClass(self):
        print("start......")

    @classmethod
    def tearDownClass(self):
        print("end......")

    def test_01(self):
        # 查询我的班课列表
        Log().info("查询我的班课列表")
        Funciton().public_method("2")


    def test_02(self):
        # 消息通知
        Log().info("消息通知")
        Funciton().public_method("3")


    def test_03(self):
        # 查看消息列表
        Log().info("查看消息列表")
        Funciton().public_method("4")


    def test_04(self):
        # 查看班级下的课程概览
        Log().info("查看班级下的课程概览")
        Funciton().public_method("5")


if __name__ == '__main__':
    unittest.main()