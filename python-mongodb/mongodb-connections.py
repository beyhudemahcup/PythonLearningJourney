import pymongo
from bson.objectid import ObjectId


myclient = pymongo.MongoClient("mongodb://localhost:27017")

mydb = myclient["node-app"]  # search for node-app collection in db

# prints every database names
# print(myclient.list_database_names())

# throws an error if a collection exist in the same name
# product_collection = mydb.create_collection("products")
# does not throw an exception
product_collection = mydb["products"]

product = {"name": "Samsung S11", "price": 500}

# insert one
# result = product_collection.insert_one(product)

# insert many
# productList = [
#     {"name": "Samsung S11", "price": 500},
#     {"name": "Samsung S10", "price": 400},
#     {"name": "Samsung S9", "price": 300},
#     {"name": "Samsung S8", "price": 200},
#     {"name": "Samsung S7", "price": 100}
# ]
# result = product_collection.insert_many(productList)

# select one
# result = product_collection.find_one()

# select every field
# for i in product_collection.find():
#     print(i)

# select every field but stricted
# for i in product_collection.find({}, {"_id": 0}):
#     print(i)


#filter
filter = {"name": "Samsung S11"}
# result = product_collection.find(filter)
result = product_collection.find_one({"_id": ObjectId("66bba9a1ef3f7edb10184333")})
print(result)

# for i in result:
#     print(i)

#MONGO DB OPERATORS
# returns a data price value is equal to 500
# result = product_collection.find({
#     "price": {
#         "$eq": 500
#     }
# })

# result = product_collection.find({
#     "name": {
#         "$in": ["Samsung S12", "Samsung S11"]
#     }
# })

# less than or equal to 300
# result = product_collection.find({
#     "price": {
#         "$lte": 300
#     }
# })

# name starts with s
# result = product_collection.find({
#     "name": {"$regex": "^S"}
# })


# print(result.inserted_ids)
# print(mydb.list_collection_names())

#sorting
# result = product_collection.find().sort("name")
# result = product_collection.find().sort("price", -1)
# result = product_collection.find().sort([("name", 1), ("price", -1)])

# for i in result:
#     print(i)

# update-one
# product_collection.update_one(
#     {"name": "Samsung S9"},
#     {"$set": {
#         "name": "IPhone 9"
#     }}
# )

#update-many
# product_collection.update_many(
#     {"name": "Samsung S11"},
#     {"$set": {
#         "price": 600
#     }}
# )

# for i in product_collection.find():
#     print(i)
#

# delete-one
product_collection.delete_one({"name": "Samsung S7"})
# delete-many
# product_collection.delete_many({"name": {"$regex": "^S"}})
# means delete all data
product_collection.delete_many({})

for i in product_collection.find():
    print(i)

















