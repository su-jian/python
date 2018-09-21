#!/usr/bin/python

#yum install psutil* -y 

def mem():
	import psutil
	aa=psutil.phymem_usage()
	total=aa[0]/1024/1024
	free=aa[4]/1024/1024
	used=aa[3]/1024/1024
	print "System memory \033[34mTotal\033[0m have %d M"%total
	print "System memory \033[34mUsed\033[0m have %d M"%used
	print "System memory \033[34mFree\033[0m have %d M"%free

def use():
	import os
	user=os.getlogin()
	uid=os.getuid()
	pid=os.getpid()
	ppid=os.getppid()
	print "System \033[34mUser\033[0m is %s"%user
	print "System \033[34mUID\033[0m is %s"%uid

def time():
	import time
	ti=time.strftime('%Y-%m-%d %H:%M:%S')
#	f=time.ctime()
#	t=f.split()
#	print "System \033[34mTime\033[0m is:",t[4],t[1],t[2],t[3]
	print "System \033[34mTime\033[0m is:",ti

time()
use()
mem()
	
	

