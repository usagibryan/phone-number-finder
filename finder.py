import re

def phone_number_finder(text):
    pattern = re.compile(r'(\(?\d{3}\)?)[- ]?(\d{3})[- ]?(\d{4})')
    matches = re.findall(pattern, text)

    phone_number_count = 0

    for match in matches:
        phone_number_count += 1
        area_code = match[0].replace('(', '').replace(')', '')
        phone_number = f'({area_code}) {match[1]}-{match[2]}'
        print()
        print(f'Phone number found: {phone_number}')
        print(f'Area code: {area_code}')
        print(f'Local exchange or number: {match[1]}-{match[2]}')

    print()
    print(f'Total phone numbers found: {phone_number_count}')

print('Enter a message to scan for phone numbers: ')
message = input()
phone_number_finder(message)