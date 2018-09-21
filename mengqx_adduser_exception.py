#!/usr/bin/python
import os
def iunputname():
	name=raw_input('please input user name ')
	return name
def useradd(name):
	if os.system('id %s &>/dev/null'%name):
		return aaa
	else:
		print "user exsits"
try:
	name=iunputname()
	useradd(name)
except NameError:
	os.system('useradd %s &>/dev/null'%name)
finally:
	os.system("cat /etc/passwd|awk -F: '{print $1,$3,$4,$6,$7}'|egrep -C20000 --color ^%s"%name)
