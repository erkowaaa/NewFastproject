from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


DB_URL = 'postgresql://postgres:admin@localhost/python123'

engine = create_engine(DB_URL)

SessionLocal = sessionmaker(bind=engine)

Base: object = declarative_base()