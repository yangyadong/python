# -*- coding: UTF-8 -*-
import pymysql
import  pymysql.cursors

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='123456',
                             db='test1',
                             port=3306,
                             charset='utf8')#注意是utf8不是utf-8
try:
    with connection.cursor() as cursor:
        count = 1
        while (count <= 200000):
            sql_2 = 'delete from test1 where `id`='+str(count)
            cout_2 = cursor.execute(sql_2)
            if cout_2!=1:
                print(count)
            count = count + 1
        
        connection.commit()
        # sql_1 = 'select count(*) from test1'
        # cout_1=cursor.execute(sql_1)
        # print(cout_1)
        # for row in cursor.fetchall():
        #     print("id:",str(row[0]),'name',str(row[1]),'age',str(row[2]))
        
finally:
    connection.close()