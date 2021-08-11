import pyperclip
import re
text = str(pyperclip.paste())

phone_regex = re.compile(r'''(
	(\d{3}|\(\d{3}\))?    
	(\s|-|\.)?             
	(\d{3})               
	(\s|-|\.)?            
	(\d{4})               
	)''', re.VERBOSE)

email_regex = re.compile(r'''(
	[a-zA-Z0-9._%+-]+      
	@                      
	[a-zA-Z0-9.-]+         
	(\.[a-z{2,4}])         
	)''', re.VERBOSE)

match =[]

for groups in phone_regex.findall(text):
	phone_number = '-'.join([groups[1],groups[3],groups[5]])
	match.append(phone_number)

for groups in email_regex.findall(text):
	match.append(groups[0])

if len(match)>0:
	pyperclip.copy('\n'.join(match))
	print ('Copied to clipboard')
	print ('\n'.join(match))
else:
	print ('Nothing found')