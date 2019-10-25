#encoding=utf-8

from case.test_teacher.cs_teacher_function import *
from function.Logfz import Log


class GenernalInfo(Funciton):
    # 个人信息 模块测试

    @classmethod
    def setUpClass(self):
        print("start......")

    @classmethod
    def tearDownClass(self):
        print("end......")


    def test_01(self):
        # 修改个人基本信息
        Log().info("修改个人基本信息")
        Funciton().public_method("26")


    def test_02(self):
        # 个人信息修改密码
        Log().info("个人信息修改密码")
        Funciton().public_method("27")


    def test_03(self):
        # 获取手机验证码
        Log().info("获取手机验证码")
        Funciton().public_method("28")


    def test_04(self):
        # 查询央馆用户的userid
        Log().info("查询央馆用户的userid")
        Funciton().public_method("29")


    def test_05(self):
        # 老师反馈信息
        Log().info("老师反馈信息")
        Funciton().public_method("30")


if __name__ == '__main__':
    unittest.main()