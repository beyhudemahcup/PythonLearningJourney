import pandas as pd
import numpy as np

'''
dataframes are combinations of 2 Series()
(looks like excel table btw)
   apples  oranges
0       3        0
1       2        3
2       1        5
3       0        9
'''

s1 = pd.Series([3, 2, 1, 0])
s2 = pd.Series([0, 3, 5, 9])

data = dict(apples=s1, oranges=s2)
list = [["metin", 50], ["mert", 75], ["cemil", 95], ["buse", 80]]
dict = {"Name": ["Mert", "Banu", "Arzu", "Yagmur"], "Grade": [50, 25, 75, 65]}

df = pd.DataFrame(data)
df_empty = pd.DataFrame()
df_list = pd.DataFrame(list)
df_list_arranged = pd.DataFrame(list, index=[1, 2, 3, 4], columns=["Name", "Grade"])
df_dict = pd.DataFrame(dict, index=["546", "642", "883", "321"])  # school numbers as indexes

print(df)
print(df_empty)
print(df_list)
print(df_list_arranged)
print(df_dict)
