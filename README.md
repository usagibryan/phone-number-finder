# Phone Number Finder

[Run on Replit](https://replit.com/@usagibryan/phone-number-finder#main.py)

This code defines a function `phone_number_finder` that takes a string `text` as input and searches for phone numbers within it using regular expressions. The regular expression used is `r'(\(?\d{3}\)?)[- ]?(\d{3})[- ]?(\d{4})'`, which matches phone numbers with or without parentheses around the area code and with or without spaces or hyphens between the digits.

The function first compiles the regular expression pattern using the `re.compile` function, and then finds all matches in the input text using the `re.findall` function.

The function then iterates over the matches and prints information about each phone number found, including the full formatted phone number, the area code, and the local exchange or number. Finally, it prints the total number of phone numbers found.

To use this code, simply call the `phone_number_finder` function with a string as an argument that you want to search for phone numbers. The function will print out the information for each phone number it finds.

For example, you could run this code by entering the following command:

```Python
phone_number_finder('My phone number is (123) 456-7890 and my office number is 555-1234.')
```

This would output:

```Python
Phone number found: (123) 456-7890
Area code: 123
Local exchange or number: 456-7890

Phone number found: 555-1234
Area code: 555
Local exchange or number: 1234

Total phone numbers found: 2
```

The purpose of this project is to practice the use of regular expressions. See Chapter 7: [Pattern Matching With Regular Expressions](https://automatetheboringstuff.com/2e/chapter7/) from Automate the Boring Stuff with Python by Al Sweigart.