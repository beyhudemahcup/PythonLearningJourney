# *********** nested func ************

#  encapsulation
def outer(num1):
    print("outer func is executed!")

    def inner_increment(num1):
        print("inner func is executed!")
        return num1 + 1

    num2 = inner_increment(num1)
    print(num1, num2)


outer(10)  # called nested function


# we cant call inner_increment(num1) because its nested func

def factorial(number):
    if not isinstance(number, int):
        raise TypeError("number must be an integer")
    if not number >= 0:
        raise ValueError("number must be equal or bigger than 0")

    def inner_factoriel(number):
        if number <= 1:
            return 1
        return number * inner_factoriel(number - 1)

    return inner_factoriel(number)


# ****** closure example *********
# returns inner function, we can call a function, use as a variable

def power_number_of(number):
    def inner(power):
        return number ** power

    return inner


def authorization_check(page):
    def inner(role):
        if role == "Admin":
            return f"{role} can reach {page}"
        else:
            return f"{role} can not reach {page}"

    return inner


def math_calculation(calculation_name):
    def sum_func(*args):
        sum = 0
        for i in args:
            sum += i
        return sum

    def multiplication_func(*args):
        multiplication = 1
        for i in args:
            multiplication *= i
        return multiplication

    if calculation_name == 'sum':
        return sum_func
    elif calculation_name == 'multiplication':
        return multiplication_func
    else:
        raise TypeError("Entered value is not valid!")


# sending funcs as a parameter
def sum_func(a, b):
    return a + b


def subtraction_func(a, b):
    return a - b


def multiplication_func(a, b):
    return a * b


def division_func(a, b):
    return a / b


def calculation(f1, f2, f3, f4, name_of_calculation):
    if name_of_calculation == "addition":
        print(f1(int(input("Enter first number: ")), int(input("Enter second number: "))))
    elif name_of_calculation == "subtraction":
        print(f2(int(input("Enter first number: ")), int(input("Enter second number: "))))
    elif name_of_calculation == "multiplication":
        print(f3(int(input("Enter first number: ")), int(input("Enter second number: "))))
    elif name_of_calculation == "division":
        print(f4(int(input("Enter first number: ")), int(input("Enter second number: "))))
    else:
        print("unknown calculation!")


# decorative functions (decorator)
# example 1
def my_decorator(func):
    def wrapper(name):
        print("preprocess from func")
        func(name)
        print("postprocess from func")

    return wrapper


@my_decorator
def sayHello(name):
    print("hello", name)


# example 2
import math
import time


def calculate_execution_time(func):
    def inner(*args, **kwargs):
        start_time = time.time()
        time.sleep(1)
        func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} function execution time is {end_time - start_time:.4f}")
    return inner


@calculate_execution_time
def get_power(a, b):
    print(math.pow(a, b))


@calculate_execution_time
def get_factorial(num):
    print(math.factorial(num))


get_power(4, 4)
get_factorial(4)

sayHello("Nick")

# execution part
'''
try:
    print(factorial(5))
    print(factorial(-3))
except Exception as e:
    print(e)

three = power_number_of(3)
print(three(3))  # gets 3 powered by 3
two = power_number_of(2)
print(two(8))  # gets 2 powered by 8

user = authorization_check("Product update")
print(user("Admin"))
print(user("Observer"))

sum_numbers = math_calculation("sum")
print(sum_numbers(1, 34, 6, 32, 75, 12))

multiplication_numbers = math_calculation("multiplication")
print(multiplication_numbers(3, 4, 5, 6))

#  calling func that accepts funcs as a parameter
summary_numbers = calculation(sum_func, subtraction_func, multiplication_func, division_func, "addition")
subtraction_numbers = calculation(sum_func, subtraction_func, multiplication_func, division_func, "subtraction")
multiplication_numbers = calculation(sum_func, subtraction_func, multiplication_func, division_func, "multiplication")
division_numbers = calculation(sum_func, subtraction_func, multiplication_func, division_func, "division")

'''
