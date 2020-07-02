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
from mAPN_service.models.radius.nas import NAS
from mAPN_service.models.radius.radacct import RadAcct
from mAPN_service.models.radius.radcheck import RadCheck
from mAPN_service.models.radius.radgroupcheck import RadGroupCheck
from mAPN_service.models.radius.radgroupreply import RadGroupReply
from mAPN_service.models.radius.radreply import RadReply
from mAPN_service.models.radius.radusergroup import RadUserGroup


GLOBAL_MYSQL_DB_ENCODING = "utf8mb4"
MYSQL_APP_DB_HOST = os.environ.get("MYSQL_APP_DB_HOST") or os.environ.get(
    "DB_HOST", "localhost"
)
MYSQL_APP_DB_PORT = int(
    os.environ.get("MYSQL_APP_DB_PORT") or os.environ.get("DB_PORT", 3306)
)
MYSQL_APP_DB_USER = os.environ.get("MYSQL_APP_DB_USER") or os.environ.get("DB_USER")
MYSQL_APP_DB_PASSWORD = os.environ.get("MYSQL_APP_DB_PASSWORD") or os.environ.get(
    "DB_PASSWORD"
)
MYSQL_APP_DB_NAME = os.environ.get("MYSQL_APP_DB_NAME") or os.environ.get("DB_NAME")
MYSQL_APP_DB_ENCODING = (
    os.environ.get("MYSQL_APP_DB_ENCODING") or GLOBAL_MYSQL_DB_ENCODING
)
MYSQL_APP_DB_URI = (
    f"mysql+pymysql://{MYSQL_APP_DB_USER}:{MYSQL_APP_DB_PASSWORD}@{MYSQL_APP_DB_HOST}:"
    f"{MYSQL_APP_DB_PORT}/{MYSQL_APP_DB_NAME}"
)
APP_API_KEY = os.environ.get("API_KEY") or os.environ.get("APP_API_KEY")


MYSQL_RADIUS_DB_HOST = os.environ.get("MYSQL_RADIUS_DB_HOST", "localhost")
MYSQL_RADIUS_DB_PORT = int(os.environ.get("MYSQL_RADIUS_DB_PORT", 3306))
MYSQL_RADIUS_DB_USER = os.environ.get("MYSQL_RADIUS_DB_USER", "root")
MYSQL_RADIUS_DB_PASSWORD = os.environ.get("MYSQL_RADIUS_DB_PASSWORD", "toor")
MYSQL_RADIUS_DB_NAME = os.environ.get("MYSQL_RADIUS_DB_NAME", "test")
MYSQL_RADIUS_DB_ENCODING = (
    os.environ.get("MYSQL_RADIUS_DB_ENCODING") or GLOBAL_MYSQL_DB_ENCODING
)

MYSQL_RADIUS_DB_URI = (
    f"mysql+pymysql://{MYSQL_RADIUS_DB_USER}:{MYSQL_RADIUS_DB_PASSWORD}@{MYSQL_RADIUS_DB_HOST}:"
    f"{MYSQL_RADIUS_DB_PORT}/{MYSQL_RADIUS_DB_NAME}"
)


if str(os.environ.get("TESTING")).lower() == "true":
    MYSQL_APP_DB_URI = "sqlite://"


make_versioned(user_cls=None)
engine = create_engine(MYSQL_APP_DB_URI)
radius_engine = create_engine(MYSQL_RADIUS_DB_URI)

tables = [
    Boards.__table__,
    Customer.__table__,
    Location.__table__,
    Network_Olt.__table__,
    Network_Router.__table__,
    Partner.__table__,
    InternetTrafficPlan.__table__,
    VoipTrafficPlan.__table__,
    CustomTrafficPlan.__table__,
]
Base.metadata.create_all(engine, tables=tables)
Session = sessionmaker(bind=engine)


radius_tables = [
    NAS.__table__,
    RadAcct.__table__,
    RadCheck.__table__,
    RadGroupCheck.__table__,
    RadGroupReply.__table__,
    RadReply.__table__,
    RadUserGroup.__table__,
]
Base.metadata.create_all(radius_engine, tables=radius_tables)
Radius_Session = sessionmaker(bind=radius_engine)


sqlalchemy.orm.configure_mappers()


@contextmanager
def session_scope(for_db="app"):
    """
    Create a new Database Session (using SQLAlchemy) which is generated from sessionmaker factory.
    NOTE: This depends on SQLAlchemy models.

    Usage:

    ```python
    # import required modules and sqlalchemy models
    # importing model
    from mAPN_service.models.testing_table import TestingTable
    # importing session_scope function from config module
    from mAPN_service.config import session_scope

    # creating a new record
    with session_scope() as session:
        record = TestingTable(**my_data)
        session.add(record)
        session.flush()
        session.refresh(record)
        inserted_id = record.id

    # select existing record (single)
    record_id = 100
    with session_scope() as session:
        found_record = session.query(TestingTable).filter_by(id=record_id).first()

    # WARNING: NOT RECOMMENDED. PLEASE USE BATCH QUERY (BY CHUNK/PAGINATION)
    # select all records
    with session_scope() as session:
        records = session.query(TestingTable).all()
    ```

    # select records by batch (Not supported right now!)
    N/A

    Arguments:
        for_db {str} -- Select db connection string.
                        (Default: "app", Possible values: "app", "radius")

    Yield:
        {Session} A Session object.
    """
    session = None
    if for_db == "radius":
        session = Radius_Session()
    else:
        session = Session()

    try:
        yield session
        session.commit()
    except:  # noqa
        session.rollback()
        raise
    finally:
        session.close()
