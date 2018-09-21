#1/usr/bin/bash
shoplist=[]
shoplist2=[]
while True:
	shop=raw_input('please input fruit name :\033[1m')
	if shop == 'ok':
		print "\033[0myou have ",len(shoplist)," to shop ,there is ",shoplist
		break
	elif shop in shoplist:
		print "this fruit is exists\033[0m"
	else:
		print "add fruit is ok\033[0m\ninput ok to stop"
		shoplist.append(shop)
while shoplist:
	print "\033[0mwhich do you want to buy \033[1m",shoplist,"\033[0m"
	nextshop=raw_input('please input fruit name :\033[1m')
	shoplist.remove(nextshop)
	shoplist2.append(nextshop)
else:
	print '\033[0mshop is over , we have to go home!'
	print 'order is \033[1m',shoplist2,'\033[0m'
