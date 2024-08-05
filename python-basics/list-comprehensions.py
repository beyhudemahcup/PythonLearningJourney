for x in range(11):
    print(x)

# it creates a list starts from 0 and ends at 10
numbers = [x for x in range(11)]
print(numbers)

numberssquared = [x**2 for x in range(11)]
print(numberssquared)

listexample1 = [x**2 for x in range(11) if x % 3 == 0]
print(listexample1)

years = [1999, 1976, 2003, 1965, 1988]
ages = [2024 - year for year in years]
print(ages)

# nested for loop with comprehesions

matrix = [(x, y) for x in range(3) for y in range(3)]
print(matrix)
