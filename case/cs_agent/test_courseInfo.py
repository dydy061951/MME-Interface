#encoding=utf-8
import unittest

from case.cs_agent.cs_agent_function import *
from function.Logfz import Log

class CourseInfo(unittest.TestCase):
    # 课程商品功能模块 测试

    @classmethod
    def setUpClass(self):
        print("start......")

    @classmethod
    def tearDownClass(self):
        print("end......")


    def test_01(self):
        # 查看所有课程商品列表
        Log().info("查看所有课程商品列表")
        Funciton().public_method("17")


    def test_02(self):
        # 查看所有课程列表课程详情
        Log().info("查看所有课程列表课程详情")
        Funciton().public_method("18")


    def test_03(self):
        # 查看客户已购课程商品列表
        Log().info("查看客户已购课程商品列表")
        Funciton().public_method("19")

    def test_04(self):
        # 查看客户已购商品课程详情
        Log().info("查看客户已购商品课程详情")
        Funciton().public_method("20")


if __name__ == '__main__':
    unittest.main()