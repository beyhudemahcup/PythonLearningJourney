import pandas as pd
import numpy as np

personels = {
    'Employees': ['Ahmet Yılmaz', 'Can Er', 'Hasan Korkmaz', 'Cenk Saymaz', 'Ali Turan', 'Rıza Er', 'Mustafa Can'],
    'Department': ['Human Resources', 'Information Technology', 'Accounting', 'Human Resources',
                   'Information Technology', 'Accounting', 'Human Resources'],
    'Age': [30, 25, 45, 50, 23, 34, 42],
    'Address': ['Kadıköy', 'Tuzla', 'Maltepe', 'Tuzla', 'Maltepe', 'Tuzla', 'Kadıköy'],
    'Salary': [50000, 30000, 40000, 35000, 27500, 65000, 45000]
}

df = pd.DataFrame(personels)
salary_sum = df["Salary"].sum()
result = df.groupby("Department").groups
result_address = df.groupby(["Department", "Address"]).groups

# for name, group in df.groupby("Address"):
#     print(name)
#     print(group)

# for name, group in df.groupby("Department"):
#     print(name)
#     print(group)

# we can get only one group detail like this
result_Kadikoy = df.groupby("Address").get_group("Kadıköy")
result_IT = df.groupby("Department").get_group("Information Technology")
sum_department = df.groupby("Department").sum()  # age and salary summary for every department
avg_department = df.groupby("Department").agg(
    {"Salary": "mean", "Age": "mean"})  # age and salary average for every department
agg_department = df.groupby("Department").agg({"Salary": np.mean, "Age": np.mean})
count_address = df.groupby("Address")["Employees"].count()
max_salary = df.groupby("Department")["Salary"].max()
max_salary_IT = df.groupby("Department")["Salary"].max()["Information Technology"]

print(df)
# print(result)
print(result_Kadikoy)
print(result_IT)
print(sum_department)
print(count_address)
print(max_salary)
print(max_salary_IT)
print(agg_department)
print(avg_department)
# print(result_address)
# print(salary_sum)
