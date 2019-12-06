#encoding=utf-8
import time,traceback,unittest,json,ast    # ast:str转换dic
from datetime import datetime, timedelta
from function.request_api import send_request
from function.excelUtils import *
from function.Body import *
from function.Header import *
from function.Logfz import Log

# test_case 测试调用

class Funciton(unittest.TestCase):

    datainfo="test_agent.xlsx"

    def public_method(self,readnum,writenum):
        # 测试用例整体调用方法，n：rownum、current_time：获取当前时间

        current_time = time.strftime("%Y/%m/%d-%H:%M:%S")
        request_info = pd_readExcel(self.datainfo, readnum)
        url = Body().test_url + request_info[4]
        header=Token().test_agent_header
        try:
            # 顺序依次：method、url、header、param(data)
            self.r = send_request(request_info[3], url, header, str(request_info[5]))
            actual_result = self.r.status_code    # int
            expected_results = int(request_info[6])   # int
            self.result_assertion(expected_results,actual_result,writenum)
            self.assertEqual(expected_results, actual_result)
        except:
            traceback.print_exc()
            Log().info("Exception:" + self.r.json()['msg'])
        finally:
            writeExcel(self.datainfo, "J" + writenum, current_time)


    def result_assertion(self,expected_results, actual_result, writenum):
        # 断言

        # self.assertEqual(int(readExcel(self.datainfo,"G"+n)),actual_result)
        if expected_results == actual_result:
            writeExcel(self.datainfo, "H" + writenum, actual_result)
            writeExcel(self.datainfo, "I" + writenum, "pass")
        else:
            writeExcel(self.datainfo, "H" + writenum, str(actual_result) + " (" + self.r.json()['msg'] + ")")
            writeExcel(self.datainfo,"I" + writenum, "fail")

    def excel_value(self,n):
        # 读取参入，更改入参日期后写入

        now = datetime.now()
        delta1 = timedelta(days=1)
        delta7 = timedelta(days=7)  # days可以为正负数，当为负数时，n_days_after 与n_days_forward 的值与正数时相反；
        one_days_forward = now - delta1  # 当前日期推迟1天之后的时间
        seven_days_forward = now - delta7  # 当前日期向前推7天的时间

        F_value=readExcel(self.datainfo, "F" + n)
        # str 转换 dic
        F_value_dict = ast.literal_eval(F_value)

        if F_value_dict["type"]==0 or F_value_dict["type"]==4:
            F_value_dict["endDate"] = one_days_forward.strftime('%Y-%m-%d')
        else:
            F_value_dict["startDate"]=seven_days_forward.strftime('%Y-%m-%d')
            F_value_dict["endDate"] = one_days_forward.strftime('%Y-%m-%d')
        # dic 转换 str 写入
        str_F_value=json.dumps(F_value_dict)
        writeExcel(self.datainfo,  "F" + n, str_F_value)
        # print("success")



if __name__ == '__main__':

    Funciton().public_method(12,"12")