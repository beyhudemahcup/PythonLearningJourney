import re


def check_password(password):
    if len(password) <= 8:
        raise Exception("Password should be longer than 8 characters")
    elif not re.search("[a-z]", password):
        raise Exception("Password should contain lowercase letters")
    elif not re.search("[A-Z]", password):
        raise Exception("Password should contain uppercase letters")
    elif not re.search("[0-9]", password):
        raise Exception("Password should contain a digit")
    elif not re.search("[_@,.]", password):
        raise Exception("Password should contain special characters")
    elif not re.search("\s", password):
        raise Exception("Password should not contain space character")


listExample = ["12", "22", "6t", "63c", "abc", "30", "40"]

# 1-) find list elements that only have digits in them
for i in listExample:
    try:
        result = int(i)
        print(result)
    except ValueError:
        continue  # it keeps working without getting an error

# 2-) checks every input if it's a digit or not until user press 'q' letter
while True:
    try:
        inputFromUser = input("enter a value('q' for exit):").lower()
        if inputFromUser == 'q':
            break
        result = int(inputFromUser)
        print(result)
    except ValueError as e:
        print(e)

# 3-) throw a turkish character error according to the password

turkish_chars = 'şçİüğöı'

password = input("please enter a password: ")

for i in password:
    if i in turkish_chars:
        raise TypeError("Password should not contain turkish characters")
    else:
        pass

print("Password is valid")



























