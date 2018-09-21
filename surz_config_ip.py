#/usr/bin/python
import os
os.system("mv /etc/sysconfig/network-scripts/ifcfg-ens33  /etc/sysconfig/network-scripts/ifcfg-ens33_back")  
os.system("touch /etc/sysconfig/network-scripts/ifcfg-ens33")
def shuchu():
	print("eg.\nIPADDR=172.16.145.72\nNETMASK=255.255.0.0\nGATEWAY=172.16.1.1\nDNS1=172.16.1.1\n")
	ip=raw_input("plese input ip:")
	netmask=raw_input("please input netmask:")
	gateway=raw_input("please input gateway:")
	dns=raw_input("please input dns:")
	f=open("/etc/sysconfig/network-scripts/ifcfg-ens33","wb")
	f.write("DEVICE=ens33\nONBOOT=yes\nBOOTPROTO=none\nIPADDR=%s"%ip)	
	f.write("\nNETMASK=%s"%netmask)	
	f.write("\nGATEWAY=%s"%gateway)	
	f.write("\nDNS1=%s\n"%dns)	
	f.close()

def restart():
	os.system("service network restart")
	
def read():
	m=open('/etc/sysconfig/network-scripts/ifcfg-ens33')
	while True:
        	line=m.readline()
        	if len(line) == 0:
                	break
        	print line,
	m.close()

	

shuchu()
restart()
read()
