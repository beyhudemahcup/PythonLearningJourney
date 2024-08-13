import mysql.connector
from connection import conn
from datetime import datetime



# insert new product to Products table!
def insertProduct(name, price, imageUrl, description):
    cursor = conn.cursor()
    sql = "INSERT INTO Products(name,price,imageUrl,description) VALUES(%s,%s,%s,%s)"
    values = (name, price, imageUrl, description)

    cursor.execute(sql, values)
    try:
        conn.commit()
    except mysql.connector.Error as err:
        print("Error: ", err)
    finally:
        conn.close()
        print("Database connection is closed")


# insert new products to Products table!
def insertProducts(product_list):
    cursor = conn.cursor()
    sql = "INSERT INTO Products(name,price,imageUrl,description) VALUES(%s,%s,%s,%s)"
    values = product_list

    cursor.executemany(sql, values)
    try:
        conn.commit()
        print(f"{cursor.rowcount} new record are added!")
        print(f"Last record id is {cursor.lastrowid}")
    except mysql.connector.Error as err:
        print("Error: ", err)
    finally:
        conn.close()
        print("Database connection is closed")


# get product list
def getProducts():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")

    try:
        result = cursor.fetchall()
        print(result)
    except mysql.connector.Error as err:
        print("Error: ", err)
    finally:
        conn.close()
        print("Database connection is closed")


# get product list by id
def getProductsById(id):
    cursor = conn.cursor()
    params = (id,)
    cursor.execute("SELECT * FROM products where id=%s", params)

    result = cursor.fetchone()
    print(result)


# get product list by id
def getProductInfo():
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM products")

    result = cursor.fetchone()
    print(result)


# getProducts()
getProductsById((5)) # returns a product with id = 5

# product_list = []

# while True:
#     name = input("Product Name: ")
#     price = input("Product Price: ")
#     imageUrl = input("Image Url: ")
#     description = input("Product Description: ")
#
#     product_list.append((name, price, imageUrl, description))
#
#     result = input("Do you want to continue? (Y,N)").lower()
#     if result == "n":
#         print("Database insert is done.")
#         print(product_list)
#         insertProducts(product_list)
#         break


# 4- Aşağıdaki sorguları yazınız.
#   a- Tüm öğrenci kayıtlarını alınız.
#   b- Tüm öğrencilerin sadece öğrenci no, ad ve soyad bilgilerini alınız.
#   c- Sadece kız öğrencilerin ad ve soyadlarını alınız.
#   d- 2003 doğumlu öğrenci bilgilerini alınız.
#   e- İsmi Ali ve doğum tarihi 2005 olan öğrenci bilgilerini alınız.
#   f- ad veya soyadı içinde 'an' ifadesi geçen kayıtları alınız.
#   g- Kaç erkek öğrenci vardır ?
#   h- Kız öğrencileri harf sırasına göre getiriniz.

# 5- Aşağıdaki güncelleme sorularını yapınız.
#   a- id' e göre aldığınız bir öğrencinin bilgilerini güncelleyiniz.
#   b- cinsiyet' e göre aldığınız bir öğrencinin bilgilerini güncelleyiniz.










