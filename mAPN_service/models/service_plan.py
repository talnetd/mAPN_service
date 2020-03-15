import sqlalchemy as sa
from mAPN_service.models import Base


class Service_Plan(Base):

    __versioned__ = {}
    __tablename__ = 'service_plan'

    id = sa.Column(sa.Integer, primary_key=True)

    def __init__(self,
            id=None):
        self.id = id

    def __repr__(self):
        k_v = ', '.join([f'{k}={v}' for k, v in self.__dict__.items()])
        return f'<{self.__tablename__} {k_v}>'