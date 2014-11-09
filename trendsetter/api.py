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
    insert = Idea(username=username, idea=idea)
    db.session.add(insert)
    db.session.commit()
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

Base = declarative_base()
Engine = create_engine( os.environ['DATABASE_URL'] )
Base.metadata.create_all(Engine)

class Idea(db.Model):
    """
    A representation of a single idea.
    """
    __tablename__ = 'ideas'

    id = Column(Integer,
                primary_key=True,
                nullable=False)

    username = Column(String(256),
#                      ForeignKey("User.username"),
                      nullable=False)

    idea = Column(Text,
                  nullable=False)


# class User(db.Model):
#     """
#     A single user in the system
#     """
#     __tablename__ = 'users'


#     id = Column(Integer,
#                 primary_key=True,
#                 nullable=False)

#     username = Column(String(256),
#                       unique=True,
#                       nullable=False)

#     ideas = relationship("Idea.username")
