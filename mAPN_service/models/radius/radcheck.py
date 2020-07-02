import sqlalchemy as sa
from mAPN_service.models import Base


class RadCheck(Base):

    __versioned__ = {}
    __tablename__ = "radcheck"

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    username = sa.Column(sa.String(64), nullable=False, default="")
    attribute = sa.Column(sa.String(64), nullable=False, default="")
    op = sa.Column(sa.CHAR(2), nullable=False, default="==")
    value = sa.Column(sa.String(253), nullable=False, default="")

    def __init__(
        self, id=None, username=None, attribute=None, op=None, value=None,
    ):
        self.id = id
        self.username = username
        self.attribute = attribute
        self.op = op
        self.value = value

    def __repr__(self):
        k_v = ", ".join([f"{k}={v}" for k, v in self.__dict__.items()])
        return f"<{self.__tablename__} {k_v}>"
