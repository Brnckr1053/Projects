from flask import Flask
app = Flask(__name__)
from flask_app.controllers import recipes
from flask_app.controllers import users

app.secret_key = "shhhhh"