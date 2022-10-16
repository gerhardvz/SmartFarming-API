from importlib import resources

from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db = None
ma = None


def setDB(app):
    global db
    db = SQLAlchemy(app)
    global ma
    ma = Marshmallow(app)


def getSQLiteSession(engine):
    Session = sessionmaker()

    Session.configure(bind=engine)

    return Session()
