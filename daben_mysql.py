#!/usr/bin/python

import MySQLdb
db=MySQLdb.connect(host='localhost',user='jiafu',passwd='jiafu',db='mysql')
cur=db.cursor()
#cur.execute('insert into student (name,age,address,sex) values (\'lee\',21,\'jinan\',\'F\')')
#r=cur.execute('delete from people where age=20')
#db.commit()


name=raw_input("please input the name you want to insert:")
age=raw_input("please input the age you want to insert:")
address=raw_input("please input the address you want to insert:")
sex=raw_input("please input the sex you want to insert:")

T=(name,age,address,sex)

cur.execute("insert into student values(%s,%s,%s,%s)",T)


r=cur.execute("select * from student")
r=cur.fetchall()

for i in r:
	print(i)

cur.close()
db.close()

