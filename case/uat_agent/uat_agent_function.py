#encoding=utf-8

import time,traceback,random,unittest
from function.request_api import send_request
from function.excelUtils import *
from function.Body import *
from function.Header import *
from function.Logfz import Log

# test_case 测试调用

class Funciton(unittest.TestCase):

    datainfo="uat_agent.xlsx"
    randomnu=str(random.randint(0,1000))   # 随机数产生

    def public_method(self,n):
        # 测试用例整体调用方法，n：rownum、current_time：获取当前时间

        current_time = time.strftime("%Y/%m/%d-%H:%M:%S")
        header=Token().uat_agent_header
        url=Body().uat_url+readExcel(self.datainfo, "E" + n)

        try:
            # 顺序依次：method、url、header、param(data)
            self.r = send_request(readExcel(self.datainfo,"D" + n), url,header, readExcel(self.datainfo,"F" + n))
            actual_result = self.r.status_code
            expected_results = int(readExcel(self.datainfo,"G" + n))
            self.result_assertion(expected_results,actual_result,n)
            self.assertEqual(int(readExcel(self.datainfo, "G" + n)), actual_result)
        except:
            traceback.print_exc()
            Log().info("Exception:" + self.r.json()['msg'])
        finally:
            writeExcel(self.datainfo, "J" + n, current_time)


    def result_assertion(self,expected_results, actual_result, n):
        # 断言

        # self.assertEqual(int(readExcel(self.datainfo,"G"+n)),actual_result)
        if expected_results == actual_result:
            writeExcel(self.datainfo, "H" + n, actual_result)
            writeExcel(self.datainfo, "I" + n, "pass")
        else:
            writeExcel(self.datainfo, "H" + n, str(actual_result) + " (" + self.r.json()['msg'] + ")")
            writeExcel(self.datainfo, "I" + n, "fail")


if __name__ == '__main__':

    pass