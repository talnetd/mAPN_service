import sqlalchemy as sa
from datetime import datetime
from sqlalchemy.schema import FetchedValue
from mAPN_service.models import Base


class Service_Plan(Base):

    __versioned__ = {}
    __tablename__ = 'service_plan'

    id = sa.Column(sa.Integer, primary_key=True)
    plan_name = sa.Column(sa.String(16), nullable=False)
    desc = sa.Column(sa.String(255)),
    pricing = sa.Column(sa.String(32), nullable=False)
    pay_method = sa.Column(sa.String(32))
    end_date = sa.Column(sa.DateTime, default=datetime.utcnow())
    discount = sa.Column(sa.String(45))
    customer_id = sa.Column(sa.Integer)

    def __init__(self,
            id=None,
            plan_name=None,
            desc=None,
            pricing=None,
            pay_method=None,
            end_date=None,
            discount=None,
            customer_id=None):
        self.id = id
        self.plan_name = plan_name
        self.desc = desc
        self.pricing = pricing
        self.pay_method = pay_method
        self.end_date = end_date
        self.discount = discount
        self.customer_id = customer_id

    def __repr__(self):
        k_v = ', '.join([f'{k}={v}' for k, v in self.__dict__.items()])
        return f'<{self.__tablename__} {k_v}>'