import sqlalchemy as sa
from mAPN_service.models import Base


class RadAcct(Base):

    __versioned__ = {}
    __tablename__ = "radacct"

    radacctid = sa.Column(sa.BigInteger, autoincrement=True, primary_key=True)
    acctsessionid = sa.Column(sa.String(64), nullable=False, default="")
    acctuniqueid = sa.Column(sa.String(32), nullable=False, default="")
    username = sa.Column(sa.String(64), nullable=False, default="")
    groupname = sa.Column(sa.String(64), nullable=False, default="")
    realm = sa.Column(sa.String(64), default="")
    nasipaddress = sa.Column(sa.String(15), nullable=False, default="")
    nasportid = sa.Column(sa.String(15))
    nasporttype = sa.Column(sa.String(32))
    acctstarttime = sa.Column(sa.DateTime)
    acctstoptime = sa.Column(sa.DateTime)
    acctsessiontime = sa.Column(sa.Integer)
    acctauthentic = sa.Column(sa.String(32))
    connectinfo_start = sa.Column(sa.String(50))
    connectinfo_stop = sa.Column(sa.String(50))
    acctinputoctets = sa.Column(sa.BigInteger)
    acctoutputoctets = sa.Column(sa.BigInteger)
    calledstationid = sa.Column(sa.String(50), nullable=False, default="")
    callingstationid = sa.Column(sa.String(50), nullable=False, default="")
    acctterminatecause = sa.Column(sa.String(32), nullable=False, default="")
    servicetype = sa.Column(sa.String(32))
    framedprotocol = sa.Column(sa.String(32))
    framedipaddress = sa.Column(sa.String(15))
    acctstartdelay = sa.Column(sa.Integer)
    acctstopdelay = sa.Column(sa.Integer)
    xascendsessionsvrkey = sa.Column(sa.String(10))

    def __init__(
        self,
        radacctid=None,
        acctsessionid=None,
        acctuniqueid=None,
        username=None,
        groupname=None,
        realm=None,
        nasipaddress=None,
        nasportid=None,
        nasporttype=None,
        acctstarttime=None,
        acctstoptime=None,
        acctsessiontime=None,
        acctauthentic=None,
        connectinfo_start=None,
        connectinfo_stop=None,
        acctinputoctets=None,
        acctoutputoctets=None,
        calledstationid=None,
        callingstationid=None,
        acctterminatecause=None,
        servicetype=None,
        framedprotocol=None,
        framedipaddress=None,
        acctstartdelay=None,
        acctstopdelay=None,
        xascendsessionsvrkey=None,
    ):
        self.radacctid = radacctid
        self.acctsessionid = acctsessionid
        self.acctuniqueid = acctuniqueid
        self.username = username
        self.groupname = groupname
        self.realm = realm
        self.nasipaddress = nasipaddress
        self.nasportid = nasportid
        self.nasporttype = nasporttype
        self.acctstarttime = acctstarttime
        self.acctstoptime = acctstoptime
        self.acctsessiontime = acctsessiontime
        self.acctauthentic = acctauthentic
        self.connectinfo_start = connectinfo_start
        self.connectinfo_stop = connectinfo_stop
        self.acctinputoctets = acctinputoctets
        self.acctoutputoctets = acctoutputoctets
        self.calledstationid = calledstationid
        self.callingstationid = callingstationid
        self.acctterminatecause = acctterminatecause
        self.servicetype = servicetype
        self.framedprotocol = framedprotocol
        self.framedipaddress = framedipaddress
        self.acctstartdelay = acctstartdelay
        self.acctstopdelay = acctstopdelay
        self.xascendsessionsvrkey = xascendsessionsvrkey

    def __repr__(self):
        k_v = ", ".join([f"{k}={v}" for k, v in self.__dict__.items()])
        return f"<{self.__tablename__} {k_v}>"
