from sqlalchemy import Column, Integer, String

from app.core.db import Base


class MeetingRoom(Base):
    name = Column(String(100), unique=True, nullable=False)
