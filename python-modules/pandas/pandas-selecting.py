import pandas as pd
from numpy.random import randn

df = pd.DataFrame(randn(3, 3), index=["A", "B", "C"], columns=["Column1", "Column2", "Column3"])

result = df
# resultCol = df["Column1"]
# resultCols = df[["Column1","Column2"]]

# loc["row","column"]
result_serie = df.loc["B"]  # returns a row named 'B'

# if you want to choose columns => loc[:,"column"]
result_columns = df.loc[:, "Column3"]  # returns a column named 'Column1'

# get row data with index number
result_index = df.iloc[1]

# insert another column
result["Column4"] = pd.Series(randn(3), ["A", "B", "C"])
# another column is created from existing columns
result["SUM"] = df["Column1"] + df["Column2"] + df["Column3"] + df["Column4"]

# delete a column
result_dropped = df.drop("Column4", axis=1)  # axis defines y coordinate
# df.drop("Column4", axis=1, inplace=True) inplace= updates df.drop()


print(result)
print(result_serie)
print(result_columns)
print(result_index)
print(result_dropped)
