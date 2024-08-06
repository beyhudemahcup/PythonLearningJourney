import numpy as np

# we can use dozens of different methods with numpy module

# python list
# py_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# np_arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

# print(type(py_list))
# print(type(np_arr))

# py_divided_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# np_divided_list = np_arr.reshape(3, 3)

# print(py_divided_list)
# print(np_divided_list)

# print(np_arr.ndim)  # 1
# print(np_divided_list.ndim)  # 2

# result = np.array([1,3,5,7,9])
# result = np.arange(1,10) #1 to 9
# result = np.arange(10,100,5)# 10 to 100 increase 5 by 5
# result = np.zeros(10) # 10 zeros
# result = np.ones(10) #10 ones
# result = np.linspace(2,102,5) #seperate numbers 5 equal part starts from 2 to ends 102
# result = np.linspace(1,10,2) #divide 2 equal part
# result = np.random.randint(0,10)# random number between 0 and 9
# result = np.random.rand(3) # 3 values between 0 and 1
# np_array = np.arange(50)
# np_multi = np_array.reshape(5,10)#creates matrix with 10 columns and 5 lines
# print(np_multi.sum(axis=1)) # sum of 5 lines
# print(np_multi.sum(axis=0))# sum of 10 columns

# random_numbers = np.random.randint(1,100,10)
# print(random_numbers)
# # result = random_numbers.max()
# # result = random_numbers.min()
# # result = random_numbers.mean() # average of numbers
# # result = random_numbers.argmax() # index of the biggest number in ndarray
# result = random_numbers.argmin() # index of the smallest number in ndarray
# print(result)

# numbers = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90])
# result = numbers[5]# 5. element
# result = numbers[-2] # 2. element counting from end of the list
# result = numbers[1:4] # numbers between 1. index and 4.index
# result = numbers[:]#whole list
# result = numbers[::]#whole list
# result = numbers[3:] #starts from 3. index and goes to the end
# result = numbers[::-1] #whole list starts from the end

# numbers2 = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])  # nested arr
# result = numbers2[0] #[10,20,30]
# result = numbers2[0,2] #30 (0. index, 2. element)

# result = numbers2[:,2] # selects 2. elements of every arr
# result = numbers2[:,0:2] # selects 0. and 1. elements of every arr
# result = numbers2[-1, :]  # every element of -1 index(last index) arr
# result = numbers2[:2,:2] #first 2 elements of first 2 index

# print(result)

# arr1 = np.arange(0, 10)
# arr2 = arr1  # reference copy
# arr3 = arr2.copy()  # normal copy
# arr2[3] = 70  # it will change arr1
#
# print(arr1)
# print(arr2)
# print(arr3)  # remains untouched


numbers1 = np.random.randint(1,100,10)
numbers2 = np.random.randint(1,100,10)

print(numbers1)
print(numbers2)
# result = numbers1 + numbers2# it will sum number1 and number2 element by element
# result = numbers1 + 20 # add 20 to every element
# result = numbers1 - numbers2
# result = numbers1 * numbers2
# result = numbers1 / numbers2
# result = numbers1 / 10 #divide every element by 10
# result = np.sin(numbers1)
# result = np.cos(numbers1)
# result = np.tan(numbers2)
# result = np.sqrt(numbers2) #square root
# result = np.log(numbers2)

multi_numbers1 = numbers1.reshape(2,5)#2 parts include 5 elements
multi_numbers2 = numbers2.reshape(2,5)#//

print(multi_numbers1)
print(multi_numbers2)

# result = np.vstack((multi_numbers1,multi_numbers2)) #sums vertically
# result = np.hstack((multi_numbers1,multi_numbers2)) #sums vertically

# result = numbers2 > 50 #returns true or false after the comparison
# result = numbers1 % 2 == 0

print(result)








