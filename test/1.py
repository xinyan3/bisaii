# -*- coding:utf-8 -*-
# __author__ = "www.iplaypy.com"

# 普通python函数


def func(a, b, c):
    return a + b + c


print(func(1, 2, 3))
# 返回值为6

# lambda匿名函数


def f(a, b, c): return a + b + c


print(f(1, 2, 3))
# 返回结果为6
foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]
print(filter(lambda x: x % 3 == 0, foo).__next__())
import names as n
print((lambda y: y + 4)(4))
pass
print((lambda x, y: x * y)(10, 20))
print(foo.__class__)
print((foo.__class__).__class__)
#导入数据库包文件
import pymysql.cursors
"""创建数据库链接
   host：数据库地址
   port：数据库端口（非str，不用引号）
   user，password：用户名密码
   charset：编码
   cursorclass：游标类

   设置相关属性
"""
connection=pymysql.connect(host='localhost',
                           port=3307,
                           user="root",
                           password="123456",
                           charset='utf8mb4',
                           cursorclass=pymysql.cursors.DictCursor)
#使用粗认识偶然方法创建游标对象cursor
cursor=connection.cursor()
#使用游标方法execute方法查询数据库版本
cursor.execute("SELECT VERSION()")
#使用fetchone方法获取单条数据
data=cursor.fetchone()
#打印单条数据
print("database version is : %s"%data)
#关闭数据库连接
connection.close()
import json

# Python 字典类型转换为 JSON 对象
data = {
    'no' : 1,
    'name' : 'Runoob',
    'url' : 'http://www.runoob.com'
}

json_str = json.dumps(data)
print ("Python 原始数据：", repr(data))
print ("JSON 对象：", json_str)
for i in range(1, 10):
        for j in range(1, i+1):
            print('{}x{}={}\t'.format(i, j, i*j), end='')
        print()

# -*- coding:utf-8 -*-
import pymysql as MySQLdb
import os


def createDatabase():
    try:
        conn = MySQLdb.connect(host='127.0.0.1', user='root', passwd='123456', port=3307, charset="UTF8")
        cur = conn.cursor()
        cur.execute('create database if not exists dht')
        conn.select_db('dht')
        cur.execute('drop table if exists hash_info')
        cur.execute('drop table if exists peerIP')
        cur.execute('create table hash_info(hash varchar(40), info varchar(100),primary key(hash))')
        cur.execute('create table peerIP(ip varchar(40), info varchar(100),primary key(ip))')
        conn.commit()
        cur.close()
        conn.close()
    except MySQLdb.Error as e:
        print(('mysql error %d:%s' % (e.args[0], e.args[1])))


def insertInfo(hash):
    try:
        conn = MySQLdb.connect(host='127.0.0.1', user='root', passwd='123456', port=3307, charset="UTF8")
        cur = conn.cursor()
        conn.select_db('dht')
        sql = "insert into hash_info(hash,info) values('%s','%s')" % (hash, "the info will added later")
        cur.execute(sql)
        conn.commit()
        cur.close()
        conn.close()
    except MySQLdb.Error as e:
        print('mysql error %d:%s' % (e.args[0], e.args[1]))


def selectAllTable(table):
    try:
        conn = MySQLdb.connect(host='127.0.0.1', user='root', passwd='123456', port=3307, charset="UTF8")
        cur = conn.cursor()
        conn.select_db('dht')
        sql = "select * from " + table
        count = cur.execute(sql)
        print("thers are %s row in table:" % count)
        result = cur.fetchall()

        for r in result:
            # print 'magnet:?xt=urn:btih:'+r[0].upper()+" info:"+r[1]
            if r[1] != "error" and r[1] != "":
                print(r[1])
        conn.commit()
        cur.close()
        conn.close()
    except MySQLdb.Error as e:
        print('mysql error %d:%s' % (e.args[0], e.args[1]))


def executeSQL(sql):
    try:
        conn = MySQLdb.connect(host='127.0.0.1', user='root', passwd='456', port=3307, charset="UTF8")
        cur = conn.cursor()
        conn.select_db('dht')
        cur.execute(sql)
        conn.commit()
        cur.close()
        conn.close()
    except MySQLdb.Error as e:
        print('mysql error %d:%s' % (e.args[0], e.args[1]))


sql="update hash_info set hash_info.info='Captain's VgHD DVD 21 a0472 to a0501.iso' where hash_info.hash='5302c42cdf439cafa98f048e8367b3ff4829628e'".encode('utf-8')
print(sql)

#createDatabase()
insertInfo("4cde5b50a8930315b479931f6872a3db59575366")
selectAllTable("hash_info")
selectAllTable("peerIP")
