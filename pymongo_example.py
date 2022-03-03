from pymongo import MongoClient
from flask import Flask
from bson.json_util import dumps
import names

app = Flask(__name__)

client = MongoClient("mongodb+srv://blog:blog@cluster0.2grje.mongodb.net/myFirstDatabase")
db = client.flask_example_db

@app.route("/create")
def add_user():
  result = db.users.insert_one({"name": names.get_full_name()})
  return str(result.inserted_id)

@app.route("/list")
def get_user():
  users = list(db.users.find({}))
  return dumps(users)
