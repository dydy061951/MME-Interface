#encoding=utf-8
import unittest

from case.cs_agent.cs_agent_function import *
from function.Logfz import Log


class Report(unittest.TestCase):
    # 数据报表、代理商excel导出模块 测试

    @classmethod
    def setUpClass(self):
        print("start......")

    @classmethod
    def tearDownClass(self):
        print("end......")


    def test_01(self):
        # 累计注册用户数
        Log().info("累计注册用户数")
        Funciton().excel_value("36")
        Funciton().public_method(36,"36")


    def test_02(self):
        # 新增注册用户数
        Log().info("新增注册用户数")
        Funciton().excel_value("37")
        Funciton().public_method(37,"37")


    def test_03(self):
        # 新增激活用户数
        Log().info("新增激活用户数")
        Funciton().excel_value("38")
        Funciton().public_method(38,"38")


    def test_04(self):
        # 新增付费用户数
        Log().info("新增付费用户数")
        Funciton().excel_value("39")
        Funciton().public_method(39,"39")


    def test_05(self):
        # 累计注册学校数
        Log().info("新增激活用户数")
        Funciton().excel_value("40")
        Funciton().public_method(40,"40")


    def test_06(self):
        # 新增注册学校数
        Log().info("新增注册学校数")
        Funciton().excel_value("41")
        Funciton().public_method(41,"41")


    def test_07(self):
        # 新增激活学校数
        Log().info("新增激活学校数")
        Funciton().excel_value("42")
        Funciton().public_method(42,"42")


    def test_08(self):
        # 新增付费学校数
        Log().info("新增付费学校数")
        Funciton().excel_value("43")
        Funciton().public_method(43,"43")


    def test_09(self):
        # 7日 | 每日新增用户数
        Log().info("7日 | 每日新增用户数")
        Funciton().excel_value("44")
        Funciton().public_method(44,"44")


    def test_10(self):
        # 7日 | 用户角色分布
        Log().info("7日 | 用户角色分布")
        Funciton().excel_value("45")
        Funciton().public_method(45,"45")

    def test_11(self):
        # 代理商excel导出
        Log().info("代理商excel导出")
        Funciton().public_method(46,"46")


if __name__ == '__main__':
    unittest.main()