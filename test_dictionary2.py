#a database used get()

#insert the database code by'test_dictionary1.py'
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


labels = {
	'phone': 'phone number',
	'addr': 'address'
}

name = raw_input('Name: ')

#search the phone number or address?
request = raw_input('Phone number(p) or address(a)? ')

#use the ture Key
Key = request #if the request is none of 'p' and 'a'
if request ==  'p': Key = 'phone'
if request ==  'a': Key = 'addr'

#use the get() to append the value
person = people.get(name,  {})
label = labels.get(Key,Key)
result = person.get(Key, 'not available')

print "%s's %s is %s." %(name, label, result)