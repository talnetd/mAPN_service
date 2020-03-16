import sqlalchemy as sa
from mAPN_service.models import Base


class Partner_Locations(Base):

    __versioned__ = {}
    __tablename__ = 'partner_locations'

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(16))

    def __init__(self,
            id=None,
            name=None):
        self.id = id
        self.name = name

    def __repr__(self):
        k_v = ', '.join([f'{k}={v}' for k, v in self.__dict__.items()])
        return f'<{self.__tablename__} {k_v}>'