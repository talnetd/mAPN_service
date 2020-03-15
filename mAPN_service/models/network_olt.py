import sqlalchemy as sa
from mAPN_service.models import Base


class Network_Olt(Base):

    __versioned__ = {}
    __tablename__ = 'network_olt'

    id = sa.Column(sa.Integer, primary_key=True)
    vendor = sa.Column(sa.String(255))
    model = sa.Column(sa.String(32))
    create_time = sa.Column(sa.String(45))
    network_oltcol = sa.Column(sa.String(45))
    ip_address = sa.Column(sa.String(45))
    ssh_port = sa.Column(sa.String(45))
    ssh_user = sa.Column(sa.String(45))
    ssh_password = sa.Column(sa.String(45))
    uplink_board = sa.Column(sa.String(45))
    uplink_interface = sa.Column(sa.String(45))
    network_oltcol1 = sa.Column(sa.String(45))
    network_router_id = sa.Column(sa.Integer())
    network_router_partner_location_id = sa.Column(sa.Integer())

    def __init__(self,
            id=None,
            vendor=None,
            model=None,
            create_time=None,
            network_oltcol=None,
            ip_address=None,
            ssh_port=None,
            ssh_user=None,
            ssh_password=None,
            uplink_board=None,
            uplink_interface=None,
            network_oltcol1=None,
            network_router_id=None,
            network_router_partner_location_id=None):
        self.id = id
        self.vendor = vendor
        self.model = model
        self.create_time = create_time
        self.network_oltcol = network_oltcol
        self.ip_address = ip_address
        self.ssh_port = ssh_port
        self.ssh_user = ssh_user
        self.ssh_password = ssh_password
        self.uplink_board = uplink_board
        self.uplink_interface = uplink_interface
        self.network_oltcol1 = network_oltcol1
        self.network_router_id = network_router_id
        self.network_router_partner_location_id = network_router_partner_location_id

    def __repr__(self):
        k_v = ', '.join([f'{k}={v}' for k, v in self.__dict__.items()])
        return f'<{self.__tablename__} {k_v}>'