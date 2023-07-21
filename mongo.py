from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

# connection to the MongoDB server:
try:
    client = MongoClient("mongodb://localhost:27017/")
    print("Connected successfully")
except ConnectionFailure:
    print("Could not connect to MongoDB server")

# Access to the database
db = client.mongoWithPython

# Using collection named 'user'
user = db.user

# Data to be inserted
data = {
    "name": "Moussa",
    "age": 30,
    "city": "Dakar"
}
# Insert the data
result = user.insert_one(data)
print("Data inserted. Inserted ID:", result.inserted_id)

# Find all documents in the user collection
documents = user.find()
# Find with filtering
# documents = user.find({"age" : 30})

# Print each document in the user collection
for document in documents:
    print(document)


# Update a document with a specific condition
condition = {"name": "Moussa"}
new_data = {"$set": {"age": 35}}
result = user.update_one(condition, new_data)
print("Matched count:", result.matched_count)
print("Modified count:", result.modified_count)


# Delete a document with a specific condition
condition = {"name": "Moussa"}
result = user.delete_one(condition)
print("Deleted count:", result.deleted_count)

# db.close()