#encoding=utf-8
import unittest

from case.test_teacher.cs_teacher_function import *
from function.Logfz import Log


class CourseInfo(unittest.TestCase):
    # 课程目录 模块测试

    @classmethod
    def setUpClass(self):
        print("start......")

    @classmethod
    def tearDownClass(self):
        print("end......")

    def test_01(self):
        # 查询班级下的课程目录（包含章节和课时）
        Log().info("查询班级下的课程目录（包含章节和课时）")
        Funciton().public_method("6")


    def test_02(self):
        # 课时锁定
        Log().info("课时锁定")
        Funciton().public_method("7")


    def test_03(self):
        # 查看课时详情
        Log().info("查看课时详情")
        Funciton().public_method("8")


    def test_04(self):
        # 查看课时详情（老师指导手册）
        Log().info("查看课时详情（老师指导手册）")
        Funciton().public_method("9")


    def test_05(self):
        # 查看课时详情（演示视频）
        Log().info("查看课时详情（演示视频）")
        Funciton().public_method("10")


    def test_06(self):
        # 查看课时详情（演示PPT）
        Log().info("查看课时详情（演示PPT）")
        Funciton().public_method("11")


    def test_07(self):
        # 查看课时详情（课堂测验解析）
        Log().info("查看课时详情（课堂测验解析）")
        Funciton().public_method("12")


    def test_08(self):
        # 查看课时详情（学生任务进度）
        Log().info("查看课时详情（学生任务进度）")
        Funciton().public_method("13")


if __name__ == '__main__':
    unittest.main()