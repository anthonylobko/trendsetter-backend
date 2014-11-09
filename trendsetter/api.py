import os
from flask import Flask, request
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, \
    Integer,\
    String, \
    Text, \
    ForeignKey
from sqlalchemy.orm import relationship
import json


app = Flask(__name__)
app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
db = SQLAlchemy(app)


def post_ideas(username, idea, timestamp):
    """
    Write a single idea to the database.

    Arguments:
     * username: The username of the person that posted the idea.
     * idea: A string representing the entire idea
     * device_id: The ID for the device the idea was submitted
       from.
    """
    insert = Idea(username=username,
                  idea=idea,
                  timestamp=timestamp)
    db.session.add(insert)
    db.session.commit()
    return "Insert happened successfully?"


@app.route("/")
def hello():
    return "Hello world!"


@app.route("/get/<int:limit>/<int:offset>")
def get(limit, offset):
    return json.dumps(
        [
            {"id": item.id,
             "username": item.username,
             "idea": item.idea,
             "up": idea.up,
             "down": idea.down,
             "timestamp": item.timestamp}
            for item
            in db.session.query(Idea).order_by(Idea.id)
            [offset:offset + limit]
        ]
    )


@app.route("/post", methods=["POST", "GET"])
def post():
    if request.method == "POST":
        return post_ideas(
            request.form["username"],
            request.form["idea"],
            request.form["timestamp"]
            )
    else:
        return "No post stuff?"


@app.route("/up/<int:id>")
def up(id):
    pass

@app.route("/down/<int:id>")
def down(id):
    pass

class Idea(db.Model):
    """
    A representation of a single idea.
    """
    __tablename__ = 'ideas'

    id = Column(Integer,
                primary_key=True,
                nullable=False)

    username = Column(String(256),
                      nullable=False)

    idea = Column(Text,
                  nullable=False)

    up = Column(Integer,
                nullable=False,
                default=0)

    down = Column(Integer,
                  nullable=False,
                  default=0)

    timestamp = Column(Integer,
                       nullable=False)
