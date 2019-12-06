#encoding=utf-8
import json,unittest

from case.cs_teacher.cs_teacher_function import *
from function.request_api import send_request
from function.excelUtils import *
from function.Logfz import Log


class StudentInfo(unittest.TestCase):
    # 学生 模块测试

    sheetpage = Body().test_teacher_sheet

    @classmethod
    def setUpClass(self):
        print("start......")

    @classmethod
    def tearDownClass(self):
        print("end......")

    def test_01(self):
        # 查询学生信息列表
        Log().info("查询学生信息列表")
        Funciton().public_method("20")


    def test_02(self):
        # 添加新学生
        Log().info("添加新学生")
        n = "21"
        json_data = [{"userName":"zhengzhouxuesheng"+Funciton().randomnu+"","realName":"zhengzhouxuesheng"+Funciton().randomnu+"",
                      "nickName":"xuesheng"+Funciton().randomnu+"","password":"111111"}]

        current_time = time.strftime("%Y/%m/%d-%H:%M:%S")
        try:
            # 顺序依次：method、url、header、param(data)
            r = send_request(readExcel(Funciton().datainfo, self.sheetpage, "D" + n),
                             Funciton().urltitle + readExcel(Funciton().datainfo, self.sheetpage, "E" + n),
                             Funciton().header, json.dumps(json_data))
            actual_result = r.status_code
            expected_results = int(readExcel(Funciton().datainfo, self.sheetpage, "G" + n))
            Funciton().result_assertion(expected_results, actual_result, n)
        except:
            traceback.print_exc()
        finally:
            writeExcel(Funciton().datainfo, self.sheetpage, "J" + n, current_time)


    def test_03(self):
        # 添加学生-查看从机构拉取列表
        Log().info("添加学生-查看从机构拉取列表")
        Funciton().public_method("22")


    # def test_04(self):
    #     # 从机构拉取添加学生
    #     Log().info("从机构拉取添加学生")
    #     Funciton().public_method("23")


    def test_05(self):
        # 重置密码
        Log().info("重置密码")
        Funciton().public_method("24")


    def test_06(self):
        # 移除学生
        pass


if __name__ == '__main__':
    unittest.main()