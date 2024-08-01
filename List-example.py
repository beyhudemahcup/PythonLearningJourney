my_list = [1, 'numbers', False]
print(my_list)

number1_list = ['one', 'two']
number2_list = ['three', 'four']
numbers_string_list = number1_list + number2_list

print(numbers_string_list)

numbers_list = [29, 25, 11, 44, 35, 16]
print(numbers_list)

numbers_list.append(0)  # adds this element end of the list
numbers_list.insert(3, 52)
numbers_list.pop()  # deletes the last element

numbers_list.sort()  # orders the list
print(numbers_list)

numbers_list.reverse()
print(numbers_list)

numbers_list.clear()  # deletes every element inside the list
print(numbers_list)


