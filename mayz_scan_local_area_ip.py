import os
import  threading
numlock =threading.RLock()
prlock=threading.RLock()
zxs=0                      
class pings(threading.Thread):
  def __init__(self,num,interval):
    threading.Thread.__init__(self)
    self.nums=num
    self.inter=interval
    self.thread_stop=False
    self.ns=0
  def run(self):
    global zxs
    start=self.nums
    while start<255:
      ret=os.system('ping -c 1 -W 1 172.16.145.%d >/dev/null' % start)
      if not ret:
        prlock.acquire()
        print 'ping 172.16.145.%d ok' % start
        prlock.release()
        self.ns +=1
      start+=self.inter
    numlock.acquire()
    zxs+=self.ns
    numlock.release()
 
def pingt():
  s=255
  r=s-1
  threads=[]
  for i in range(1,s):
    t=pings(i,r)
    threads.append(t)
  for i in threads:
    i.start()
  for i in threads:
    i.join()
  global zxs
  print zxs,'ge ip'   
if __name__=='__main__':
  pingt()
