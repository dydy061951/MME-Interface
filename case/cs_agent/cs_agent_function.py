# encoding=utf-8
import time,json, ast  # ast:str转换dic
from datetime import datetime, timedelta
from function.request_api import send_request
from function.excelUtils import readExcel, writeExcel, pd_readExcel
from function.Body import *
from function.Header import *


# test_case 测试调用

class Funciton:
    datainfo = "test_agent.xlsx"


    def get_request_info(self,readnum):
        # 获取测试用例数据

        self.request_info = pd_readExcel(self.datainfo, readnum)
        return self.request_info


    def public_method(self,writenum):
        # 测试用例整体调用方法，readnum：rownum、current_time：获取当前时间

        current_time = time.strftime("%Y/%m/%d-%H:%M:%S")
        # 读取excel整行数据
        url = Body().test_url + self.request_info[4]
        header = Token().test_agent_header

        # 顺序依次：method、url、header、param(data)
        self.r = send_request(self.request_info[3], url, header, str(self.request_info[5]))
        writeExcel(self.datainfo, "J" + writenum, current_time)
        return self.r


    def result_assertion(self, expected_results, actual_result, writenum):
        # 断言

        # self.assertEqual(int(readExcel(self.datainfo,"G"+n)),actual_result)
        if expected_results == actual_result:
            writeExcel(self.datainfo, "H" + writenum, actual_result)
            writeExcel(self.datainfo, "I" + writenum, "pass")
        else:
            writeExcel(self.datainfo, "H" + writenum, str(actual_result) + " (" + self.r.json()['msg'] + ")")
            writeExcel(self.datainfo, "I" + writenum, "fail")


    def excel_value(self, n):
        # 读取参入，更改入参日期后写入

        now = datetime.now()
        delta1 = timedelta(days=1)
        delta7 = timedelta(days=7)  # days可以为正负数，当为负数时，n_days_after 与n_days_forward 的值与正数时相反；
        one_days_forward = now - delta1  # 当前日期推迟1天之后的时间
        seven_days_forward = now - delta7  # 当前日期向前推7天的时间

        F_value = readExcel(self.datainfo, "F" + n)
        # str 转换 dic
        F_value_dict = ast.literal_eval(F_value)

        if F_value_dict["eventId"] == 1002 or F_value_dict["eventId"] == 1007:
            F_value_dict["endDate"] = one_days_forward.strftime('%Y-%m-%d')
        else:
            F_value_dict["startDate"] = seven_days_forward.strftime('%Y-%m-%d')
            F_value_dict["endDate"] = one_days_forward.strftime('%Y-%m-%d')
        # dic 转换 str 写入
        str_F_value = json.dumps(F_value_dict)
        writeExcel(self.datainfo, "F" + n, str_F_value)


if __name__ == '__main__':
    a=Funciton().get_request_info(18)
    print(a)