import sqlalchemy as sa
from datetime import datetime
from mAPN_service.models import Base


class Location(Base):

    __versioned__ = {}
    __tablename__ = "location"

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(16))
    created_at = sa.Column(sa.DateTime, default=datetime.now)
    updated_at = sa.Column(sa.DateTime, onupdate=datetime.now)
    deleted_at = sa.Column(sa.DateTime)

    def __init__(self, id=None, name=None):
        self.id = id
        self.name = name

    def __repr__(self):
        k_v = ", ".join([f"{k}={v}" for k, v in self.__dict__.items()])
        return f"<{self.__tablename__} {k_v}>"
