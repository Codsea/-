#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/31 16:41
# @Author  : Jiange
# @File    : DOmysql.py
# @简介     : 连接MySQL数据库
import pymysql

class domysql:
    def __init__(self,host,user,pwd,db,port=3306,charset='utf8'):
        '''
        连接MySQL数据库，需提供IP地址，账号，密码，数据库名称，端口号，字符集
        :param host: IP地址
        :param user: 账号
        :param pwd: 密码
        :param db: 数据库名称
        :param port: 端口号
        :param charset: 字符集
        '''
        self.host = host
        self.user = user
        self.pwd = pwd
        self.db = db
        self.port = port
        self.charset = charset
        self.cur = None
        self.con =  None
        self.connect_db()
    def connect_db(self):
        #连接数据库
        try:
            self.con = pymysql.connect(host=self.host,user=self.user,passwd=self.pwd,
                                     db=self.db,port=self.port,charset=self.charset)
        except Exception as a:
            a = print('数据库连接失败，请检查参数')
        else:
            print('*'*40+'登录数据库成功！可以进行下一步操作'+'*'*40)
            print('>  '*50)
            self.cur = self.con.cursor()    #创建游标
    def get_one(self,sql):
        #获取一行
        self.cur.execute(sql)
        return self.cur.fetchone()
    def get_all(self,sql):
        #获取所有
        self.cur.execute(sql)
        return self.cur.fetchall()
    def dml(self,sql):
        #执行dml操作
        self.cur.execute(sql)
    def commit(self):
        #提交事务
        self.con.commit()
    def close(self):
        self.cur.close()    #关闭游标
        self.con.close()    #关闭数据库连接

if __name__ == '__main__':
    con = domysql('localhost','root','123456','mysql')
    sql = 'select * from user'
    getsql = con.get_one(sql)
    print(getsql)