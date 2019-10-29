#encoding=utf-8

import time,traceback,random,unittest
from function.request_api import send_request
from function.excelUtils import *
from function.Body import *
from function.Header import *

# test_case 测试调用

class Funciton(unittest.TestCase):

    datainfo="Interface_test.xlsx"
    urltitle=Body().uat_url
    header=Token().uat_teacher_header
    sheetpage=Body().uat_teacher_sheet
    randomnu=str(random.randint(0,1000))   # 随机数产生


    def public_method(self,n):
        # 测试用例整体调用方法，n：rownum、current_time：获取当前时间

        current_time = time.strftime("%Y/%m/%d-%H:%M:%S")
        method=readExcel(self.datainfo,self.sheetpage,"D" + n)
        url_title=readExcel(self.datainfo,self.sheetpage, "E" + n)
        param=readExcel(self.datainfo,self.sheetpage, "F" + n)

        try:
            # 顺序依次：method、url、header、param(data)
            self.r = send_request(method, self.urltitle + url_title,self.header,param )
            actual_result = self.r.status_code
            expected_results = int(readExcel(self.datainfo,self.sheetpage, "G" + n))
            self.result_assertion(expected_results, actual_result, n)
            self.assertEqual(int(readExcel(self.datainfo, self.sheetpage, "G" + n)), actual_result)
        except:
            traceback.print_exc()
            print("Exception:"+self.r.json()['msg'])
        finally:
            writeExcel(self.datainfo, self.sheetpage,"J" + n, current_time)


    def result_assertion(self,expected_results, actual_result, n):
        # 断言,在Excel中写入结果

        # self.assertEqual(int(readExcel(self.datainfo,self.sheetpage,"G"+n)),actual_result)
        if expected_results == actual_result:
            writeExcel(self.datainfo,self.sheetpage, "H" + n, actual_result)
            writeExcel(self.datainfo,self.sheetpage, "I" + n, "pass")
        else:
            writeExcel(self.datainfo,self.sheetpage, "H" + n, str(actual_result) + " (" + self.r.json()['msg'] + ")")
            writeExcel(self.datainfo,self.sheetpage, "I" + n, "fail")


if __name__ == '__main__':

    Funciton().public_method("7")