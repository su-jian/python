import thread,os
import time
ipused=[]
ipnoused=[]
def get_ip(num):
	if os.system('ping -i1 -c2 -W1 172.16.145.%s &>/dev/null'%num):
		ipnoused.append('172.16.145.%s'%num)
		f=open('not_used.txt','a+')
		f.write('172.16.145.%s\n'%num)
		f.close()
	else:
		ipused.append('172.16.145.%s'%num)
		f=open('used.txt','a+')
		f.write('172.16.145.%s\n'%num)
		f.close()
	
ip=0
while ip<254:
	ip+=1
	thread.start_new_thread( get_ip, ( '%s'%ip, ) )
raw_input('wait:')
for i in  ipnoused:
	print i
#os.system('cat used.txt |sort -n -t. -k4')
