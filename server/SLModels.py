import json

from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy.ext.declarative import declarative_base

from SLConfig import db_url

Base = declarative_base()

GRADE_PADAWAN = 0
GRADE_JEDI = 1
GRADE_MASTER = 2


class Agency(Base):
        __tablename__ = 'agency'
        id = Column(Integer, primary_key=True)
        name = Column(String)
        description = Column(String)
        tags = Column(String)
        grade = Column(Integer)

        def __repr__(self):
                return get_json_from_entity(self)


def get_json_from_entity(entity):
        return json.dumps(dict((col, getattr(entity, col)) for col in entity.__table__.columns.keys()))


if __name__ == "__main__":
        engine = create_engine(URL(**db_url))

        # create tables
        Base.metadata.drop_all(bind=engine)
        Base.metadata.create_all(bind=engine)

        for _t in Base.metadata.tables:
                print "Table: ", _t
