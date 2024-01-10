from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///dog_adopt.db")
Session = sessionmaker(bind=engine)
session = Session()