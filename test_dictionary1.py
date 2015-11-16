#!/user/bin/python2
#database

#the database use the name as Key.every people use another dictionary,and the Key'phone' and 'addr' are their phonenumber and address.

people = {

	'Alice':{
		'phone': '2341',
		'addr': 'Foo drive 23'
	},

	'Beth':{
		'phone': '9102',
		'addr': 'Bar street 42'	
	},

	'Cecil':{
		'phone': '3158',
		'addr': 'Baz avenue 90'
	}
}

#the label for phonenumber and address,will be used when print
labels = {
	'phone': 'phone number',
	'addr': 'address'
}

name = raw_input('Name: ')

#search phone or address?
request = raw_input('phone number (p) or address (a)?')

#use the ture Key
if request == 'p': key = 'phone'
if request == 'a': key = 'addr'

#if the Key is effective,print the information
if name in people:print "%s's %s is %s." % \
	(name, labels[key], people[name][key])