#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb

# 打开数据库连接
db = MySQLdb.connect("localhost", "root", "whx19911105", "ipatron")

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# 使用execute方法执行SQL语句
cursor.execute("SELECT length(ckey) keylen, count(*)FROM ipatron.bibli group by length(ckey)")

# 使用 fetchall() 方法获取所有数据
data = cursor.fetchall()
for row in data:
    print "length:", row[0], "count", row[1]

# 关闭数据库连接
db.close()
