import re

print('Enter a message to scan for phone numbers: ')
message = input()

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search(message)
print('Phone number found: ' + mo.group())