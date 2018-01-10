import json

from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy.ext.declarative import declarative_base
from SLDao import *
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
                return json.dumps(self.get_dict())

        def get_dict(self):
                return dict((col, getattr(self, col)) for col in self.__table__.columns.keys())


def re_populate_model():
        engine = create_engine(URL(**db_url))

        # create tables
        Base.metadata.drop_all(bind=engine)
        Base.metadata.create_all(bind=engine)

        for _t in Base.metadata.tables:
                print "re_populate_model, Table: ", _t

        # populate tables
        dao = SLDao()
        description = 'Havas Worldwide, formerly known as Euro RSCG, is an American advertising agency. ' \
                      'It is one of the largest integrated marketing communications agencies in the world, ' \
                      'made up of 316 offices located in 75 countries.[2][3] ' \
                      'The firm provides advertising, marketing, and corporate communications services.' \
                      'In 2010, Advertising Age listed the firm, (then called Euro RSCG), ' \
                      'as having more global assignments than any other network for the fifth consecutive year, ' \
                      'making the agency the worlds largest network by global accounts.[4] ' \
                      'Headquartered in New York, Havas Worldwide is the largest unit of Havas ' \
                      '(Euronext Paris SA: HAV.PA), the fifth largest communications group in the world, ' \
                      'behind Omnicom, WPP, Interpublic, and Publicis.'

        dao.add_agency('Havas worldwide', description, GRADE_MASTER, 'Full Integrated, Advertising')

        description = 'Huge is a digital agency providing strategy, marketing, design, ' \
                      'and technology services to Fortune 100 companies. ' \
                      'The company was founded in 1999 and was named the ' \
                      'fastest-growing marketing agency in 2009 by Advertising Age. ' \
                      'Huge has offices in Brooklyn, Los Angeles, Portland, Washington, D.C., ' \
                      'Sao Paulo, Rio de Janeiro, Atlanta, Toronto, Bogota, Medellin, Singapore, ' \
                      'Oakland, London, and Detroit.[1] Since 2008, ' \
                      'Huge has been a member the Interpublic Group of Companies.[2][3]'
        dao.add_agency('Huge New York', description, GRADE_MASTER, 'Digital Advertising, User Experience')

        description = 'Grey Group is a global advertising and marketing agency with headquarters ' \
                      'in New York City, and 432 offices in 96 countries, operating in 154 cities[1]' \
                      ' - organized into four geographical units: North America; Europe, Middle East and Africa,' \
                      ' Asia-Pacific and Latin America.[2]As a unit of communications conglomerate WPP Group,' \
                      ' Grey Global Group operates branded independent business units in many communications disciplines' \
                      ' including: advertising, direct marketing, public relations, public affairs, brand development,' \
                      ' customer relationship management, sales promotion, interactive marketing' \
                      ' - through its subsidiaries: Grey, G2, GHG, GCI Group, MediaCom Worldwide,' \
                      ' Alliance, G WHIZ, and WING.Grey Groups international clients include:' \
                      'Procter & Gamble, GlaxoSmithKline, Nokia, BritishAmerican Tobacco, Diageo, ' \
                      'Volkswagen, Novartis, Wyeth, Canon, DirecTV, and 3M.[3] The company has won:' \
                      '10 Cannes Lions; beside the Addy, Clio and one Emmy Award.[3]' \
                      'Grey Groups European network, Grey EMEA, won 26 Euro EFFIE awards, ' \
                      ' and is the five - time Euro EFFIE Agency Network of the Year, ' \
                      ' in four consecutive years of 2005-2008[4] and again in 2012[5]'
        dao.add_agency('Grey Group', description, GRADE_JEDI, 'Brand activation, Public Relation')

        description = 'Mindshare is a global media and marketing services company created in 1997. ' \
                      'The company was created by the merger of the media operations of JWT and Ogilvy & Mather, ' \
                      'then the two big full service advertising agencies within WPP Group. ' \
                      'The launch team comprised Mandy Pooler and Nick Emery from O&M ' \
                      'and Ron De Pear and James Walker from JWT. Initially the business ' \
                      'faced strong opposition to the merger from the agency parent GroupM in the US region. ' \
                      'The Mindshare global network consists of approximately 6,000 employees across 115 offices ' \
                      'in 82 countries throughout North America, Latin America, Europe, the Middle East, ' \
                      'Africa and Asia Pacific.[1][2] Mindshare USA LLC has 11 offices across the U.S. ' \
                      'and Canada with billings of $9.96 billion (according to the media agency monitoring body, RECMA). ' \
                      'Phil Cowdell has served as head of North American operations since 2009.[3] ' \
                      'Mindshare Nederland was created in 1999 by Ton Schoonderbeek, ' \
                      'now regional leader and chief executive for the companys Benelux region (including Scandinavia).[4] ' \
                      'In November 2017, Mindshare appointed Sudipto Roy as managing director, ' \
                      'team Unilever for Asia Pacific, Africa, Middle East, Turkey and Russia (AAR). [5]'
        dao.add_agency('Mindshare', description, GRADE_PADAWAN, 'Media Planning, Advertising')

        # agencies = dao.find_all_agencies()
        # print 'agencies found after creation (=4)', len(agencies)
        # print 'agencies json : ', agencies
        # dao.session.close()
        # return dao
        dao.close()


if __name__ == "__main__":
        re_populate_model()
