import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship,Session
from sqlalchemy import create_engine

engine = create_engine("sqlite:///web/Sqlite-Data/example.db")
session = Session(bind=engine)