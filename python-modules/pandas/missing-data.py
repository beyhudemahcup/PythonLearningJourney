import pandas as pd
import numpy as np

data = np.random.randint(10, 100, 15).reshape(5, 3)

df = pd.DataFrame(data, index=['a', 'c', 'd', 'f', 'h'], columns=['column1', 'column2', 'column3'])

df = df.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])

newColumn = [np.nan, 30, np.nan, 43, np.nan, 40, np.nan, 20]
df["column4"] = newColumn

result = df
result = df.drop("column2", axis=1)
result = df.drop(["column2", "column3"], axis=1)

# check if values are null or not
result = df.isnull()
result = df.notnull()
result = df["column3"].notnull()
# null values are only in column1
result = df[df["column1"].isnull()]["column1"]

# it drops null values
result = df.dropna()  # axis = 0 deletes row
result = df.dropna(axis=1)  # axis = 1 deletes column

result = df.dropna(how="any")  # returns any nan value
result = df.dropna(how="all")  # returns nan value if the entire row does not have nan values
result = df.dropna(subset=["column1", "column2"])  # searchs for only "column1" and"column2"
result = df.dropna(thresh=2)  # dont drop if 2 values are not Nan
result = df.fillna(value='no input')  # fills Nan values with the value variable

result = df.sum().sum()  # sums all the data for just one value
result = df.size  # returns element number
result = df.isnull().sum()  # sums of nan values. before this method we should change nan values like 1.0 to do easy calculation


def average(df):
    sum = df.sum().sum()
    size = df.size - df.isnull().sum().sum()
    return sum / size


result = df.fillna(value=average(df))  # switch to average number is calculated by average func

print(result)
print(df)
