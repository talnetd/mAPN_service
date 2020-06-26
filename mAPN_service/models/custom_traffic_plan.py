import sqlalchemy as sa
from datetime import datetime
from mAPN_service.models import Base


class CustomTrafficPlan(Base):

    __versioned__ = {}
    __tablename__ = "custom_traffic_plan"

    id = sa.Column(sa.Integer, primary_key=True)
    title = sa.Column(sa.String(191), nullable=False)
    service_name = sa.Column(sa.String(191))
    price = sa.Column(sa.Float, nullable=False)
    bandwidth = sa.Column(sa.Integer, nullable=False)
    created_at = sa.Column(sa.DateTime, default=datetime.now)
    updated_at = sa.Column(sa.DateTime, onupdate=datetime.now)
    deleted_at = sa.Column(sa.DateTime)

    def __init__(
        self, id=None, title=None, service_name=None, price=None, bandwidth=None
    ):
        self.id = id
        self.title = title
        self.service_name = service_name
        self.price = price
        self.bandwidth = bandwidth

    def __repr__(self):
        k_v = ", ".join([f"{k}={v}" for k, v in self.__dict__.items()])
        return f"<{self.__tablename__} {k_v}>"
