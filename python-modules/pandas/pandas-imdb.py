import pandas as pd

df = pd.read_csv("datasets/imdb.csv")

# 1- Information about the file.
result = df
result = df.columns
result = df.info
# 2- Show the first 5 records.
result = df.head()
# 3- Show the first 10 records.
result = df.head(10)

# 4- Show the last 5 records.
result = df.tail()

# 5- Show the last 10 records.
result = df.tail(10)

# 6- Select only the Movie_Title column.
result = df["Movie_Title"]

# 7- Select the first 5 records containing only the Movie_Title column.
result = df["Movie_Title"].head()

# 8- Select the first 5 records containing only the Movie_Title and Rating columns.
result = df[["Movie_Title", "Rating"]].head()

# 9- Select the last 7 records containing only the Movie_Title and Rating columns.
result = df[["Movie_Title", "Rating"]].tail(7)

# 10- Select the second 5 records containing only the Movie_Title and Rating columns.
result = df[5:10][["Movie_Title", "Rating"]]

# 11- Select the first 50 records containing only the Movie_Title and Rating columns with an IMDb rating of 8.0 and above.
result = df[df["Rating"] >= 8.0][["Movie_Title", "Rating"]].head(50)

# 12- Get the names of movies released between 2014 and 2015.
result = df[(df["YR_Released"] >= 2014) & (df["YR_Released"] <= 2015)][["Movie_Title"]]

# 13- List the movies with a number of reviews (Num_Reviews) greater than 100,000 or with an IMDb rating between 8 and 9.
result = df[((df["Rating"] >= 8.0) & (df["Rating"] <= 9.0)) | (df["Num_Reviews"] > 100000)]
print(result)
