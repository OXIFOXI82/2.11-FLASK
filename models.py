import atexit
import datetime
import os

import sqlalchemy
from sqlalchemy import Table, Index, Integer, String, Column, Text, \
    DateTime, Boolean, PrimaryKeyConstraint, \
    UniqueConstraint, ForeignKeyConstraint, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import DateTime, String, create_engine, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker, relationship

POSTGRES_PASSWORD = "post_oxana"
POSTGRES_USER = "oxana"
POSTGRES_DB = "flask"
POSTGRES_HOST = "127.0.0.1"
POSTGRES_PORT = "5432"

PG_DSN = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

engine = create_engine(PG_DSN)
Session = sessionmaker(bind=engine)

#atexit.register(engine.dispose)

Base = sqlalchemy.orm.declarative_base()


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, index=True, nullable=False)
    password = Column(String(100), index=True, nullable=False)
    registration_time = Column(DateTime, server_default=func.now())
    advert = relationship('Advert')

    @property
    def dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "password": self.password,
            "registration_time": self.registration_time.isoformat(),
        }


class Advert(Base):
    __tablename__ = "advert"

    id = Column(Integer, primary_key=True)
    header = Column(String(100), unique=True, index=True, nullable=False)
    description = Column(String(1000), index=True, nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    owner_id = Column(Integer, ForeignKey('user.id'))
    owner = relationship(User)

    @property
    def dict(self):
        return {
            "id": self.id,
            "header": self.header,
            "description": self.description,
            "created_at": self.created_at.isoformat(),
            "owner_id": self.owner_id
        }


Base.metadata.create_all(bind=engine)
