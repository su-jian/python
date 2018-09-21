import os,commands


try:
	u_name=raw_input("please input your name:")
	if os.system("id %s &>/dev/null"%(u_name)) != 0:
		raise NameError
	os.system("useradd %s"%(u_name))
except NameError:
	print "%s is not exists"%(u_name)
finally:
	print os.system("cat /etc/passwd")
