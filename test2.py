# -*- coding: UTF-8 -*-
import xlrd,logging,urllib,urllib2,json,sys,requests
from pylsy import pylsytable


#######################################################################################################
#定义系统输出编码
reload(sys)
sys.setdefaultencoding('utf-8')

#########################################################################################################
#定义日志输出
logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='myapp.log',
                filemode='w')

#################################################################################################
#定义一个StreamHandler，将INFO级别或更高的日志信息打印到标准错误，并将其添加到当前的日志处理对象#
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)
#################################################################################################


#url1 = requests.get("http://www.baidu.com")
#print(url1.text)



###################################################################################################
#处理excel表格
data = xlrd.open_workbook('/Users/baidu/Documents/test.xlsx')#打开excel表格
logging.info("打开%s excel表格成功"%data)
#table = data.sheet_by_name(u'Sheet2')#打开工作表sheet1
table = data.sheet_by_index(0) 
logging.info("打开%s表成功"%table)
nrows = table.nrows#统计行数
logging.info("表中有%s行"%nrows)
ncols = table.ncols#统计列数
logging.info("表中有%s列"%ncols)
logging.info("开始进行循环")
name_1=[];url_1=[];params_1=[];type_1=[];Expected_result_1=[];Actual_result_1 =[];test_result_1=[];Remarks_1=[]#定义数组
Success=0;fail=0           #初始化成功失败用例
##################################################################################################################
for i in range(1,nrows):#遍历excel表格
    cell_A3 =table.row_values(i)
#获取excel表格中的数据
    name    = cell_A3[0]
    url    = cell_A3[1]
    params=eval(cell_A3[2])


    type   = cell_A3[3]
    error_no =cell_A3[4]
    Remarks =cell_A3[5]
    logging.info(url)
#############################################################################################################################3
    params =urllib.urlencode(params)  #参数化处理
    #params = json.JSONEncoder().encode(params)
    logging.info(params)
    

    headers = {
        'Cookie': "COFFEE_TOKEN=2e1509d2-2263-44c0-9d1c-f956a4f5b037",
        'Content-Type': "application/x-www-form-urlencoded",
        'Cache-Control': "no-cache",
        'Postman-Token': "fe2f5a7e-4e56-c696-17ee-13e6d804a10b"
   }
   

  #  headers = {"COFFEE_TOKEN":"2e1509d2-2263-44c0-9d1c-f956a4f5b037"}
    print url
    print params
    print headers
    url2 = urllib2.Request(url,params,headers)
    print("***********开始执行请求************") 
    response = urllib2.urlopen(url2)
    #response=requests.post(url,files=files)
    logging.info(response)
    apicontent = response.read()
    logging.info(apicontent)
    apicontent = json.loads(apicontent)
    #验证返回值
    if apicontent["error_no"]==int(error_no):
        name2="通过"
        print(name+"测试通过")
    else:
        name2="失败"
        print(name+"测试失败")
    name_1.append(name)
    url_1.append(url)
    params_1.append(params)
    type_1.append(type)
    Expected_result_1.append(int(error_no))
    Actual_result_1.append(apicontent["error_no"])
    test_result_1.append(name2)
    Remarks_1.append(Remarks)
    if name2=="通过":
        Success+=1
    elif name2=="失败":
        fail +=1
    else:
        print("测试结果异常")

##############################################################################################################################
#输出表格形式
attributes =["urlname","url","params","type","Expected_result","Actual_result","test_result","Remarks"]
table =pylsytable(attributes)
name =name_1
url =url_1
params=params_1
type=type_1
Expected_result=Expected_result_1
Actual_result =Actual_result_1
test_result=test_result_1
Remarks=Remarks_1
table.add_data("urlname",name)
table.add_data("url",url)
table.add_data("params",params)
table.add_data("type",type)
table.add_data("Expected_result",Expected_result)
table.add_data("Actual_result",Actual_result)
table.add_data("test_result",test_result)
table.add_data("Remarks",Remarks)
table._create_table()
print(table)
print("成功的用例个数为：%s"%Success,"失败的用例个数为：%s"%fail)
print("***********执行测试成功************")
