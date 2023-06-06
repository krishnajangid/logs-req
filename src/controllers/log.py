import asyncio
import json
import os
import time

from repository.log import LogLayer
from utils.common import get_logger
from utils.config import settings

LOGGER = get_logger()


class LogBuffer:
    def __init__(self, file_path: str = settings.LOG_FILE):
        self.__file_path: str = file_path

    def get_file_age(self) -> float:
        """
        Get file age

        :return: float
        """
        return time.time() - os.path.getmtime(self.__file_path)

    def get_file_size(self) -> int:
        """
        Function to get the file_path size

        :return: int
        """
        return os.path.getsize(self.__file_path)

    def clear_file(self) -> None:
        """
        Reset file

        :return: None
        """
        with open(self.__file_path, "w") as file:
            file.truncate()

    def add_log(self, log: str) -> None:
        """
        Add logs to file

        :param log: Log object
        :return:
        """

        with open(self.__file_path, "a") as file:
            file.write(f"{log}\n")

    async def flush_logs(self) -> None:
        """
        Flush logs to db

        :return: None
        """

        LOGGER.info("Flushing logs to db")

        data_list = []
        with open(self.__file_path) as file:
            for line in file:
                data_list.append(json.loads(line))
        if len(data_list) > 0:
            await LogLayer.save(data_list)
            self.clear_file()

    async def flush_logs_periodically(self) -> None:
        """
        Flush logs periodically

        :return: None
        """
        while True:
            LOGGER.info("Running task in background")
            await asyncio.sleep(30)
            await self.flush_logs()
