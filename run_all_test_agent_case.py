#encoding=utf-8
import unittest


if __name__ == '__main__':

    # 默认的测试用例加载器 defaultTestLoader
    suite = unittest.defaultTestLoader.discover('./case/uat_teacher', pattern='test*.py')
    # 执行集合test用例文件
    unittest.TextTestRunner().run(suite)