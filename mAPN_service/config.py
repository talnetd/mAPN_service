import os
import sqlalchemy
from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_continuum import make_versioned
from mAPN_service.models import Base
from mAPN_service.models.boards import Boards
from mAPN_service.models.customer import Customer
from mAPN_service.models.location import Location
from mAPN_service.models.network_olt import Network_Olt
from mAPN_service.models.network_router import Network_Router
from mAPN_service.models.partner import Partner
from mAPN_service.models.internet_traffic_plan import InternetTrafficPlan
from mAPN_service.models.voip_traffic_plan import VoipTrafficPlan
from mAPN_service.models.custom_traffic_plan import CustomTrafficPlan


DB_HOST = os.environ.get('DB_HOST', 'localhost')
DB_PORT = os.environ.get('DB_PORT', 3306)
DB_USER = os.environ.get('DB_USER')
DB_PASSWORD = os.environ.get('DB_PASSWORD')
DB_NAME = os.environ.get('DB_NAME')
DB_URI = f'mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
API_KEY = os.environ.get('API_KEY')


if str(os.environ.get('TESTING')).lower() == 'true':
    DB_URI = 'sqlite://'


make_versioned(user_cls=None)
engine = create_engine(DB_URI)
tables = [
    Boards.__table__,
    Customer.__table__,
    Location.__table__,
    Network_Olt.__table__,
    Network_Router.__table__,
    Partner.__table__,
    InternetTrafficPlan.__table__,
    VoipTrafficPlan.__table__,
    CustomTrafficPlan.__table__
]
Base.metadata.create_all(engine, tables=tables)
Session = sessionmaker(bind=engine)


sqlalchemy.orm.configure_mappers()


@contextmanager
def session_scope():
    session = Session()

    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()
