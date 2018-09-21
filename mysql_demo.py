#!/usr/bin/python

import MySQLdb
db=MySQLdb.connect(host='localhost',user='jiafu',passwd='jiafu',db='jiafu')
cur=db.cursor()
cur.execute('insert into student (name,age,address,sex) values (\'liudehua\',50,\'jinan changqing\',\'F\')')
#r = cur.execute('delete from people where age=20')
db.commit()
r = cur.execute('select * from student')
r= cur.fetchall()
print(r)
cur.close()
db.close()
#往数据库里增加数据
#通过一个交互的界面往数据库里增加、删除、修改、查询数据
#显示出来的时候，尽可能是一行一行显示







