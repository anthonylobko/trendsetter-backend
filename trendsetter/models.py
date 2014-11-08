from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, \
    Integer,\
    String, \
    Text, \
    ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()


class Idea(Base):
    """
    A representation of a single idea.
    """
    __tablename__ = 'ideas'

    id = Column(Integer,
                primary_key=True,
                nullable=False)

    username = Column(String(256),
                      ForeignKey("User.username"),
                      nullable=False)

    idea = Column(Text,
                  nullable=False)


class User(Base):
    """
    A single user in the system
    """
    __tablename__ = 'users'


    id = Column(Integer,
                primary_key=True,
                nullable=False)

    username = Column(String(256),
                      unique=True,
                      nullable=False)

    ideas = relationship("Idea")
