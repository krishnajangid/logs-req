import time

from sqlalchemy import Column, Integer, String

from utils.database import engine, base


# Define models
class Log(base):
    __tablename__ = "logs"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    unix_ts = Column(Integer, default=int(time.time()))
    user_id = Column(Integer)
    event_name = Column(String)


def init_db():
    base.metadata.create_all(engine)
