import sqlalchemy as sa
from mAPN_service.models import Base


class Customer(Base):

    __versioned__ = {}
    __tablename__ = 'customer'

    id = sa.Column(sa.Integer, primary_key=True)
    username = sa.Column(sa.String(16))
    email = sa.Column(sa.String(255))
    password = sa.Column(sa.String(32))
    full_name = sa.Column(sa.String(45))
    phone = sa.Column(sa.String(45))
    date_of_birth = sa.Column(sa.String(45))
    active_status = sa.Column(sa.String(45))
    type_of_billing = sa.Column(sa.String(45))
    customer_category = sa.Column(sa.String(45))
    customer_location = sa.Column(sa.String(45))
    date_added = sa.Column(sa.String(45))
    geo_data = sa.Column(sa.String(45))
    gpon_ont = sa.Column(sa.String(45))
    partner_isp_id = sa.Column(sa.String(45))
    splitter_port_no = sa.Column(sa.String(45))

    def __init__(self,
                 id=None,
                 username=None,
                 email=None,
                 password=None,
                 full_name=None,
                 phone=None,
                 date_of_birth=None,
                 active_status=None,
                 type_of_billing=None,
                 customer_category=None,
                 customer_location=None,
                 date_added=None,
                 geo_data=None,
                 gpon_ont=None,
                 partner_isp_id=None,
                 splitter_port_no=None):
        self.id = id
        self.username = username
        self.email = email
        self.password = password
        self.full_name = full_name
        self.phone = phone
        self.date_of_birth = date_of_birth
        self.active_status = active_status
        self.type_of_billing = type_of_billing
        self.customer_category = customer_category
        self.customer_location = customer_location
        self.date_added = date_added
        self.geo_data = geo_data
        self.gpon_ont = gpon_ont
        self.partner_isp_id = partner_isp_id
        self.splitter_port_no = splitter_port_no

    def __repr__(self):
        k_v = ', '.join([f'{k}={v}' for k, v in self.__dict__.items()])
        return f'<{self.__tablename__} {k_v}>'
