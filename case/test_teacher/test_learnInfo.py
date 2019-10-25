#encoding=utf-8
import unittest

from case.test_teacher.cs_teacher_function import *
from function.Logfz import Log


class LearnInfo(unittest.TestCase):
    # 学情分析 模块测试

    @classmethod
    def setUpClass(self):
        print("start......")

    @classmethod
    def tearDownClass(self):
        print("end......")

    def test_01(self):
        # 学情分析-上课进度
        Log().info("学情分析-上课进度")
        Funciton().public_method("14")


    def test_02(self):
        # 上课进度导出报表
        Log().info("上课进度导出报表")
        Funciton().public_method("15")


    def test_03(self):
        # 学情分析-测验结果
        Log().info("学情分析-测验结果")
        Funciton().public_method("16")


    def test_04(self):
        # 测验结果导出报表
        Log().info("测验结果导出报表")
        Funciton().public_method("17")


    def test_05(self):
        # 学情分析-掌握知识点
        Log().info("学情分析-掌握知识点")
        Funciton().public_method("18")


    def test_06(self):
        # 掌握知识点导出报表
        Log().info("掌握知识点导出报表")
        Funciton().public_method("19")


if __name__ == '__main__':
    unittest.main()