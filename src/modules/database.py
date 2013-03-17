from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from transaction import commit_on_success

Base = declarative_base()

def init(db_name = "tracker", user=""):
    host = "" if user == "" else "localhost"
    engine = create_engine("postgresql+psycopg2://%s@%s/%s" % (user, host, db_name))

    global session
    session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

    Base.query = session.query_property()
    Base.metadata.bind = engine

def recreate_tables():
    #Load all tables that are currently in the database
    Base.metadata.reflect()

    Base.metadata.drop_all()
    Base.metadata.create_all()

@commit_on_success
def empty_database():
    for table in reversed(Base.metadata.sorted_tables):
        session.execute(table.delete())

