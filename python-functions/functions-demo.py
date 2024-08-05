def printScreen(word, number):
    for i in range(0, number):
        print(word)


def listConverter(*args):
    mylist = []
    for i in range(len(args)):
        mylist.append(args[i])
    return mylist


def primeNumberFinder(num1, num2):
    biggerNumber = num1
    shortNumber = num2
    temp = 0
    myPrimeNumbersList = []

    if biggerNumber < shortNumber:
        temp = biggerNumber
        biggerNumber = shortNumber
        shortNumber = temp

    for i in range(shortNumber, biggerNumber):
        isPrime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                isPrime = False
                break
        if isPrime:
            myPrimeNumbersList.append(i)

    return myPrimeNumbersList


def divideDedector(num1):
    myDivideNumbersList = []
    for i in range(1, num1):
        if num1 % i == 0:
            myDivideNumbersList.append(i)
    return myDivideNumbersList


printScreen("hello", 10)
print(listConverter(10, 20, 40, 50, 60))
print(listConverter('a', 'b', 'c', 'd'))
print(primeNumberFinder(17, 120))
print(divideDedector(50))