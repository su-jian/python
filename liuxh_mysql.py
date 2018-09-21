#!/usr/bin/python
#
import MySQLdb as m
db=m.connect('172.16.145.43','python','python','python')
def menu():
	print '\t\t1\t\t\tinsert'
	print '\t\t2\t\t\tdelete'
	print '\t\t3\t\t\tupdate'
	print '\t\t4\t\t\tquery'
	print '\t\t5\t\t\texit'
def add():
	id=raw_input('ID:')
	name=raw_input('NAME:')
	cur=db.cursor()
	cur.execute('insert into a values(\'%s\',\'%s\')'%(id,name))
	db.commit()
	print 'insert OK'
	r=cur.execute('select * from a')
	r=cur.fetchall()
	print
	for i in r:
		print i
	cur.close()
def delete():
	cur=db.cursor()
	r=cur.execute('select * from a')
	r=cur.fetchall()
	print
	for i in r:
		print i
	del_condition=raw_input("Please input the condition of deletion:(row='content')")
	cur.execute('delete from a where %s'%(del_condition))
	db.commit()
	r=cur.execute('select * from a')
	r=cur.fetchall()
	print
	for i in r:
		print i
	cur.close()
	print 'delete OK'
def update():
	cur=db.cursor()
	r=cur.execute('select * from a')
	r=cur.fetchall()
	for i in r:
		print i
	up_condition=raw_input("Please input the condition of update:(row='content')")
	up_to=raw_input("Please input the content of update:(row='content')")
	cur.execute('update a set %s where %s'%(up_to,up_condition))
	db.commit()
	r=cur.execute('select * from a')
	r=cur.fetchall()
	print
	for i in r:
		print i
	cur.close()
	print 'update OK'
def query():
	cur=db.cursor()
	r=cur.execute('select * from a')
	r=cur.fetchall()
	for i in r:
		print i
	cur.close()
def main():
	import sys
	import os
	os.system('clear')
	while True:
		menu()
		i=raw_input('Please input your choice:')
		if i=='1':
			add()
		elif i=='2':
			delete()
		elif i=='3':
			update()
		elif i=='4':
			query()
		else:
			sys.exit()
		key=raw_input('press any key to continue:')
		os.system('clear')
main()
