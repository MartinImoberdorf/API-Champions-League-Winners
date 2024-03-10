import os
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


sqlite_name="../winners.sqlite"
base_dir=os.path.dirname(os.path.realpath(__file__))
databaseURL=f"sqlite:///{os.path.join(base_dir,sqlite_name)}"

engine=create_engine(databaseURL, echo=True)

session=sessionmaker(bind=engine)

base=declarative_base()