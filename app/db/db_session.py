# connect to our database where we are going to use it for our models
# tell SQLAlchemy how to connect to the DB (e.g. what is the database called, how do we connect to it, what flavor of SQL is it)
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

# SQLALCHEMY_DATABASE_URL = os.getenv("DB_CONN")
# defines the file where Postgress will persist data
SQLALCHEMY_DATABASE_URL = settings.db_url

# instantiate the enfine, passing in the Db connection URL
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# create a db session local for our database and bind it to our engine
# When working with the ORM, the session object is our main access point to the database
# the Session establishes all conversations with the database and represents a “holding zone” for all the objects
# which you’ve loaded or associated with it during its lifespan.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


