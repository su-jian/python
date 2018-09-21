#!/usr/bin/python

#database:test
#table:student
#tab_column: id,name,address,sex
#create table student(id int,name varchar(10),address varchar(20),sex varchar(2));


#########
#connect
import MySQLdb
db=MySQLdb.connect(user='root',db='test')
#########

def menu():
        print '\t1.add student'
        print '\t2.del student'
        print '\t3.update student'
        print '\t4.query student'
        print '\t5.exit'
##########
def add():
        id=raw_input("please input your ID: ")
        name=raw_input("please input your name: ")
        addr=raw_input("please input your address: ")
        sex=raw_input("please input your sex:[W/M] ")
        cur=db.cursor()
        cur.execute('insert into student values (%s,%s,%s,%s)',(id,name,addr,sex))
        db.commit()
        print "inser successful !!!"
        r = cur.execute('select * from student')
        r=cur.fetchall()
	print
        for member3 in r:
                print member3
        cur.close()
##########
def dele():
        cur=db.cursor()
        r = cur.execute('select id,name from student')
        r=cur.fetchall()
        for member in r:
		print member
        del_id=raw_input("please input you want to delete id :")
        cur.execute('delete from student where id = %s',del_id)
        db.commit()
        cur.close()
        print "delete successful !!"
##########
def update():
        cur=db.cursor()
        r = cur.execute('select * from student')
        r=cur.fetchall()
	for member in r:
		print member
        up_id=raw_input("please input you want to update id :")
	up_num=raw_input("please input you modify object:[name/addr/sex]")
	if up_num=='name':
		new_name=raw_input("input new name: ")
		cur.execute('update student set name=\'%s\' where id=%s'%(new_name,up_id))
		print "success!!"
	elif up_num=='addr':
		new_addr=raw_input("input new addr: ")
		cur.execute('update student set address=\'%s\' where id=%s'%(new_addr,up_id))
		print "success!!"
	elif up_num=='sex':	
		new_sex=raw_input("input new sex:")	
		cur.execute('update student set sex=\'%s\' where id=%s'%(new_sex,up_id))
		print "success!!"
	else:
		print "please try again"
	db.commit()
	cur.close()
#########
def querry():
        cur=db.cursor()
        r = cur.execute('select * from student')
        r=cur.fetchall()
        for member in r:
		print member
	cur.close()
########
def main():
	import os
	import sys
	os.system('clear')
	while True:
		menu()
		choose=raw_input("please input your choose: ")
		if choose=='1':
			add()
		elif choose=='2':
			dele()
		elif choose=='3':
			update()
		elif choose=='4':
			querry()
		else:
			#break
			sys.exit()
		a=raw_input("press anykey to continue:")
		os.system('clear')
main()



