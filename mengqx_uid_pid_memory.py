#!/usr/bin/python
import os,time,commands
def local_user_info():
        userinfo={}
        readline=open('/etc/passwd','r')
        for i in readline:
                j=i.split(':')
                userinfo[j[0]]=j[2]
        return userinfo

def cat_user_count(userinfo):
	user=os.popen('who').readlines()
	for (i,j) in enumerate(user):
		login_info=j.split()
		print "\033[1m %-5s \033[0m user is \033[1m %-5s \033[0m uid is \033[1m%-4s \033[0m terminal is \033[1m %-5s \033[0m start time is \033[1m %-7s %-5s \033[0m from \033[1m %-20s \033[0m"%(str(i+1)+'th',login_info[0],userinfo.get(login_info[0]),login_info[1],login_info[2],login_info[3],login_info[4])

def get_time():
	print time.strftime('%Y-%m(%B)-%d %X %w(%A) %Z',time.localtime(time.time()))

def get_pid():
	ppid=commands.getstatusoutput("ps -ef |awk -v pid=$$ '$2==pid{print $2,$3}'")[1].split()
	pid=os.popen('ps -ef|tail -n +2').readlines()
	for i,j in enumerate(pid):
		pid_count=j.split()
		print "\033[1m %-8s \033[0m pid is \033[1m %-7s \033[0m ppid is \033[1m %-7s \033[0m"%(pid_count[0],pid_count[1],pid_count[2])
	print "\nprocess total is \033[1m{s}\033[0m \n\n\n current process pid is \033[1m{d}\033[0m ppid is \033[1m{f}\033[0m".format(s=i+1,d=ppid[0],f=ppid[1])
	
def get_mem():
	meminfo=os.popen('free |tail -n +2').readlines()
	for o,i in enumerate(meminfo):
		j=i.split()
		if o==0:
			print "mem total is \033[1m%s\033[0m usedd is \033[1m%s\033[0m available(buff/cache+shared+free) is \033[1m%s\033[0m free is \033[1m%s\033[0m buff/cache is \033[1m%s\033[0m shared is \033[1m%s\033[0m"%(j[1],j[2],j[6],j[3],j[5],j[4])
		else :
			print "swap total is \033[1m%s\033[0m used is \033[1m%s\033[0m free is \033[1m%s\033[0m"%(j[1],j[2],j[3])
	

def view():
	while True:
		os.system('clear')
		choice=raw_input('%s\n\n\n\t\t\t\t\t\033[1mwelcome to mqx\'s Python Practice Court\n\n\t\t\t\t\t1,get login user info now\n\t\t\t\t\t2,get system time and current pid,ppid\n\t\t\t\t\t3,get memory info now\n\t\t\t\t\t0,is exit\033[0m\n\n\n%s\n\npleasy input you choice : '%('*'*120,'*'*120))
		if not choice.isdigit():
			print "\t\t\t\t\t\033[1minput false ! please try again\033[0m"
		elif int(choice)==1:
			user_info=local_user_info()
			cat_user_count(user_info)
		elif int(choice)==2:
			get_time()
			get_pid()
		elif int(choice)==3:
			get_mem()
		elif int(choice)==0:
			print "\t\t\t\t\t\033[1mthinks for you employ\033[0m"
			time.sleep(1)
			os.system('clear')
			return 0
		else:
			print "\t\t\t\t\t\033[1minput false ! please try again\033[0m"
		raw_input('\n\n\t\t\t\t\t\033[1mpress Enter to continue\033[0m')
view()
