#encoding=utf-8
import unittest, random

from case.cs_agent.cs_agent_function import *
from function.request_api import send_request
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
        n="8"
        json_data={"name":"一级客户"+self.randomnu,"nickName":"一级客户"+self.randomnu,"realName":"一级客户"+self.randomnu,"code":"a"+Funciton().randomnu,"contact":"一级客户"+Funciton().randomnu,
                   "email":"13323132313@qq.com","password":"111111","confirmPwd":"111111","mobile":"13323132313","province":"41",
                   "city":"4101","district":"410103","address":"二七区","account":"wanghn1j-"+self.randomnu+"-"+self.randomnu,"schoolType": "7"}

        current_time = time.strftime("%Y/%m/%d-%H:%M:%S")
        url = Body().test_url + readExcel(Funciton().datainfo, "E" + n)
        try:
            # 顺序依次：method、url、header、param(data)
            r = send_request(readExcel(Funciton().datainfo, "D" + n), url,self.header, json.dumps(json_data))
            actual_result = r.status_code
            expected_results = int(readExcel(Funciton().datainfo, "G" + n))
            Funciton().result_assertion(expected_results,actual_result, n)
        except:
            traceback.print_exc()
        finally:
            writeExcel(Funciton().datainfo, "J" + n, current_time)


    def test_02(self):
        # 修改客户
        Log().info("修改客户")
        Funciton().public_method(9,"9")


    def test_03(self):
        # 查看客户详情
        Log().info("查看客户详情")
        Funciton().public_method(10,"10")


    def test_04(self):
        # 查看客户可见商品列表
        Log().info("查看班课设置列表")
        Funciton().public_method(11,"11")


    def test_05(self):
        # 查询客户下可见商品详情（附带租户的课数）
        Log().info("查询客户下可见商品详情（附带租户的课数）")
        Funciton().public_method(12,"12")


    def test_06(self):
        # 客户购买课程最近十次操作记录
        Log().info("客户购买课程最近十次操作记录")
        Funciton().public_method(13,"13")


    def test_07(self):
        # 客户购买课时
        Log().info("客户购买课时")
        Funciton().public_method(14,"14")


    def test_08(self):
        # 查看客户列表
        Log().info("查看客户列表")
        Funciton().public_method(34,"34")


    def test_09(self):
        # 客户列表导出
        Log().info("客户列表导出")
        Funciton().public_method(15,"15")


    def test_10(self):
        # 查看客户班课记录
        Log().info("查看客户班课记录")
        Funciton().public_method(16,"16")


if __name__ == '__main__':
    unittest.main()