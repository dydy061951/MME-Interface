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

        F = Funciton()
        request_info = F.get_request_info(17)
        actual_result = F.public_method("17").status_code  # int
        expected_results = int(request_info[6])  # int
        F.result_assertion(expected_results, actual_result, "17")
        try:
            self.assertEqual(expected_results, actual_result)
        except Exception as msg:
            Log().info("Exception:" + F.public_method("17").json()['msg'])
            raise msg


    def test_02(self):
        # 查看所有课程列表课程详情
        Log().info("查看所有课程列表课程详情")

        F = Funciton()
        request_info = F.get_request_info(18)
        actual_result = F.public_method("18").status_code  # int
        expected_results = int(request_info[6])  # int
        F.result_assertion(expected_results, actual_result, "18")
        try:
            self.assertEqual(expected_results, actual_result)
        except Exception as msg:
            Log().info("Exception:" + F.public_method("18").json()['msg'])
            raise msg


    def test_03(self):
        # 查看客户已购课程商品列表
        Log().info("查看客户已购课程商品列表")

        F = Funciton()
        request_info = F.get_request_info(19)
        actual_result = F.public_method("19").status_code  # int
        expected_results = int(request_info[6])  # int
        F.result_assertion(expected_results, actual_result, "19")
        try:
            self.assertEqual(expected_results, actual_result)
        except Exception as msg:
            Log().info("Exception:" + F.public_method("19").json()['msg'])
            raise msg


    def test_04(self):
        # 查看客户已购商品课程详情
        Log().info("查看客户已购商品课程详情")

        F = Funciton()
        request_info = F.get_request_info(20)
        actual_result = F.public_method("20").status_code  # int
        expected_results = int(request_info[6])  # int
        F.result_assertion(expected_results, actual_result, "20")
        try:
            self.assertEqual(expected_results, actual_result)
        except Exception as msg:
            Log().info("Exception:" + F.public_method("20").json()['msg'])
            raise msg


if __name__ == '__main__':
    unittest.main()