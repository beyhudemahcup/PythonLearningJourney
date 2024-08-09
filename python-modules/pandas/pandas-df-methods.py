import pandas as pd
import numpy as np

data = {
    "Column1": [1, 2, 3, 4, 5, 6],
    "Column2": [10, 20, 20, 40, 50, 65],
    "Column3": ["asd", "abc", "ade", "def", "fes", "sad"]
}

df = pd.DataFrame(data)


def getSquare(x):
    return x * x


result = df
result = df["Column2"].unique()
result = df["Column2"].nunique()  # number of unique element in specified column
result = df["Column2"].value_counts()
result = df["Column1"] * 2
result = df["Column1"].apply(getSquare)  # sending dataFrame to a method
df["Column4"] = df["Column3"].apply(len)  # column4 with the length value of column3
result = df.index
result = len(df.index)
result = df.sort_values("Column3", ascending=False)  # z to a

print(result)
print(df)
