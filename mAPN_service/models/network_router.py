from datetime import datetime
import sqlalchemy as sa
from mAPN_service.models import Base


class Network_Router(Base):

    __versioned__ = {}
    __tablename__ = "network_router"

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(16))
    nas_type = sa.Column(sa.String(45))
    vendor_model = sa.Column(sa.String(45))
    physical_address = sa.Column(sa.String(45))
    host_address = sa.Column(sa.String(45))
    nas_address = sa.Column(sa.String(45))
    authorization_accounting_type = sa.Column(sa.String(45))
    radius_secret = sa.Column(sa.String(45))
    enable_api = sa.Column(sa.String(45))
    login = sa.Column(sa.String(45))
    username = sa.Column(sa.String(45))
    partner_locations_id = sa.Column(sa.Integer)
    created_at = sa.Column(sa.DateTime, default=datetime.now)
    updated_at = sa.Column(sa.DateTime, onupdate=datetime.now)
    deleted_at = sa.Column(sa.DateTime)

    def __init__(
        self,
        id=None,
        name=None,
        nas_type=None,
        vendor_model=None,
        physical_address=None,
        host_address=None,
        nas_address=None,
        authorization_accounting_type=None,
        radius_secret=None,
        enable_api=None,
        login=None,
        username=None,
        partner_locations_id=None,
    ):

        self.id = id
        self.name = name
        self.nas_type = nas_type
        self.vendor_model = vendor_model
        self.physical_address = physical_address
        self.host_address = host_address
        self.nas_address = nas_address
        self.authorization_accounting_type = authorization_accounting_type
        self.radius_secret = radius_secret
        self.enable_api = enable_api
        self.login = login
        self.username = username
        self.partner_locations_id = partner_locations_id

    def __repr__(self):
        k_v = ", ".join([f"{k}={v}" for k, v in self.__dict__.items()])
        return f"<{self.__tablename__} {k_v}>"
