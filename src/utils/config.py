from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    """
    Read env from root file.
    Note: The variable name mentioned here should be the same in .env file
    """
    HTTP_HOST: str = Field(default="0.0.0.0")
    HTTP_PORT: int = Field(default=5050)
    DEBUG_MODE: bool = Field(default=False)

    # DB constants
    DB_HOST: str
    DB_PORT: int = Field(default=5432)
    DB_USER: str
    DB_PASSWORD: str
    DB_NAME: str = Field(default="log_db")

    LOG_FILE: str = Field(default="/tmp/logs.json")


settings = Settings()
