#encoding=utf-8
import unittest, random

from case.cs_agent.cs_agent_function import *
from function.request_api import send_request
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
        Funciton().public_method(21,"21")


    def test_02(self):
        # 新增客户管理员查询已有客户
        Log().info("新增客户管理员查询已有客户")
        Funciton().public_method(22,"22")


    def test_03(self):
        # 新增客户管理员
        Log().info("新增客户管理员")
        n = "23"
        json_data = {"email":"13323132313@qq.com","password":"111111","confirmPwd":"111111","mobile":"13323132313",
                     "userName":"yijikehu-"+self.randomnu+"-"+self.randomnu+"","tenantId":31,
                     "realName":"一级"+self.randomnu,"nickName":"一级"+self.randomnu}

        current_time = time.strftime("%Y/%m/%d-%H:%M:%S")
        url = Body().test_url + readExcel(Funciton().datainfo, "E" + n)
        try:
            # 顺序依次：method、url、header、param(data)
            r = send_request(readExcel(Funciton().datainfo,"D" + n), url,self.header, json.dumps(json_data))
            actual_result = r.status_code
            expected_results = int(readExcel(Funciton().datainfo, "G" + n))
            Funciton().result_assertion(expected_results,actual_result, n)
        except:
            traceback.print_exc()
        finally:
            writeExcel(Funciton().datainfo,"J" + n, current_time)


    def test_04(self):
        # 修改客户管理员
        Log().info("修改客户管理员")
        Funciton().public_method(24,"24")


    def test_05(self):
        # 客户重置密码
        Log().info("客户重置密码")
        Funciton().public_method(25,"25")


    def test_06(self):
        # 查询代理商管理员列表
        Log().info("查询代理商管理员列表")
        Funciton().public_method(26,"26")


    def test_07(self):
        # 新增代理商管理员
        Log().info("新增代理商管理员")
        n = "27"
        json_data = {"email":"13323132313@qq.com","password":"111111","confirmPwd":"111111","contact":"13323132313",
                     "account":"yijiguanli-"+self.randomnu+"-"+self.randomnu+"","name":"一级管理"}

        current_time = time.strftime("%Y/%m/%d-%H:%M:%S")
        url = Body().test_url + readExcel(Funciton().datainfo, "E" + n)
        try:
            # 顺序依次：method、url、header、param(data)
            r = send_request(readExcel(Funciton().datainfo, "D" + n),url,self.header, json.dumps(json_data))
            actual_result = r.status_code
            expected_results = int(readExcel(Funciton().datainfo, "G" + n))
            Funciton().result_assertion(expected_results, actual_result, n)
        except:
            traceback.print_exc()
        finally:
            writeExcel(Funciton().datainfo, "J" + n, current_time)


    def test_08(self):
        # 修改代理商管理员
        Log().info("修改代理商管理员")
        Funciton().public_method(28,"28")


    def test_09(self):
        # 代理商重置密码
        Log().info("代理商重置密码")
        Funciton().public_method(29,"29")


    def test_10(self):
        # 查看消息通知列表
        Log().info("查看消息通知列表")
        Funciton().public_method(30,"30")


if __name__ == '__main__':
    unittest.main()