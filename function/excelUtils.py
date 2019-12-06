#encoding=utf-8
import os,csv
import xlwings as xw
from itertools import islice
import pandas as pd



def getFilePath(filename):
    # 获取data文件地址
    basePath = os.path.dirname(__file__)
    filePath = basePath.replace("function", "data\\" + filename)
    return filePath


def readExcel(filename,rowcell):
    # 读取Excel文件

    filePath=getFilePath(filename)
    # 打开excel文件读取内容
    app = xw.App(visible=False,add_book=False)
    datas=app.books.open(filePath)
    sheet1=datas.sheets["Sheet1"]
    data=sheet1.range(rowcell).value
    datas.close()
    app.quit()
    return data


def writeExcel(filename,seat,actualresult):
    # 写入Excel文件

    filePath = getFilePath(filename)
    app = xw.App(visible=False, add_book=False)
    # 打开excel文件写入内容
    datas = app.books.open(filePath)
    sheet1 = datas.sheets["Sheet1"]
    sheet1.range(seat).value = actualresult
    datas.save()
    datas.close()
    app.quit()


def readCsv(filename):
    # 读取Csv文件

    filePath = getFilePath(filename)
    # 打开csv文件，跳过首行读取
    result=[]
    with open(filePath,'r') as file:
        data_table = csv.reader(file)
        for row in islice(data_table,1,None):
            result.append(row)
    return result


def writeCsv(filename,a,b):
    # 按列明写入Csv文件

    filePath = getFilePath(filename)
    # 字典中的key值即为csv中列名
    data = {'ActualResult': a}
    dataframe = pd.DataFrame(data, index=list(str(b)))  # index指定行的索引值
    dataframe.to_csv(filePath,mode='a+',columns=['ActualResult'])


def pd_readExcel(filename,row):
    # pandas读取excel指定行

    filePath = getFilePath(filename)
    # 默认读取到这个Excel的第一个表单
    datas = pd.DataFrame(pd.read_excel(filePath))
    # 0表示第一行 读取数据并不包含表头
    data = datas.loc[row-2].tolist()
    return data



# data=ExcelUtils().readCsv("testdata1.csv")
# print(data[1][1])

# print(type(readExcel("Interface_test.xlsx","Agent","F24")))
# print(type(readExcel("Interface_test.xlsx","Agent","F40")))

# a=pd_readExcel("test_agent.xlsx",20)
# print(a)


