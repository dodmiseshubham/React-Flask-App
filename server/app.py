# from flask import Flask,jsonify
# app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     response = jsonify(message="Simple server is running hellpo")

#     # Enable Access-Control-Allow-Origin
#     response.headers.add("Access-Control-Allow-Origin", "*")
#     return response

from flask import Flask,jsonify,request
from flask_pymongo import PyMongo
from flask_cors import cross_origin

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/react_app"
mongo = PyMongo(app)

@app.route("/")
def home_page():
    online_users = mongo.db.user.find({"online": True})
    user=""
    for doc in online_users:
        print("online users ",doc['name'])
        user = doc['name']
    response = jsonify(message=user)

    # Enable Access-Control-Allow-Origin
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@app.route("/post-data", methods = ['POST'])
@cross_origin()
def get_query_from_react():
    data = request.get_json()
    # data = request.args.get('nm')
    doc = mongo.db.user.insert({'name': data['data'], 'online':False})
    print("post")
    print(data)
    return data