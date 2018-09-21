#!/usr/bin/python
#Filename:shop.py
shoplist=['apple','pear','orange','banana','peach']
shop_purchase=[]
def prepare():
	value=True
	while value:
		fruit=raw_input('Please input your favourite fruit:')
		if fruit not in shoplist:
			shoplist.append(fruit)
		else:
			print '%s already exists'%(fruit)
		yn=raw_input('Would you like to continue?y/n')
		if yn!='y':
			value=False
	print 'amount:%d'%(len(shoplist))
def purchase():
	value=True
	while value:
		fruit=raw_input('please input fruit you purchased:')
		if fruit in shoplist:
		  	shop_purchase.append(fruit)
			shoplist.remove(fruit)
		else:
			print '%s does not exists'%(fruit)
		print shoplist
		if len(shoplist)==0:
			value=False
			print 'You have purchases all fruit.'
			print 'The order you purchase is',shop_purchase
			print 'Go home now!'
prepare()
purchase()
			



