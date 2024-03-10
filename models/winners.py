from bd.database import base
from sqlalchemy import Column,Integer,String,Float

class Winner(base):
    __tablename__="winners"
    id=Column(Integer,primary_key=True,autoincrement=True)
    season=Column(String)
    year=Column(Integer)
    winner=Column(String)
    score=Column(String)
    runners_up=Column(String)
    stadium=Column(String)
    attendance=Column(Float)
