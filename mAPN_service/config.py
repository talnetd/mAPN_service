import os
import sqlalchemy
from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_continuum import make_versioned
from mAPN_service.models import Base
from mAPN_service.models.customer import Customer
from mAPN_service.models.network_olt import Network_Olt
from mAPN_service.models.network_router import Network_Router
from mAPN_service.models.partner_locations import Partner_Locations
from mAPN_service.models.service_plan import Service_Plan
from mAPN_service.models.traffic_plan import Traffic_Plan


DB_HOST = os.environ.get('DB_HOST', 'localhost')
DB_PORT = os.environ.get('DB_PORT', 3306)
DB_USER = os.environ.get('DB_USER')
DB_PASSWORD = os.environ.get('DB_PASSWORD')
DB_NAME = os.environ.get('DB_NAME')
DB_URI = f'mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'


make_versioned(user_cls=None)
engine = create_engine(DB_URI)
Base.metadata.create_all(engine, tables=[
    Customer.__table__,
    Network_Olt.__table__,
    Network_Router.__table__,
    Partner_Locations.__table__,
    Service_Plan.__table__,
    Traffic_Plan.__table__
])
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
