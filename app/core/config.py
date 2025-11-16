from pydantic import BaseSettings


class Settings(BaseSettings):
    app_author: str
    db_url: str = 'postgres://login:password@127.0.0.1:5432/room_reservation'
    path: str
    app_title: str = "Бронирование переговорок"

    class Config:
        env_file = ".env"


settings = Settings()
