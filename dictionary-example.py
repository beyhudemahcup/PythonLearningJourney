student_details = {'firstStudent': 1, 'secondStudent': 2,
                   'thirdStudent': {
                       'age': 18,
                       'email': 'example@gmail.com',
                       'phoneNumber': '123324123'
                   }}

print(student_details)
print(student_details['firstStudent'])  # gives 1
print(student_details['thirdStudent'])
print(student_details['thirdStudent']['age'])
