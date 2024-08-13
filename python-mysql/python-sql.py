import mysql.connector

my_con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    auth_plugin='1234',
    database="schoolDB"
)

mycursor = my_con.cursor()

"""
mycursor.execute("SELECT * FROM products")

for i in mycursor:
    print(i)
"""

# create schooldb and student table

# mycursor.execute("CREATE DATABASE schoolDB")
# mycursor.execute("""
# CREATE TABLE Student (
#     ID INT AUTO_INCREMENT PRIMARY KEY,
#     FirstName VARCHAR(50),
#     LastName VARCHAR(50),
#     Birthdate DATE,
#     Gender VARCHAR(10)
# )
# """)

# my_con.commit()















