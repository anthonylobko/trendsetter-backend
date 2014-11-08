import os
from flask import Flask

APP = Flask(__name__)

@APP.route("/")
def hello():
    return "Hello world!"
