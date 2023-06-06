from sqlalchemy.exc import IntegrityError

from models.models import Log
from utils.database import db_session


class LogLayer:

    @staticmethod
    async def save(log_list: list) -> None:
        """
        Save logs to db

        :param log_list: List containing log dict
        :return: None
        """
        with db_session() as session:
            try:
                session.bulk_insert_mappings(Log, log_list)
                session.commit()
                session.close()
            except IntegrityError:
                pass

    @staticmethod
    async def get_all(offset: int, limit: int) -> list:
        """
        Get all logs

        :param offset: Offset
        :param limit: Limit
        :return: List
        """
        with db_session() as session:
            return session.query(Log).offset(offset).limit(limit).all()
