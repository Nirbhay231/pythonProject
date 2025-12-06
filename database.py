from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "postgresql://postgres:admin@localhost:5432/pythonproject5"

engine = create_engine(DATABASE_URL)
sessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)
Base = declarative_base()