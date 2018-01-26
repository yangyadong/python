# -*- coding: UTF-8 -*-
import xlrd,logging,json,requests,urllib
import urllib.parse,urllib.request
# import importlib,sys

class curlDemo:
    """docstring for curlDemo"""
    headers = {
        'Cookie': "COFFEE_TOKEN=2e1509d2-2263-44c0-9d1c-f956a4f5b037",
        'Content-Type': "application/x-www-form-urlencoded",
        'Cache-Control': "no-cache",
    }

    def __init__(self, path, index):
        self.path = path
        self.index = index

    def initLog(self):
        # importlib.reload(sys)
        #定义日志输出
        logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                        datefmt='%a, %d %b %Y %H:%M:%S',
                        filename='myapp.log',
                        filemode='w')
        #定义一个StreamHandler，将INFO级别或更高的日志信息打印到标准错误，并将其添加到当前的日志处理对象#
        console = logging.StreamHandler()
        console.setLevel(logging.INFO)
        formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
        console.setFormatter(formatter)
        logging.getLogger('').addHandler(console)

    def curlPost(self, name, url, params, headers, error_no):
        print("***********开始执行请求"+name+"************") 
        logging.info("url"+url)
        logging.info("params"+params)
        logging.info("headers"+urllib.parse.urlencode(headers))
        url2 = urllib.request.Request(url,params)
        response = urllib.request.urlopen(url2)
        logging.info(response)
        apicontent = response.read()
        logging.info(apicontent)
        apicontent = json.loads(apicontent)
        #验证返回值
        if apicontent["error_no"]==int(error_no):
            logging.info(name+"测试通过")
            print(name+"测试通过")
        else:
            logging.info(name+"测试通过")
            print(name+"测试失败")
        print("***********请求执行完成************") 

    def readData(self, path, index):
        data = xlrd.open_workbook(path)#打开excel表格
        logging.info("打开%s excel表格成功"%data)
        #table = data.sheet_by_name(u'Sheet2')#打开工作表sheet1
        table = data.sheet_by_index(index) 
        logging.info("打开%s表成功"%table)
        nrows = table.nrows#统计行数
        logging.info("表中有%s行"%nrows)
        ncols = table.ncols#统计列数
        logging.info("表中有%s列"%ncols)
        logging.info("开始进行循环")
        name_1=[];url_1=[];params_1=[];type_1=[];Expected_result_1=[]
        Actual_result_1 =[];test_result_1=[];Remarks_1=[]#定义数组
        for i in range(1,nrows):#遍历excel表格，重第一行开始
            cell_A3 =table.row_values(i)
            #获取excel表格中的数据
            name     = cell_A3[0]
            url      = cell_A3[1]
            params   = eval(cell_A3[2])
            params   = urllib.parse.urlencode(params)
            curlType = cell_A3[3]
            errorNo  = cell_A3[4]
            headers  = cell_A3[6]
            if headers == '':
                headers = self.headers
            self.curlPost(name,url,params,headers,errorNo)

    def run(self):
        self.initLog()
        self.readData(self.path,self.index)

obj = curlDemo('./curl.xlsx',0)
obj.run()
