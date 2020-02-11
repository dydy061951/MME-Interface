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
        F = Funciton()
        request_info = F.get_request_info(36)
        actual_result = F.public_method("36").status_code  # int
        expected_results = int(request_info[6])  # int
        F.result_assertion(expected_results, actual_result, "36")
        try:
            self.assertEqual(expected_results, actual_result)
        except Exception as msg:
            Log().info("Exception:" + F.public_method("36").json()['msg'])
            raise msg


    def test_02(self):
        # 新增注册用户数
        Log().info("新增注册用户数")

        Funciton().excel_value("37")
        F = Funciton()
        request_info = F.get_request_info(37)
        actual_result = F.public_method("37").status_code  # int
        expected_results = int(request_info[6])  # int
        F.result_assertion(expected_results, actual_result, "37")
        try:
            self.assertEqual(expected_results, actual_result)
        except Exception as msg:
            Log().info("Exception:" + F.public_method("37").json()['msg'])
            raise msg


    def test_03(self):
        # 新增激活用户数
        Log().info("新增激活用户数")

        Funciton().excel_value("38")
        F = Funciton()
        request_info = F.get_request_info(38)
        actual_result = F.public_method("38").status_code  # int
        expected_results = int(request_info[6])  # int
        F.result_assertion(expected_results, actual_result, "38")
        try:
            self.assertEqual(expected_results, actual_result)
        except Exception as msg:
            Log().info("Exception:" + F.public_method("38").json()['msg'])
            raise msg


    def test_04(self):
        # 新增付费用户数
        Log().info("新增付费用户数")

        Funciton().excel_value("39")
        F = Funciton()
        request_info = F.get_request_info(39)
        actual_result = F.public_method("39").status_code  # int
        expected_results = int(request_info[6])  # int
        F.result_assertion(expected_results, actual_result, "39")
        try:
            self.assertEqual(expected_results, actual_result)
        except Exception as msg:
            Log().info("Exception:" + F.public_method("39").json()['msg'])
            raise msg


    def test_05(self):
        # 累计注册学校数
        Log().info("新增激活用户数")
        Funciton().excel_value("40")

        F = Funciton()
        request_info = F.get_request_info(40)
        actual_result = F.public_method("40").status_code  # int
        expected_results = int(request_info[6])  # int
        F.result_assertion(expected_results, actual_result, "40")
        try:
            self.assertEqual(expected_results, actual_result)
        except Exception as msg:
            Log().info("Exception:" + F.public_method("40").json()['msg'])
            raise msg


    def test_06(self):
        # 新增注册学校数
        Log().info("新增注册学校数")
        Funciton().excel_value("41")

        F = Funciton()
        request_info = F.get_request_info(41)
        actual_result = F.public_method("41").status_code  # int
        expected_results = int(request_info[6])  # int
        F.result_assertion(expected_results, actual_result, "41")
        try:
            self.assertEqual(expected_results, actual_result)
        except Exception as msg:
            Log().info("Exception:" + F.public_method("41").json()['msg'])
            raise msg


    def test_07(self):
        # 新增激活学校数
        Log().info("新增激活学校数")
        Funciton().excel_value("42")

        F = Funciton()
        request_info = F.get_request_info(42)
        actual_result = F.public_method("42").status_code  # int
        expected_results = int(request_info[6])  # int
        F.result_assertion(expected_results, actual_result, "42")
        try:
            self.assertEqual(expected_results, actual_result)
        except Exception as msg:
            Log().info("Exception:" + F.public_method("42").json()['msg'])
            raise msg


    def test_08(self):
        # 新增付费学校数
        Log().info("新增付费学校数")
        Funciton().excel_value("43")

        F = Funciton()
        request_info = F.get_request_info(43)
        actual_result = F.public_method("43").status_code  # int
        expected_results = int(request_info[6])  # int
        F.result_assertion(expected_results, actual_result, "43")
        try:
            self.assertEqual(expected_results, actual_result)
        except Exception as msg:
            Log().info("Exception:" + F.public_method("43").json()['msg'])
            raise msg


    def test_09(self):
        # 7日 | 每日新增用户数
        Log().info("7日 | 每日新增用户数")
        Funciton().excel_value("44")

        F = Funciton()
        request_info = F.get_request_info(44)
        actual_result = F.public_method("44").status_code  # int
        expected_results = int(request_info[6])  # int
        F.result_assertion(expected_results, actual_result, "44")
        try:
            self.assertEqual(expected_results, actual_result)
        except Exception as msg:
            Log().info("Exception:" + F.public_method("44").json()['msg'])
            raise msg


    def test_10(self):
        # 7日 | 用户角色分布
        Log().info("7日 | 用户角色分布")
        Funciton().excel_value("45")

        F = Funciton()
        request_info = F.get_request_info(45)
        actual_result = F.public_method("45").status_code  # int
        expected_results = int(request_info[6])  # int
        F.result_assertion(expected_results, actual_result, "45")
        try:
            self.assertEqual(expected_results, actual_result)
        except Exception as msg:
            Log().info("Exception:" + F.public_method("45").json()['msg'])
            raise msg

    def test_11(self):
        # 代理商excel导出
        Log().info("代理商excel导出")

        F = Funciton()
        request_info = F.get_request_info(46)
        actual_result = F.public_method("46").status_code  # int
        expected_results = int(request_info[6])  # int
        F.result_assertion(expected_results, actual_result, "46")
        try:
            self.assertEqual(expected_results, actual_result)
        except Exception as msg:
            Log().info("Exception:" + F.public_method("46").json()['msg'])
            raise msg


if __name__ == '__main__':
    unittest.main()