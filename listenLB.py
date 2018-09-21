#!/usr/bin/python

#version : 2.0
#author : mengqingxiang
import os,time,commands
#class simple_listen(pycurl.Crul):
class simple_listen:
	url=''
	port=''
	serveralived=''
	cpuLoad=''
	memLoad=''
	netLoad=''
	ioLoad=''
	logLevel=0
	def __init__(self,url,port):
		self.url=url
		self.port=port


	def get_serveralived(self):
		try:
			if os.system('nc -z %s %s &>/dev/null'%(self.url,self.port)):
				print 'server is false'
				return 1
			else:
				print 'server is ok'
				return 0
		except:
			print '\033[1mget_serveralived mistake\033[0m\nCant\'t get server state\nmaybe you OS not support or nc is not install ( or unknownError please call WebMaster ) '
			return 10



	def get_cpuLoad(self):
		try:
			load=commands.getoutput("ssh root@%s cat /proc/loadavg |awk '{print $1,$2,$3}' "%self.url).split()
			if float(load[0])>5 and float(load[1])>5 and float(load[2])>5:
				print 'cpuload is super full ',load
				return 2
			elif float(load[0])>5 or float(load[1])>5 or float(load[2])>5:
				print 'cpuload is general full ',load
				return 1
			else :
				print 'cpuload is relaxed ',load
				return 0
		except:
			print '\033[1mget_cpuLoad mistake\033[0m\n1,maybe not use ssh\'s secret key authentication\n2,maybe network not clear\n3,unknownError'
			return 10



	def get_memLoad(self):
		try:
			load=commands.getoutput("ssh root@%s cat /proc/meminfo |head -n 2|awk '{print $2}'"%self.url).split()
			if int(load[1])*100/int(load[0])>60:
				print 'memload is relaxed ',int(load[1])*100/int(load[0]),'% free'
				return 0
			elif int(load[1])*100/int(load[0])>20:
				print 'memload is general full ',int(load[1])*100/int(load[0]),'% free'
				return 1
			else :
				print 'memload is too full ',int(load[1])*100/int(load[0]),'% free'
				return 2
		except:
			print '\033[1mget_memLoad mistake\033[0m\n1,maybe not use ssh\'s secret key authentication\n2,maybe network not clear\n3,unknownError'
			return 10



class high_listen(simple_listen):
	logLevel=1
	def __init__(self,url,port):
		simple_listen.__init__(self,url,port)
	def get_webLoad(self):
		try:
			load=commands.getoutput("ping -i0.1 -c5 -W2 %s|awk '/avg/{print $4}'"%self.url).split('/')
			if float(load[1])>3 or float(load[2])>12:
				print 'webstate is too bad avg_respond time is %.2f max_respond time is %.2f'%(float(load[1]),float(load[2]))
				return 2
			elif  2>=float(load[1])>=1 or 10>=float(load[2])>=2:
				print 'webstate is bad avg_respond time is %.2f max_respond time is %.2f'%(float(load[1]),float(load[2]))
				return 1
			else:
				print 'webstate is relaxed avg_respond time is %.2f max_respond time is %.2f'%(float(load[1]),float(load[2]))
				return 0
		except:
			print '\033[1mget_webLoad mistake\033[0m\nmaybe network not clear or unknownError'
			return 10



	def get_ioLoad(self):
		try:
			judge_value=[]
			version=commands.getoutput("ssh root@%s cat /etc/redhat-release|egrep -o --color '\\b([0-9]\\.[0-9]+)\\b'"%self.url)
			if 5<=float(version)<7:
				load=commands.getoutput("ssh root@%s iostat -x 1 1|egrep -A5 -i 'Device' |tail -n +2|awk '$1 ~/[a-Z]$/{print $10,$12}'"%self.url).split()
				for i in range(0,len(load),2):
					if float(load[i])>15 or float(load[i+1])>80:
						print 'you %dth disk ioLoad is too full ,await is %s util is %.2f'%(i//2+1,load[i],float(load[i+1])),'%'
						judge_value.append(2)
					elif 5<=float(load[i])<=15 or 20<=float(load[i+1])<=80:
						print 'you %dth disk ioLoad is general full ,await is %s util is %.2f'%(i//2+1,load[i],float(load[i+1])),'%'
						judge_value.append(1)
					else:
						print 'you %dth disk ioLoad is relaxed ,await is %s util is %.2f'%(i//2+1,load[i],float(load[i+1])),'%'
						judge_value.append(0)
			else:
				print '\033[1mnow get_ioLoad method just support redhat\'s or CentOS\'s what varsion is 5 and 6 . 7 series is Developing\033[0m'
				judge_value.append(10)
			return judge_value
		except:
			print '\033[1mget_ioLoad mistake\033[0m\n1,maybe not use ssh\'s secret key authentication\n2,maybe network not clear\n3,maybe iostat not install\n4,screen size not suitable\n5,unknownError'
			return judge_value.append(10)



def set_log(level,info,ab):
	try:
		if int(level)==1:
			file=open('/var/log/ListenLB','a+')
		        file.write('%s \'s %s serverstate is %s,cpuload is %s,memLoad is %s,webLoad is %s,ioLoad is %s at time is %s\n'%(info[0],info[1],ab.get_serveralived(),ab.get_cpuLoad(),ab.get_memLoad(),ab.get_webLoad(),ab.get_ioLoad(),time.strftime('%Y-%m-%d %X %A',time.localtime(time.time()))))
        		file.close()
		else:
			file=open('/var/log/ListenLB','a+')
                        file.write('%s \'s %s serverstate is %s,cpuload is %s,memLoad is %s, at time is %s\n'%(info[0],info[1],ab.get_serveralived(),ab.get_cpuLoad(),ab.get_memLoad(),time.strftime('%Y-%m-%d %X %A',time.localtime(time.time()))))
                        file.close()
	except:
		print 'write false'



def input_info():
	a=raw_input('please input listen url : ')
	b=raw_input('please input listen port : ')
	c=[a,b]
	return c
#info=input_info()
#alived=get_serveralived(info[0],info[1])
#abc=simple_listen(info[0],info[1])
#print abc.get_serveralived()
#print abc.get_cpuLoad()
#print abc.get_memLoad()
#ab=high_listen(info[0],info[1])
#print ab.get_cpuLoad()
#print ab.get_webLoad()
#print ab.get_ioLoad()
#print get_cpuLoad(info[0])
#print get_memLoad(info[0])
#print get_ioLoad(info[0])

