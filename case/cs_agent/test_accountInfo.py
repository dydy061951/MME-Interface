#encoding=utf-8
import unittest, random

from case.cs_agent.cs_agent_function import *
from function.excelUtils import *
from function.Logfz import Log



class AccountInfo(unittest.TestCase):
    # 账号管理、消息通知功能模块 测试

    randomnu = str(random.randint(0, 1000))  # 随机数产生
    header = Token().test_agent_header

    @classmethod
    def setUpClass(self):
        print("start......")

    @classmethod
    def tearDownClass(self):
        print("end......")


    def test_01(self):
        # 查看客户账号列表
        Log().info("查看客户账号列表")

        F = Funciton()
        request_info = F.get_request_info(21)
        actual_result = F.public_method("21").status_code  # int
        expected_results = int(request_info[6])  # int
        F.result_assertion(expected_results, actual_result, "21")
        try:
            self.assertEqual(expected_results, actual_result)
        except Exception as msg:
            Log().info("Exception:" + F.public_method("21").json()['msg'])
            raise msg


    def test_02(self):
        # 新增客户管理员查询已有客户
        Log().info("新增客户管理员查询已有客户")

        F = Funciton()
        request_info = F.get_request_info(22)
        actual_result = F.public_method("22").status_code  # int
        expected_results = int(request_info[6])  # int
        F.result_assertion(expected_results, actual_result, "22")
        try:
            self.assertEqual(expected_results, actual_result)
        except Exception as msg:
            Log().info("Exception:" + F.public_method("22").json()['msg'])
            raise msg


    def test_03(self):
        # 新增客户管理员
        Log().info("新增客户管理员")

        F = Funciton()
        request_info = F.get_request_info(23)
        dict=json.loads(request_info[5])
        dict["userName"]="yijikehu"+self.randomnu+"-"+self.randomnu+""
        str_dict=json.dumps(dict)    # 这里转换不能直接用 str(dict)，会使字典格式属性和值单双引号不一致
        writeExcel("test_agent.xlsx","F23",str_dict)
        request_info = F.get_request_info(23)
        actual_result = F.public_method("23").status_code  # int
        expected_results = int(request_info[6])  # int
        F.result_assertion(expected_results, actual_result, "23")
        try:
            self.assertEqual(expected_results, actual_result)
        except Exception as msg:
            Log().info("Exception:" + F.public_method("23").json()['msg'])
            raise msg


    def test_04(self):
        # 修改客户管理员
        Log().info("修改客户管理员")

        F = Funciton()
        request_info = F.get_request_info(24)
        actual_result = F.public_method("24").status_code  # int
        expected_results = int(request_info[6])  # int
        F.result_assertion(expected_results, actual_result, "24")
        try:
            self.assertEqual(expected_results, actual_result)
        except Exception as msg:
            Log().info("Exception:" + F.public_method("24").json()['msg'])
            raise msg


    def test_05(self):
        # 客户重置密码
        Log().info("客户重置密码")

        F = Funciton()
        request_info = F.get_request_info(25)
        actual_result = F.public_method("25").status_code  # int
        expected_results = int(request_info[6])  # int
        F.result_assertion(expected_results, actual_result, "25")
        try:
            self.assertEqual(expected_results, actual_result)
        except Exception as msg:
            Log().info("Exception:" + F.public_method("25").json()['msg'])
            raise msg


    def test_06(self):
        # 查询代理商管理员列表
        Log().info("查询代理商管理员列表")

        F = Funciton()
        request_info = F.get_request_info(26)
        actual_result = F.public_method("26").status_code  # int
        expected_results = int(request_info[6])  # int
        F.result_assertion(expected_results, actual_result, "26")
        try:
            self.assertEqual(expected_results, actual_result)
        except Exception as msg:
            Log().info("Exception:" + F.public_method("26").json()['msg'])
            raise msg


    def test_07(self):
        # 新增代理商管理员
        Log().info("新增代理商管理员")
        F = Funciton()

        request_info = F.get_request_info(27)
        dict = json.loads(request_info[5])
        dict["account"] = "yjgl" + self.randomnu + "-" + self.randomnu + ""
        str_dict = json.dumps(dict)  # 这里转换不能直接用 str(dict)，会使字典格式属性和值单双引号不一致
        writeExcel("test_agent.xlsx", "F27", str_dict)
        request_info = F.get_request_info(27)
        actual_result = F.public_method("27").status_code  # int
        expected_results = int(request_info[6])  # int
        F.result_assertion(expected_results, actual_result, "27")
        try:
            self.assertEqual(expected_results, actual_result)
        except Exception as msg:
            Log().info("Exception:" + F.public_method("27").json()['msg'])
            raise msg


    def test_08(self):
        # 修改代理商管理员
        Log().info("修改代理商管理员")

        F = Funciton()
        request_info = F.get_request_info(28)
        actual_result = F.public_method("28").status_code  # int
        expected_results = int(request_info[6])  # int
        F.result_assertion(expected_results, actual_result, "28")
        try:
            self.assertEqual(expected_results, actual_result)
        except Exception as msg:
            Log().info("Exception:" + F.public_method("28").json()['msg'])
            raise msg


    def test_09(self):
        # 代理商重置密码
        Log().info("代理商重置密码")

        F = Funciton()
        request_info = F.get_request_info(29)
        actual_result = F.public_method("29").status_code  # int
        expected_results = int(request_info[6])  # int
        F.result_assertion(expected_results, actual_result, "29")
        try:
            self.assertEqual(expected_results, actual_result)
        except Exception as msg:
            Log().info("Exception:" + F.public_method("29").json()['msg'])
            raise msg


    def test_10(self):
        # 查看消息通知列表
        Log().info("查看消息通知列表")

        F = Funciton()
        request_info = F.get_request_info(30)
        actual_result = F.public_method("30").status_code  # int
        expected_results = int(request_info[6])  # int
        F.result_assertion(expected_results, actual_result, "30")
        try:
            self.assertEqual(expected_results, actual_result)
        except Exception as msg:
            Log().info("Exception:" + F.public_method("30").json()['msg'])
            raise msg


if __name__ == '__main__':
    unittest.main()