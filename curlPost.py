# -*- coding: utf-8 -*- 
import urllib
import urllib2
import json


#发起请求的url
post_url = '10.16.77.216:50096/v1/curl/post';
 
postData  = {'a':'aaa','b':'bbb','c':'ccc','d':'ddd'}

#json序列化
data = json.dumps(postData)

req = urllib2.Request(post_url)
# response = urllib2.urlopen(req,urllib.urlencode({'sku_info':data}))
response = urllib2.urlopen(req,data)
 
#打印返回值
print response.read()