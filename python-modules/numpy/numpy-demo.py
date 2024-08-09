import numpy as np

# 1- Create a numpy array with values (10, 15, 30, 45, 60).
# result = np.array([10, 15, 30, 45, 60])
# 2- Create a numpy array with numbers between (5-15).
# result = np.arange(5, 16)

# 3- Create a numpy array with numbers between (50-100) incremented by 5.
# result = np.arange(50,101,5)

# 4- Create an array of 10 zeros.
# result = np.zeros(10)

# 5- Create an array of 10 ones.
# result = np.ones(10)

# 6- Generate 5 evenly spaced numbers between (0-100).
# result = np.linspace(0,100,5)

# 7- Generate 5 random integers between (10-30).
# result = np.random.randint(10, 30, 5)

# 8- Generate 10 numbers between [-1 and 1].
# result = np.random.randn(10)

# 9- Create a random matrix of size (3x5) with values between (10-50).
random_matrix = np.random.randint(10, 50, 15)
# matrix_reshaped = random_matrix.reshape(3, 5)

# 10- Calculate the sum of the rows and columns of the generated matrix.
# rowTotal = matrix_reshaped.sum(axis = 1)
# columnTotal = matrix_reshaped.sum(axis = 0)
# print(rowTotal)
# print(columnTotal)

# 11- What are the maximum, minimum, and average of the generated matrix?
# result = np.min(random_matrix)
# result = np.max(random_matrix)
# result = np.mean(random_matrix)

# 12- What is the index of the largest value in the generated matrix?
# result = np.argmax(random_matrix)


# 13- Select the first 3 elements of the array containing numbers between (10-20).
# result = np.random.randint(10,20,5)
# result = result[:3]

# 14- Print the elements of the generated array in reverse order.
# result = np.random.randint(10,20,5)
# result = result[::-1]

# 15- Select the first row of the generated matrix.
# result = random_matrix.reshape(3, 5)
# print(result[0])

# 16- What is the element in the 2nd row and 3rd column of the generated matrix?
# result = random_matrix.reshape(3, 5)
# print(result[1,2])

# 17- Select the first element of each row in the generated matrix.
# result = random_matrix.reshape(3, 5)
# print(result)
# print(result[:,0])

# 18- Square every element in the generated matrix.
# result = random_matrix.reshape(3, 5)
# result = result * result

# 19- Which elements of the generated matrix are positive even numbers?

# matrix_negative_positive = np.random.randint(-50, 50, 15)
# result = matrix_negative_positive.reshape(3, 5)
# even_numbers_matrix = result[result % 2 == 0]
# result = even_numbers_matrix[even_numbers_matrix > 0]
# print(result)
