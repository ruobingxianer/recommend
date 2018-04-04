#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb
import time

# 打开数据库连接
db = MySQLdb.connect("localhost", "root", "whx19911105", "ipatron")

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# 使用execute方法执行SQL语句
print "in time begin",time.time()
cursor.execute(
    "SELECT item_id,ckey FROM ipatron.userlog where ckey in (select ckey from ipatron.bibli where author='') group by item_id,ckey")
# 使用 fetchall() 方法获取所有数据
data = cursor.fetchall()
print len(data)
print "in time end",time.time()

print "link time begin",time.time()
cursor.execute(
    "SELECT item_id,l.ckey FROM ipatron.userlog l, ipatron.bibli b where l.ckey=b.ckey and b.author='' group by item_id,l.ckey")
# 使用 fetchall() 方法获取所有数据
data = cursor.fetchall()
print len(data)
print "link time end",time.time()

# 关闭数据库连接
db.close()
