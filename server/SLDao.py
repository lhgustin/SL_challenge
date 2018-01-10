from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import sessionmaker

from SLConfig import db_url
import SLModels  # import all then use filename to load specific object


class SLDao:
        def __init__(self):
                self.engine = create_engine(URL(**db_url))
                self.session_maker = sessionmaker()
                self.session_maker.configure(bind=self.engine)
                self.session = self.session_maker()

        # close db connection properly accross new dao instances
        def close(self):
                self.session.close()
                self.engine.dispose()

        def add_agency(self, name, description, grade, tags):
                agency = SLModels.Agency(name=name, description=description, grade=grade, tags=tags)
                self.session.add(agency)
                self.session.commit()
                return agency

        def find_all_agencies(self):
                return self.session.query(SLModels.Agency).all()
