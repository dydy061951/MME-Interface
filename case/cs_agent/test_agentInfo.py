#encoding=utf-8
import unittest

from case.cs_agent.cs_agent_function import *
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

        F = Funciton()
        request_info = F.get_request_info(2)
        actual_result = F.public_method("2").status_code  # int
        expected_results = int(request_info[6])  # int
        F.result_assertion(expected_results, actual_result, "2")
        try:
            self.assertEqual(expected_results, actual_result)
        except Exception as msg:
            Log().info("Exception:" + F.public_method("2").json()['msg'])
            raise msg


    def test_02(self):
        # 查询下属代理商账户列表
        Log().info("查询下属代理商账户列表")

        F = Funciton()
        request_info = F.get_request_info(3)
        actual_result = F.public_method("3").status_code  # int
        expected_results = int(request_info[6])  # int
        F.result_assertion(expected_results, actual_result, "3")
        try:
            self.assertEqual(expected_results, actual_result)
        except Exception as msg:
            Log().info("Exception:" + F.public_method("3").json()['msg'])
            raise msg


    def test_03(self):
        # 查询下属代理商转课时记录
        Log().info("查询下属代理商转课时记录")

        F = Funciton()
        request_info = F.get_request_info(4)
        actual_result = F.public_method("4").status_code  # int
        expected_results = int(request_info[6])  # int
        F.result_assertion(expected_results, actual_result, "4")
        try:
            self.assertEqual(expected_results, actual_result)
        except Exception as msg:
            Log().info("Exception:" + F.public_method("4").json()['msg'])
            raise msg


    def test_04(self):
        # 查询代理商单个转课时详情
        Log().info("查询代理商单个转课时详情")

        F = Funciton()
        request_info = F.get_request_info(5)
        actual_result = F.public_method("5").status_code  # int
        expected_results = int(request_info[6])  # int
        F.result_assertion(expected_results, actual_result, "5")
        try:
            self.assertEqual(expected_results, actual_result)
        except Exception as msg:
            Log().info("Exception:" + F.public_method("5").json()['msg'])
            raise msg


    def test_05(self):
        # 查询代理商转课时的充值记录
        Log().info("查询代理商转课时的充值记录")

        F = Funciton()
        request_info = F.get_request_info(6)
        actual_result = F.public_method("6").status_code  # int
        expected_results = int(request_info[6])  # int
        F.result_assertion(expected_results, actual_result, "6")
        try:
            self.assertEqual(expected_results, actual_result)
        except Exception as msg:
            Log().info("Exception:" + F.public_method("6").json()['msg'])
            raise msg


    def test_06(self):
        # 给二级代理商转课时
        Log().info("给二级代理商转课时")

        F = Funciton()
        request_info = F.get_request_info(7)
        actual_result = F.public_method("7").status_code  # int
        expected_results = int(request_info[6])  # int
        F.result_assertion(expected_results, actual_result, "7")
        try:
            self.assertEqual(expected_results, actual_result)
        except Exception as msg:
            Log().info("Exception:" + F.public_method("7").json()['msg'])
            raise msg


    def test_07(self):
        # 首页查询代理商基本信息
        Log().info("首页查询代理商基本信息")

        F = Funciton()
        request_info = F.get_request_info(31)
        actual_result = F.public_method("31").status_code  # int
        expected_results = int(request_info[6])  # int
        F.result_assertion(expected_results, actual_result, "31")
        try:
            self.assertEqual(expected_results, actual_result)
        except Exception as msg:
            Log().info("Exception:" + F.public_method("31").json()['msg'])
            raise msg


    def test_08(self):
        # 首页查询代理商充值记录
        Log().info("首页查询代理商充值记录")

        F = Funciton()
        request_info = F.get_request_info(32)
        actual_result = F.public_method("32").status_code  # int
        expected_results = int(request_info[6])  # int
        F.result_assertion(expected_results, actual_result, "32")
        try:
            self.assertEqual(expected_results, actual_result)
        except Exception as msg:
            Log().info("Exception:" + F.public_method("32").json()['msg'])
            raise msg


    def test_09(self):
        # 首页查看消息数
        Log().info("首页查看消息数")

        F = Funciton()
        request_info = F.get_request_info(33)
        actual_result = F.public_method("33").status_code  # int
        expected_results = int(request_info[6])  # int
        F.result_assertion(expected_results, actual_result, "33")
        try:
            self.assertEqual(expected_results, actual_result)
        except Exception as msg:
            Log().info("Exception:" + F.public_method("33").json()['msg'])
            raise msg


if __name__ == '__main__':
    unittest.main()