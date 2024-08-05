def square(num): return num ** 2


def even_checker(num): return num % 2 == 0


numbers = [1, 2, 3, 4, 5, 6, 7]
square_result = list(map(square, numbers))

# lambda version of result
square_resultLambda = list(map(lambda num: num ** 2, numbers))

print(square_result)
print(square_resultLambda)

even_result = list(filter(even_checker, numbers))

# lambda version of even result
even_resultLambda = list(filter(lambda num: num % 2 == 0, numbers))

print(even_result)
print(even_resultLambda)

