import pandas as pd

customers = {
    "CustomerId": [1, 2, 3, 7],
    "FirstName": ["Damla", "Deniz", "Mert", "Ebru"],
    "LastName": ["Cengiz", "Derya", "Baret", "Saniye"]
}

orders = {
    "OrderId": [10, 20, 30, 40],
    "CustomerId": [3, 5, 6, 7],
    "OrderDate": ["2024-08-07", "2024-08-07", "2024-08-08", "2024-08-06"]
}

# Data frames are created
df_customers = pd.DataFrame(customers, columns=["CustomerId", "FirstName", "LastName"])
df_orders = pd.DataFrame(orders, columns=["OrderId", "CustomerId", "OrderDate"])

# print(df_orders)
# print(df_customers)

result_inner = pd.merge(df_customers, df_orders, how="inner")  # inner join returns data have same customerId
result_left = pd.merge(df_customers, df_orders, how="left")  # left join
result_right = pd.merge(df_customers, df_orders, how="right")  # right join

print(result_inner)
print(result_left)
print(result_right)
