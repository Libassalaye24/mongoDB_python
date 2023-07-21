from flask import Flask, jsonify , render_template, request
from flask_pymongo import PyMongo
import json
from bson import ObjectId
from bson.json_util import dumps
from flask_cors import CORS

class CustomJSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return super().default(o)

class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        return obj.__dict__    

# ! app flask
app = Flask(__name__)
CORS(app ,origins="http://localhost:8080")
app.json_encoder = CustomJSONEncoder

# ! config database with mongoDB
app.config['MONGO_URI'] = 'mongodb://localhost:27017/blog2'

# ! get database
mongo = PyMongo(app)

# ?? api function start
user_aggregate = [
    {
            "$lookup": {
                "from": "adresse",
                "localField": "address",
                "foreignField": "_id",
                "as": "address"
            },
        },
        {
            '$unwind': '$address'
        },
        {
            '$project': {
                '_id': 0,
                'name': 1,
                'username': 1,
                'email': 1,
                'phone': 1,
                'website': 1,
                'address.street': 1,
                'address.city': 1,
                'address.suite': 1,
                'address.zipcode': 1,
                'address.geo': 1,
            }
        }
]


#? get users
@app.route('/api/users', methods=['GET'])
def get_users():
    users = mongo.db.user.find()   
    # return render_template('users.html', users=users)
    return dumps(users)

#? get one user
@app.route('/api/users/<id>', methods=['GET'])
def get_user(id):
    user = mongo.db.user.find_one({'_id': ObjectId(id)})
    if user : 
        return dumps(user)
    else :
        return jsonify({'message': 'user not found' , 'code' : 404})
    
#? add user   
@app.route('/api/users', methods=['POST'])
def add_user():
    data = request.get_json()
    user = mongo.db.user.insert_one(data)
    if user.acknowledged :
        return jsonify({'message' : "User created successfully with ID :%s" % user.inserted_id})
    else :
        return jsonify({'message': 'Could not insert user' , 'code' : 404})

#? update user
@app.route('/api/users/<id>', methods=['PUT'])
def update_user(id):
    data = request.get_json()
    
    print('data update ',data)
    user = mongo.db.user.update_one({'_id': ObjectId(id)}, {'$set': data})
    if user.modified_count == 1 :
        return jsonify({'message' : "User updated successfully with ID :%s" % user.modified_count})
    else : 
         return jsonify({'message': 'Update user failed' , 'code' : 404})

#? delete user
@app.route('/api/users/<id>', methods=['DELETE'])
def delete_user(id):
    user = mongo.db.user.delete_one({'_id': ObjectId(id)})
    if user.deleted_count == 1 :
        return jsonify({'message' : "User deleted successfully ","code" : 200,"data" : user.deleted_count })
    else :
        return jsonify({'message': 'Delete user failed', 'code' : 404})
    
#? get posts
@app.route('/api/posts', methods=['GET'])
def get_posts():
    posts = mongo.db.post.find()   
    # return render_template('users.html', users=users)
    return dumps(posts)

#? get post by user
@app.route('/api/posts/<user>' , methods=['GET'])
def get_posts_by_user(user):
    posts = mongo.db.post.find({'userId' : ObjectId(user)})
    return dumps(posts)


#? delete one post
@app.route('/api/posts/<id>', methods=['DELETE'])
def delete_post(id):
    post = mongo.db.post.delete_one({'_id': ObjectId(id)})
    if post.deleted_count == 1 :
        return jsonify({'message' : "Post deleted successfully ","code" : 200,"data" : post.deleted_count })
    else :
        return jsonify({'message': 'Delete post failed', 'code' : 404})
    
# ?? api function end 


# ! run flask app
if __name__ == '__main__':
    app.run(debug=True)


