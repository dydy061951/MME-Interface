#encoding=utf-8

import unittest, random
from case.cs_agent.cs_agent_function import *
from function.excelUtils import *
from function.Logfz import Log


class CustomerInfo(unittest.TestCase):
    # 客户管理功能模块 测试

    randomnu = str(random.randint(0, 1000))  # 随机数产生
    header = Token().test_agent_header

    @classmethod
    def setUpClass(self):
        print("start......")

    @classmethod
    def tearDownClass(self):
        print("end......")


    def test_01(self):
        # 新增客户
        Log().info("新增客户")

        F = Funciton()
        request_info = F.get_request_info(8)
        dict = json.loads(request_info[5])
        dict["name"] = "yijikehu" + self.randomnu + "-" + self.randomnu + ""
        dict["account"]="wanghn1j"+self.randomnu+"-"+self.randomnu+""
        str_dict = json.dumps(dict)  # 这里转换不能直接用 str(dict)，会使字典格式属性和值单双引号不一致
        writeExcel("test_agent.xlsx", "F8", str_dict)
        request_info = F.get_request_info(8)
        actual_result = F.public_method("8").status_code  # int
        expected_results = int(request_info[6])  # int
        F.result_assertion(expected_results, actual_result, "8")
        try:
            self.assertEqual(expected_results, actual_result)
        except Exception as msg:
            Log().info("Exception:" + F.public_method("8").json()['msg'])
            raise msg


    def test_02(self):
        # 修改客户
        Log().info("修改客户")

        F = Funciton()
        request_info = F.get_request_info(9)
        actual_result = F.public_method("9").status_code  # int
        expected_results = int(request_info[6])  # int
        F.result_assertion(expected_results, actual_result, "9")
        try:
            self.assertEqual(expected_results, actual_result)
        except Exception as msg:
            Log().info("Exception:" + F.public_method("9").json()['msg'])
            raise msg


    def test_03(self):
        # 查看客户详情
        Log().info("查看客户详情")

        F = Funciton()
        request_info = F.get_request_info(10)
        actual_result = F.public_method("10").status_code  # int
        expected_results = int(request_info[6])  # int
        F.result_assertion(expected_results, actual_result, "10")
        try:
            self.assertEqual(expected_results, actual_result)
        except Exception as msg:
            Log().info("Exception:" + F.public_method("10").json()['msg'])
            raise msg


    def test_04(self):
        # 查看客户可见商品列表
        Log().info("查看班课设置列表")

        F = Funciton()
        request_info = F.get_request_info(11)
        actual_result = F.public_method("11").status_code  # int
        expected_results = int(request_info[6])  # int
        F.result_assertion(expected_results, actual_result, "11")
        try:
            self.assertEqual(expected_results, actual_result)
        except Exception as msg:
            Log().info("Exception:" + F.public_method("11").json()['msg'])
            raise msg


    def test_05(self):
        # 查询客户下可见商品详情（附带租户的课数）
        Log().info("查询客户下可见商品详情（附带租户的课数）")

        F = Funciton()
        request_info = F.get_request_info(12)
        actual_result = F.public_method("12").status_code  # int
        expected_results = int(request_info[6])  # int
        F.result_assertion(expected_results, actual_result, "12")
        try:
            self.assertEqual(expected_results, actual_result)
        except Exception as msg:
            Log().info("Exception:" + F.public_method("12").json()['msg'])
            raise msg


    def test_06(self):
        # 客户购买课程最近十次操作记录
        Log().info("客户购买课程最近十次操作记录")

        F = Funciton()
        request_info = F.get_request_info(13)
        actual_result = F.public_method("13").status_code  # int
        expected_results = int(request_info[6])  # int
        F.result_assertion(expected_results, actual_result, "13")
        try:
            self.assertEqual(expected_results, actual_result)
        except Exception as msg:
            Log().info("Exception:" + F.public_method("13").json()['msg'])
            raise msg


    def test_07(self):
        # 客户购买课时
        Log().info("客户购买课时")

        F = Funciton()
        request_info = F.get_request_info(14)
        actual_result = F.public_method("14").status_code  # int
        expected_results = int(request_info[6])  # int
        F.result_assertion(expected_results, actual_result, "14")
        try:
            self.assertEqual(expected_results, actual_result)
        except Exception as msg:
            Log().info("Exception:" + F.public_method("14").json()['msg'])
            raise msg


    def test_08(self):
        # 查看客户列表
        Log().info("查看客户列表")

        F = Funciton()
        request_info = F.get_request_info(34)
        actual_result = F.public_method("34").status_code  # int
        expected_results = int(request_info[6])  # int
        F.result_assertion(expected_results, actual_result, "34")
        try:
            self.assertEqual(expected_results, actual_result)
        except Exception as msg:
            Log().info("Exception:" + F.public_method("34").json()['msg'])
            raise msg


    def test_09(self):
        # 客户列表导出
        Log().info("客户列表导出")

        F = Funciton()
        request_info = F.get_request_info(15)
        actual_result = F.public_method("15").status_code  # int
        expected_results = int(request_info[6])  # int
        F.result_assertion(expected_results, actual_result, "15")
        try:
            self.assertEqual(expected_results, actual_result)
        except Exception as msg:
            Log().info("Exception:" + F.public_method("15").json()['msg'])
            raise msg


    def test_10(self):
        # 查看客户班课记录
        Log().info("查看客户班课记录")

        F = Funciton()
        request_info = F.get_request_info(16)
        actual_result = F.public_method("16").status_code  # int
        expected_results = int(request_info[6])  # int
        F.result_assertion(expected_results, actual_result, "16")
        try:
            self.assertEqual(expected_results, actual_result)
        except Exception as msg:
            Log().info("Exception:" + F.public_method("16").json()['msg'])
            raise msg


if __name__ == '__main__':
    unittest.main()