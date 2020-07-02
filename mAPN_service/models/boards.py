import sqlalchemy as sa
from datetime import datetime
from mAPN_service.models import Base


class Boards(Base):

    __versioned__ = {}
    __tablename__ = "board"

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(255), nullable=False)
    port_count = sa.Column(sa.Integer)
    created_at = sa.Column(sa.DateTime, default=datetime.now)
    updated_at = sa.Column(sa.DateTime, onupdate=datetime.now)
    deleted_at = sa.Column(sa.DateTime)

    def __init__(self, id=None, name=None, port_count=None):

        self.id = id
        self.name = name
        self.port_count = port_count

    def __repr__(self):
        k_v = ", ".join([f"{k}={v}" for k, v in self.__dict__.items()])
        return f"<{self.__tablename__} {k_v}>"
