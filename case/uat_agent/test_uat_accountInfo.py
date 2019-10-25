#encoding=utf-8
import unittest, json

from case.uat_agent.uat_agent_function import *
from function.request_api import send_request
from function.excelUtils import *
from function.Logfz import Log



class AccountInfo(unittest.TestCase):
    # 账号管理、消息通知功能模块 测试

    sheetpage = Body().uat_agent_sheet

    @classmethod
    def setUpClass(self):
        print("start......")

    @classmethod
    def tearDownClass(self):
        print("end......")


    def test_01(self):
        # 查看客户账号列表
        Log().info("查看客户账号列表")
        Funciton().public_method("21")


    def test_02(self):
        # 新增客户管理员查询已有客户
        Log().info("新增客户管理员查询已有客户")
        Funciton().public_method("22")


    def test_03(self):
        # 新增客户管理员
        Log().info("新增客户管理员")
        n = "23"
        json_data = {"email":"","password":"111111","confirmPwd":"111111","mobile":"13323132313",
                     "userName":"jilin1j-"+Funciton().randomnu+"-"+Funciton().randomnu+"","tenantId":268,
                     "realName":"吉一级管员"+Funciton().randomnu,"nickName":"吉管"+Funciton().randomnu}

        current_time = time.strftime("%Y/%m/%d-%H:%M:%S")
        try:
            # 顺序依次：method、url、header、param(data)
            r = send_request(readExcel(Funciton().datainfo,self.sheetpage,"D" + n), Funciton().urltitle + readExcel(Funciton().datainfo,self.sheetpage, "E" + n),
                             Funciton().header, json.dumps(json_data))
            actual_result = r.status_code
            expected_results = int(readExcel(Funciton().datainfo,self.sheetpage, "G" + n))
            Funciton().result_assertion(expected_results,actual_result,n)
        except:
            traceback.print_exc()
        finally:
            writeExcel(Funciton().datainfo,self.sheetpage,"J" + n, current_time)


    def test_04(self):
        # 修改客户管理员
        Log().info("修改客户管理员")
        Funciton().public_method("24")


    def test_05(self):
        # 客户重置密码
        Log().info("客户重置密码")
        Funciton().public_method("25")


    def test_06(self):
        # 查询代理商管理员列表
        Log().info("查询代理商管理员列表")
        Funciton().public_method("26")


    def test_07(self):
        # 新增代理商管理员
        Log().info("新增代理商管理员")
        n = "27"
        json_data = {"email":"","password":"111111","confirmPwd":"111111","contact":"13323132313",
                     "account":"jilin1j-"+Funciton().randomnu+"-"+Funciton().randomnu+"","name":"吉一管理"}

        current_time = time.strftime("%Y/%m/%d-%H:%M:%S")
        try:
            # 顺序依次：method、url、header、param(data)
            r = send_request(readExcel(Funciton().datainfo,self.sheetpage, "D" + n),
                             Funciton().urltitle + readExcel(Funciton().datainfo,self.sheetpage,"E" + n),
                             Funciton().header, json.dumps(json_data))
            actual_result = r.status_code
            expected_results = int(readExcel(Funciton().datainfo,self.sheetpage, "G" + n))
            Funciton().result_assertion(expected_results,actual_result,  n)
        except:
            traceback.print_exc()
        finally:
            writeExcel(Funciton().datainfo,self.sheetpage, "J" + n, current_time)


    def test_08(self):
        # 修改代理商管理员
        Log().info("修改代理商管理员")
        Funciton().public_method("28")


    def test_09(self):
        # 代理商重置密码
        Log().info("代理商重置密码")
        Funciton().public_method("29")


    def test_10(self):
        # 查看消息通知列表
        Log().info("查看消息通知列表")
        Funciton().public_method("30")


if __name__ == '__main__':
    unittest.main()