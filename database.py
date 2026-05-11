from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base


database_url = 'sqlite:///performance.db'

engine = create_engine(
    database_url
)

SessionLocal = sessionmaker(
    bind=engine
)


Base = declarative_base()
