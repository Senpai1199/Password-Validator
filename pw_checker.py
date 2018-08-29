import re
password = input('Enter password: ')

if(len(password) > 5):
	m1 = re.search(r'[a-z]+',password)
	if(m1 == None):
		print('Invalid password')
		sys.exit()

	else:			
		m2 = re.search(r'[A-Z]+',password)
		if(m2 == None):
			print('Invalid password')
			sys.exit()              
			
		else:
			m3 = re.search(r'\d+', password)
			if(m3 == None):
				print('Invalid password')
				sys.exit()
				
			else:
				m4 = re.search(r'[!@#$%^-_.&*]+',password)                      
				if(m4 == None):
					print('Invalid password')
					sys.exit()
					
				else:
					print('Valid password')
				
else:
	print('Invalid password')

	
	
