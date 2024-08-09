import pandas as pd
import numpy as np
import sqlite3

# db connection
connection = sqlite3.connect("datasets/sample.db")

df_csv = pd.read_csv("datasets/sample.csv")
df_json = pd.read_json("datasets/sample.json")
df_xlsx = pd.read_excel("sample.xlsx")
df_db = pd.read_sql_query("SELECT * FROM students", connection)

print(df_csv)
print(df_json)
print(df_xlsx)
print(df_db)
