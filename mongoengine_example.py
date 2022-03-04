from flask import Flask
from mongoengine import *
import names

app = Flask(__name__)

connect(host="<CONNECTION_STRING>")

class User(Document):
    name = StringField()

@app.route("/create")
def add_user():
    new_user = User(name=names.get_full_name())
    new_user.save()
    return str(new_user.id)

@app.route("/list")
def get_user():
    return User.objects.to_json()
