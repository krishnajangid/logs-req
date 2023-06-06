from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from utils.constants import SQLALCHEMY_DATABASE_URL

engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_pre_ping=True)
db_session = sessionmaker(bind=engine)
base = declarative_base()


def get_db():
    db = db_session()
    try:
        yield db
    finally:
        db.close()
