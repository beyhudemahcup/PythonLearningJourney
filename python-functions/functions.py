def sayHello(name=""):
    print("Hello " + name)


def sumTwoNumbers(number1, number2):
    print(number1 + number2)


def sumNumbers(*params):
    print(sum(params))
    '''
    sum = 0

    for i in params:
        sum = sum + i
    print(sum)
    # '''


# ** indicates that we send a dictionary to the function
def displayUser(**args):
    for key, value in args.items():
        print(f"{key} is {value}")


def ageCalculator(born_year):
    print(f"Your age is {2024 - born_year}")


def myfunc(a, b, *args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)


sayHello()
sayHello("World!")
sayHello("Ismet Ozel")
sumTwoNumbers(43, 54)
ageCalculator(1978)
ageCalculator(2050)  # if user came from the future
sumNumbers(32, 54, 65, 12)
displayUser(Name='Ismet', Age=76, City='Istanbul')
# this is not  best practise obviously
displayUser(FavouriteBook='Killing the mockingbird', Writtenyear=1976)
myfunc(10, 20, 30, 40, 50, key1="value 1", key2="value 2")
