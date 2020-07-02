import sqlalchemy as sa
from mAPN_service.models import Base


class NAS(Base):

    __versioned__ = {}
    __tablename__ = "nas"

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    nasname = sa.Column(sa.String(128), nullable=False)
    shortname = sa.Column(sa.String(32), default=None)
    type = sa.Column(sa.String(30), default="other")
    ports = sa.Column(sa.Integer, default=None)
    secret = sa.Column(sa.String(60), default="secret")
    server = sa.Column(sa.String(64), default=None)
    community = sa.Column(sa.String(50), default=None)
    description = sa.Column(sa.String(200), default="RADIUS Client")

    def __init__(
        self,
        id=None,
        nasname=None,
        shortname=None,
        type=None,
        ports=None,
        secret=None,
        server=None,
        community=None,
        description=None,
    ):
        self.id = id
        self.nasname = nasname
        self.shortname = shortname
        self.type = type
        self.ports = ports
        self.secret = secret
        self.server = server
        self.community = community
        self.description = description

    def __repr__(self):
        k_v = ", ".join([f"{k}={v}" for k, v in self.__dict__.items()])
        return f"<{self.__tablename__} {k_v}>"
