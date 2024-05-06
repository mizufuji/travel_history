# 3番目に作成 __init__.pyはその前に作成
#from typing import List, Optional
from sqlalchemy import create_engine, engine
#from sqlalchemy.orm import DeclarativeBase
#from sqlalchemy.schema import Column
#from sqlalchemy.types import Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"

#connect_argsはsqliteがDBの時のみ
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
