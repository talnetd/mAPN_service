import sqlalchemy as sa
from mAPN_service.models import Base


class RadUserGroup(Base):

    __versioned__ = {}
    __tablename__ = "radusergroup"

    username = sa.Column(sa.String(64), primary_key=True, nullable=False, default="")
    groupname = sa.Column(sa.String(64), nullable=False, default="")
    priority = sa.Column(sa.Integer, nullable=False, default="1")

    def __init__(
        self, username=None, groupname=None, priority=None,
    ):
        self.username = username
        self.groupname = groupname
        self.priority = priority

    def __repr__(self):
        k_v = ", ".join([f"{k}={v}" for k, v in self.__dict__.items()])
        return f"<{self.__tablename__} {k_v}>"
