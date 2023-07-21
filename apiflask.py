# from flask import Flask, jsonify , render_template
# from flask_pymongo import PyMongo
# import json
# from bson import ObjectId

# class CustomJSONEncoder(json.JSONEncoder):
#     def default(self, o):
#         if isinstance(o, ObjectId):
#             return str(o)
#         return super().default(o)
    
# # ! app flask
# app = Flask(__name__)

# app.json_encoder = CustomJSONEncoder

# # ! config database with mongoDB
# app.config['MONGO_URI'] = 'mongodb://localhost:27017/blogPy'

# # ! get database
# mongo = PyMongo(app)

# # ?? api function start
# user_aggregate = [
#     {
#             "$lookup": {
#                 "from": "adresse",
#                 "localField": "address",
#                 "foreignField": "_id",
#                 "as": "address"
#             },
#         },
#         {
#             '$unwind': '$address'
#         },
#         {
#             '$project': {
#                 '_id': 0,
#                 'name': 1,
#                 'username': 1,
#                 'email': 1,
#                 'phone': 1,
#                 'website': 1,
#                 'address.street': 1,
#                 'address.city': 1,
#                 'address.suite': 1,
#                 'address.zipcode': 1,
#                 'address.geo': 1,
#             }
#         }
# ]

 
# def aggregate_filters(key , val):
#   return  [
#         {'$match': {'username': 'Bat'}},
#         {
#             "$lookup": {
#                 "from": "adresse",
#                 "localField": "address",
#                 "foreignField": "_id",
#                 "as": "address"
#             },
#         },
#         {
#             '$unwind': '$address'
#         },
#         {
#             '$project': {
#                 '_id': 0,
#                 'name': 1,
#                 'username': 1,
#                 'email': 1,
#                 'phone': 1,
#                 'website': 1,
#                 'address.street': 1,
#                 'address.city': 1,
#                 'address.suite': 1,
#                 'address.zipcode': 1,
#                 'address.geo': 1,
#             }
#         }
#     ]
# @app.route('/api/users', methods=['GET'])
# def get_users():
#     users = mongo.db.user.aggregate(user_aggregate)
#     return jsonify(list(users))

# @app.route('/api/users/<username>', methods=['GET'])
# def get_user(username): 
#     pipeline = [
#         {'$match': {'username': username}},
#         {
#             "$lookup": {
#                 "from": "adresse",
#                 "localField": "address",
#                 "foreignField": "_id",
#                 "as": "address"
#             },
#         },
#         {
#             '$unwind': '$address'
#         },
#         {
#             '$project': {
#                 '_id': 0,
#                 'name': 1,
#                 'username': 1,
#                 'email': 1,
#                 'phone': 1,
#                 'website': 1,
#                 'address.street': 1,
#                 'address.city': 1,
#                 'address.suite': 1,
#                 'address.zipcode': 1,
#                 'address.geo': 1,
#             }
#         }
#     ]
#     user = mongo.db.user.aggregate(pipeline)
#     print(user)
#     return jsonify(user)

# # ?? api function end 


# # ! run flask app
# if __name__ == '__main__':
#     app.run()


