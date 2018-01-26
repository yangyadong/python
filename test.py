# -*- coding: utf-8 -*- 
import requests
import unittest
import json

class MyTest(unittest.TestCase):  # 封装测试环境的初始化和还原的类
    def setUp(self):
        print("start test")

    def tearDown(self):
        print("end test")

class Test_transapi(MyTest):  # 把一个接口封装一个类，下面的方法是具体的测试用例执行

    @staticmethod
    def getParams():
        Data = open(r"F:\TestData0618.json").read()
        temp = eval(Data)   #type(Data)为str,type(temp)为dict
        data = temp['2100']
        return data

    def test_transapi(self):
        self.url = "http://fanyi.baidu.com/v2transapi"
        self.headers = {
            'Host': 'fanyi.baidu.com',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, sdch, br',
            'Accept-Language': 'zh-CN,zh;q=0.8',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive'}
        data = self.getParams()
        for i in data:
            print i
            self.params = i
            #print u'参数：',self.params
            #s = requests.session()
            #login_data = {'userid':'用户名','password':'密码'}  对于有鉴权的接口需要在请求的时候加上以上两句注释
            r = requests.get(url=self.url, params=self.params,headers=self.headers)
            #print (r.text)
            print (r.status_code)
            #print type(r.status_code)
            self.assertEqual(200,r.status_code)

if __name__=="__main__":
    unittest.main()