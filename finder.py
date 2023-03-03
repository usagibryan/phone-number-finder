import re

print('Enter a message to scan for phone numbers: ')
message = input()

# phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}') # shortened wtih braces
# phoneNumRegex = re.compile(r'(\d{3})-(\d{3}-\d{4})') # grouping with parentheses

# phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)') # area code in () and grouped
phoneNumRegex = re.compile(r'(\(\d{3}\)) (\d{3}-\d{4})') # shortened with braces

mo = phoneNumRegex.search(message)
print('Phone number found: ' + mo.group()) # mo.group(0) will also return the entire matched text
print('The area code is: ' + mo.group(1))
print('The local exchange or subscriber number is: ' + mo.group(2))

# print(mo.groups())
# areaCode, mainNumber = mo.groups()
# print(areaCode)
# print(mainNumber)