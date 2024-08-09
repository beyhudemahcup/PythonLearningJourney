import pandas as pd

data = pd.read_csv("datasets/nba.csv")

df = pd.DataFrame(data)

# 1. **Retrieve the first 10 records.**
result = df.head(10)

# 2. **How many records are there in total?**
result = len(df.index) #458

# 3. **What is the average salary of all players?**
result = df["Salary"].mean()
print(result)
# 4. **What is the highest salary?**
result = df["Salary"].max()

# 5. **Who is the player with the highest salary?**
max_salary = df["Salary"].max()
player_with_max_salary = df.loc[df["Salary"] == max_salary, "Name"].iloc[0]  # RIP Kobe
print(player_with_max_salary)

# 6. **Retrieve the names and teams of players aged between 20 and 25, sorted in descending order.**
ages_restricted = (df["Age"] >= 20) & (df["Age"] <= 25)
result = df.loc[ages_restricted]
result = result.sort_values("Age", ascending=False)
result = result[["Name", "Team", "Age"]]

# 7. **Which team does the player named "John Holland" play for?**
player_info = df.loc[df["Name"] == "John Holland"]
result = player_info[["Team", "Name"]]

# 8. **What is the average salary of players by team?**
result = df.groupby("Team")["Salary"].mean()

# 9. **How many different teams are there?**
result = df["Team"].nunique()  # 30

# 10. **How many players are there in each team?**
result = df["Team"].value_counts()

# 11. **Find records where the name contains "and".
result = df["Name"].str.contains("and", case=False, na=False)
name_contains_and = df[result]
print(name_contains_and)








