import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    auth_plugin='1234',
    database="node-app"
)