import pandas as pd

# read csv file
data = pd.read_csv("datasets/nba.csv")

# set printing option
pd.set_option('display.max_columns', None)

# delete Nan areas
data.dropna(inplace=True)

# upper name field
data["Name"] = data["Name"].str.upper()
# lower name field
data["Name"] = data["Name"].str.lower()

# searchs for how many 'a' letters the Name field contains
data["index"] = data["Name"].str.find('a')

# returns players who have jordan in their names
# data = data[data.Name.str.contains('jordan')]

# replaces team names contain los to dos
data.Team = data.Team.str.replace("Los", "Dos")

# seperate names as firstname and last name
mask = data["Name"].str.split().str.len() == 2
data[["First_Name", "Last_Name"]] = data["Name"].loc[mask].str.split(expand=True)

print(data.head(50))

# data = data[data.Team.str.replace('los ','dos')]
#
# print(data.head(10))
# print(data["index"])
