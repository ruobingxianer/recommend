#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb

# 打开数据库连接
db = MySQLdb.connect("localhost", "root", "whx19911105", "ipatron")

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# 使用execute方法执行SQL语句
cursor.execute(
    "SELECT item_id,l.ckey FROM ipatron.userlog l, ipatron.bibli b where l.ckey=b.ckey and b.title='' group by item_id,l.ckey")

# 使用 fetchall() 方法获取所有数据
data = cursor.fetchall()

for row in data:
    print str(row[0])
# 关闭数据库连接
db.close()
