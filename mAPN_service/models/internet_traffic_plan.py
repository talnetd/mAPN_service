import sqlalchemy as sa
from datetime import datetime
from mAPN_service.models import Base


class InternetTrafficPlan(Base):

    __versioned__ = {}
    __tablename__ = "internet_traffic_plan"

    id = sa.Column(sa.Integer, primary_key=True)
    title = sa.Column(sa.String(191), nullable=False)
    service_name = sa.Column(sa.String(191))
    download_speed = sa.Column(sa.Integer, nullable=False)
    upload_speed = sa.Column(sa.Integer, nullable=False)
    price = sa.Column(sa.Float, nullable=False)
    created_at = sa.Column(sa.DateTime, default=datetime.now)
    updated_at = sa.Column(sa.DateTime, onupdate=datetime.now)
    deleted_at = sa.Column(sa.DateTime)

    def __init__(
        self,
        id=None,
        title=None,
        service_name=None,
        download_speed=None,
        upload_speed=None,
        price=None,
    ):
        self.id = id
        self.title = title
        self.service_name = service_name
        self.download_speed = download_speed
        self.upload_speed = upload_speed
        self.price = price

    def __repr__(self):
        k_v = ", ".join([f"{k}={v}" for k, v in self.__dict__.items()])
        return f"<{self.__tablename__} {k_v}>"
