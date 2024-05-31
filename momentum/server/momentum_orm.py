import datetime
# for timezone()
import pytz

from sqlalchemy import create_engine, Column, types, MetaData , ForeignKey, func 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import declarative_base

metadata = MetaData()
base_user = declarative_base(metadata = metadata)





class User(base_user):
    """
    Table ``users`` with fields:
    * ``user_id`` - Serial primary key integer
    * ``username`` - VARCHAR(50), unique and not null
    * ``email`` - VARCHAR(100), unique and not null
    * ``password_hash`` - VARCHAR(255), not null
    * ``phone_number`` - VARCHAR(20)
    * ``created_at`` - TIMESTAMP, default CURRENT_TIMESTAMP
    """
    __tablename__ = 'users'
    user_id = Column(types.Integer, primary_key=True)
    username = Column(types.String(length=50), unique=True, nullable=False)
    email = Column(types.String(length=100), unique=True, nullable=False)
    password_hash = Column(types.String(length=255), nullable=False)
    phone_number = Column(types.String(length=20))
    #created_at = Column(types.TIMESTAMP, server_default=types.func.current_timestamp())
    created_at = Column(types.TIMESTAMP, server_default=func.now())
    #created_at = Column(types.TIMESTAMP, server_default=datetime.datetime.now(pytz.timezone('Asia/Kolkata')))
