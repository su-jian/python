#1/usr/bin/python
from listenLB import *
import threading
info=input_info()
def call(info):
#	print '\033[1m-----------------------------------------call father class print\033[0m'
	abc=simple_listen(info[0],info[1])
#	abc.get_serveralived()
#	abc.get_cpuLoad()
#	abc.get_memLoad()
	ab=high_listen(info[0],info[1])
#	print '\033[1m-----------------------------------------call son class print\033[0m'
#	ab.get_serveralived()
#	ab.get_cpuLoad()
#	ab.get_memLoad()
#	ab.get_webLoad()
#	ab.get_ioLoad()
	print '\033[1m-----------------------------------------call setlog\033[0m'
	set_log(abc.logLevel,info,abc)
	print '\033[1m-----------------------------------------end\033[0m'
while True:
	call(info)
	time.sleep(5)
