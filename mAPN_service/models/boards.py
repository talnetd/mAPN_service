import sqlalchemy as sa
from datetime import datetime
from sqlalchemy.schema import FetchedValue
from mAPN_service.models import Base


class Boards(Base):

    __versioned__ = {}
    __tablename__ = 'boards'

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(255), nullable=False)
    port_count = sa.Column(sa.Integer)

    def __init__(self,
        id=None,
        name=None,
        port_count=None):

        self.id = id
        self.name = name
        self.port_count = port_count

    def __repr__(self):
        k_v = ', '.join([f'{k}={v}' for k, v in self.__dict__.items()])
        return f'<{self.__tablename__} {k_v}>'
