message = 'Hello, Is there anybody in there?'

print(message.upper())
print(message.lower())
print(message.title())   # every first letter will be uppercase
print(message.capitalize())   # only first letter will be uppercase
print(message.strip())
print(message.split(','))
print('*'.join(message))
print(message.find('anybody'))
print(message.lstrip('Hello,'))
print(message.rstrip('re?'))
print(message.count('e'))  # sentence has 5 'e'
print(message.isalpha())  # checks if is alphabetic or not

# message = '123'
print(message.isdigit())  # checks if it contains only digits or not
print(message.center(50, '*'))  # it centered our message and complete it 50 characters with *
print(message.ljust(50, '*'))
print(message.rjust(50, '*'))
print(message.replace(' ', '?'))

resultArr = message.split(' ')
print(resultArr[1])

