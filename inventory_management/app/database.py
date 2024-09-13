from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

SQLALCHEMY_DATABASE_URL = "postgresql://deakinlab_n7w5_user:I0NHfqcbJRZaGIDOrr6UAGfwpyzjipWZ@dpg-cri0mglumphs73cb3oeg-a.oregon-postgres.render.com/deakinlab_n7w5" #os.getenv("DATABASE_URL")

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
