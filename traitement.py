from pymongo import MongoClient;  
import requests;

client = MongoClient("mongodb://localhost:27017/")


# access to the database
db = client.blog2

# get collection from database

userCollection = db.user
postCollection = db.post
#

base_url = "https://jsonplaceholder.typicode.com/"

def find(type):
    return requests.get(base_url+type)

response_posts = find("posts")
response_users = find("users")

if response_posts.status_code == 200 :
    posts = response_posts.json()
else :
    print("Could not find posts")


if response_users.status_code == 200 :
    users = response_users.json()
else :
    print("Could not find users")

user_ids = []
for u1 in users :
    print("User: %s" % u1['address'])

    userSave = userCollection.insert_one(
        {
            "name": u1['name'],
            "username": u1['username'],
            "email": u1['email'],
            "phone": u1['phone'],
            "website": u1['website'],
            "address" : u1['address'],
            "company" : u1['company'],
        }
    )
    if userSave.acknowledged :
        print("User saved")
        for post in posts :
            if post['userId'] == u1['id'] :
                print("Post: %s" % post)
                postSave = postCollection.insert_one(
                    {
                        "title": post['title'],
                        "body": post['body'],
                        "userId": userSave.inserted_id
                    }    
                )
                if postSave.acknowledged :
                    print("Post saved ID: " ,postSave.inserted_id)
    else :
        print("Could not insert user")
