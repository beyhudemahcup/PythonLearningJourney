import pandas as pd
import numpy as np

numbers = [20, 30, 40, 50, 60]
letters = ['a', 'b', 'c', 'd', 'e']
scalar = 15
dict = {'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 50}
random_number = np.random.randint(10, 50, 5)

pandas_series_empty = pd.Series()
pandas_series_numbers = pd.Series(numbers)
pandas_series_letters = pd.Series(letters)
pandas_scalar = pd.Series(scalar)
pandas_scalar_numbers = pd.Series(scalar, numbers)  # gives scalar value to every numbers(it will be indexes)
pandas_series_let_ = pd.Series(numbers, letters)  # a= 20, b= 30 ...
pandas_series_dict = pd.Series(dict)
pandas_series_random = pd.Series(random_number)

# print(pandas_series_empty) #object
# print(pandas_series_numbers) #int64
# print(pandas_series_letters) #object
# print(pandas_scalar) #int64
# print(pandas_scalar_numbers)
print(pandas_series_let_)  # same formats
# print(pandas_series_dict) #//
# print(pandas_series_random)

# result = pandas_series_let_[0] # first element
# result = pandas_series_let_[-2:]  # last two element
# result = pandas_series_let_[['a','b','g']] # raise an error because 'g' is not in series
#preventing this we should use reindex method
# result = pandas_series_let_.reindex(['a','b','g'])
# result = pandas_series_let_.ndim # 1
# result = pandas_series_let_.dtype #data type
# result = pandas_series_let_.shape #5 element
# result = pandas_series_let_.sum() # sum all elements
# result = pandas_series_let_.max() #max value
# result = pandas_series_let_.sum() # min value
# result = pandas_series_let_ + pandas_series_let_ # values are doubled
# result = pandas_series_let_ + 50 # 50 added every element
# result = np.sqrt(pandas_series_let_) #square root for every element
# result = pandas_series_let_ > 34 # returns true-false

opel2018 = pd.Series([20,30,40,70],["astra","corsa","mokka","insignia"])
opel2019 = pd.Series([20,10,40,70],["astra","grandLand","mokka","insignia"])
total = opel2019 + opel2018
print(total)







