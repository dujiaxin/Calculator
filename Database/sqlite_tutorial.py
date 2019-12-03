from sqlalchemy.orm import create_engine, Session
engine = create_engine("postgres+psycopg2://postgres:pass@localhost/mydb")
session = Session(bind=engine)