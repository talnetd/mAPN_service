from tests.fixture import client
from mAPN_service.config import Base, tables, engine


Base.metadata.drop_all(bind=engine, tables=tables)
Base.metadata.create_all(bind=engine, tables=tables)