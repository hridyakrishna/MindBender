from sqlalchemy import *
from sqlalchemy import create_engine,declarative_base,Column,String

engine = create_engine('sqlite:///login.db', echo=True)
Base = declarative_base()

class User(Base):
__tablename__ = "users"

id = Column(String)
name = Column(String)
gender = Column(String)
email = Column(String)
username = Column(String)
password = Column(String)

def account(obj,id,name,gender,email,username,password):
    obj.id = id
    obj.name = name
    obj.gender = gender
    obj.email = email
    obj.username = username
    obj.password = password
    
Base.metadata.create_all(engine)