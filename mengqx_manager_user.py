#!/usr/bin/python
import os 
def add_user():
	add_name=raw_input('please input add user name : ')
	os.system("useradd %s "  % (add_name) )
	os.system('id %s ' % (add_name))
def del_user(name):
	os.system("userdel -r %s" % (name))
	os.system("id  %s" % (name))
def user_count():
	readfile=open('/etc/passwd','r')
	for (num,value) in enumerate(readfile):
        	name=value.split(':')
	        print "{x} \033[1m {a} \033[0m uid is \033[1m {b} \033[0m home is \033[1m {c} \033[0m".format(x=num+1,a=name[0],b=name[2],c=name[5])
	readfile.close()
add_user()
del_name=raw_input('please input del user name : ')
del_user(del_name)
user_count()
