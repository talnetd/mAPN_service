import sqlalchemy as sa
from mAPN_service.models import Base


class RadUserGroup(Base):

    __versioned__ = {}
    __tablename__ = "radusergroup"

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    username = sa.Column(sa.String(64), nullable=False, default="")
    groupname = sa.Column(sa.String(64), nullable=False, default="")
    priority = sa.Column(sa.Integer, nullable=False, default="1")

    def __init__(
        self, id=None, username=None, groupname=None, priority=None,
    ):
        self.id = id
        self.username = username
        self.groupname = groupname
        self.priority = priority

    def __repr__(self):
        k_v = ", ".join([f"{k}={v}" for k, v in self.__dict__.items()])
        return f"<{self.__tablename__} {k_v}>"
