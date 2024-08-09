import pandas as pd
import numpy as np

data = np.random.randint(10, 100, 75).reshape(15, 5)
df = pd.DataFrame(data, columns=["Column1", "Column2", "Column3", "Column4", "Column5"])
result = df

# columns as list
# result = df.columns

# returns first (parameter) rows of DataFrame
# result_head = df.head(3)

# returns last (parameter) rows of DataFrame
# result_tail = df.tail(2)

# first 5 element from Column2
# result = df["Column2"].head()
# result = df.Column2.head() # it does the same

# returns column1 with the matching conditions + adds same rows from column3
result_condition1 = df[df["Column1"] > 50][["Column1", "Column3"]]
result_condition2 = df[(df["Column2"] > 20) & (df["Column2"] < 40)]
result_condition3 = df.query("Column1 >= 90 | Column1 % 2 == 1")

print(result_condition1)
print(result_condition2)
print(result_condition3)
# print(result_head)
# print(result_tail)
