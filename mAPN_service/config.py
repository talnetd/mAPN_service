import os
import sqlalchemy
from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_continuum import make_versioned
from mAPN_service.models import Base
from mAPN_service.models.radius.nas import NAS
from mAPN_service.models.radius.radacct import RadAcct
from mAPN_service.models.radius.radcheck import RadCheck
from mAPN_service.models.radius.radgroupcheck import RadGroupCheck
from mAPN_service.models.radius.radgroupreply import RadGroupReply
from mAPN_service.models.radius.radreply import RadReply
from mAPN_service.models.radius.radusergroup import RadUserGroup


GLOBAL_MYSQL_DB_ENCODING = "utf8mb4"
APP_API_KEY = os.environ.get("API_KEY") or os.environ.get("APP_API_KEY")
MYSQL_RADIUS_DB_ENCODING = (
    os.environ.get("MYSQL_RADIUS_DB_ENCODING") or GLOBAL_MYSQL_DB_ENCODING
)

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
    MYSQL_RADIUS_DB_URI = "sqlite://"

make_versioned(user_cls=None)
radius_engine = create_engine(MYSQL_RADIUS_DB_URI)

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
        session = Radius_Session()

    # NOW ONLY RADIUS is import
    try:
        yield session
        session.commit()
    except:  # noqa
        session.rollback()
        raise
    finally:
        session.close()
