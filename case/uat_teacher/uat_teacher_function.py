#encoding=utf-8

import time,traceback,random,unittest
from function.request_api import send_request
from function.excelUtils import *
from function.Body import *
from function.Header import *
from function.Logfz import Log

# test_case 测试调用

class Funciton(unittest.TestCase):

    datainfo="uat_teacher.xlsx"
    urltitle=Body().uat_url
    randomnu=str(random.randint(0,1000))   # 随机数产生


    def public_method(self,n):
        # 测试用例整体调用方法，n：rownum、current_time：获取当前时间

        current_time = time.strftime("%Y/%m/%d-%H:%M:%S")
        header=Token().uat_teacher_header
        method=readExcel(self.datainfo,"D" + n)
        url_title=readExcel(self.datainfo, "E" + n)
        param=readExcel(self.datainfo, "F" + n)

        try:
            # 顺序依次：method、url、header、param(data)
            self.r = send_request(method, self.urltitle + url_title,header,param )
            actual_result = self.r.status_code
            expected_results = int(readExcel(self.datainfo, "G" + n))
            self.result_assertion(expected_results, actual_result, n)
            self.assertEqual(int(readExcel(self.datainfo,  "G" + n)), actual_result)
        except:
            traceback.print_exc()
            Log().info("Exception:"+self.r.json()['msg'])
        finally:
            writeExcel(self.datainfo, "J" + n, current_time)


    def result_assertion(self,expected_results, actual_result, n):
        # 断言,在Excel中写入结果

        # self.assertEqual(int(readExcel(self.datainfo,self.sheetpage,"G"+n)),actual_result)
        if expected_results == actual_result:
            writeExcel(self.datainfo, "H" + n, actual_result)
            writeExcel(self.datainfo, "I" + n, "pass")
        else:
            writeExcel(self.datainfo, "H" + n, str(actual_result) + " (" + self.r.json()['msg'] + ")")
            writeExcel(self.datainfo, "I" + n, "fail")


if __name__ == '__main__':

    Funciton().public_method("7")