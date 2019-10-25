#encoding=utf-8
import unittest

from case.uat_agent.uat_agent_function import *
from function.Logfz import Log


class AgentInfo(unittest.TestCase):
    # 下属代理商功能模块 测试

    @classmethod
    def setUpClass(self):
        print("start......")

    @classmethod
    def tearDownClass(self):
        print("end......")


    def test_01(self):
        # 查询下属代理商列表
        Log().info("查询下属代理商列表")
        Funciton().public_method("2")


    def test_02(self):
        # 查询下属代理商账户列表
        Log().info("查询下属代理商账户列表")
        Funciton().public_method("3")


    def test_03(self):
        # 查询下属代理商转课时记录
        Log().info("查询下属代理商转课时记录")
        Funciton().public_method("4")


    def test_04(self):
        # 查询代理商单个转课时详情
        Log().info("查询代理商单个转课时详情")
        Funciton().public_method("5")


    def test_05(self):
        # 查询代理商转课时的充值记录
        Log().info("查询代理商转课时的充值记录")
        Funciton().public_method("6")


    def test_06(self):
        # 给二级代理商转课时
        Log().info("给二级代理商转课时")
        Funciton().public_method("7")


    def test_07(self):
        # 首页查询代理商基本信息
        Log().info("首页查询代理商基本信息")
        Funciton().public_method("31")


    def test_08(self):
        # 首页查询代理商充值记录
        Log().info("首页查询代理商充值记录")
        Funciton().public_method("32")


    def test_09(self):
        # 首页查看消息数
        Log().info("首页查看消息数")
        Funciton().public_method("33")


if __name__ == '__main__':
    unittest.main()