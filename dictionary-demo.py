students = {}

print('please enter required info...')

number = input("student number: ")
name = input("student name: ")
surname = input("student surname: ")
phone = input("student phone: ")

# students[number] = {
#     'name': name,
#     'surname': surname,
#     'phone': phone
# }

students.update({
    number: {
        'name': name,
        'surname': surname,
        'phone': phone
    }
})

print(students)
studentNumberInput = input('Please enter a student number you want to check:')
print(students[studentNumberInput])
















