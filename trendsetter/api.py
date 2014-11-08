import os
from trendsetter import models
from flask import Flask, request
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
db = SQLAlchemy(app)


def post_ideas(username, idea):
    """
    Write a single idea to the database.

    Arguments:
     * username: The username of the person that posted the idea.
     * idea: A string representing the entire idea
     * device_id: The ID for the device the idea was submitted
       from.
    """
    insert = models.Idea.insert()
    db.session.execute(insert,
                       username=username,
                       idea=idea)
    return "Insert happened successfully?"


@app.route("/")
def hello():
    return "Hello world!"


@app.route("/post", methods=["POST", "GET"])
def post():
    if request.method == "POST":
        return post_ideas(
            request.form["username"],
            request.form["idea"]
            )
    else:
        return "No post stuff?"
