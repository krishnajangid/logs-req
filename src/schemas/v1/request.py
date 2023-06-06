"""Request classes schema for all the incoming requests."""
from enum import Enum

from pydantic import BaseModel


class EventEnum(str, Enum):
    LOGIN = 'login'
    LOGOUT = 'logout'


class LogRequest(BaseModel):
    user_id: int
    event_name: EventEnum

    class Config:
        use_enum_values = True
