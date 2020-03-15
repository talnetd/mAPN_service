import sqlalchemy as sa
from mAPN_service.models import Base


class Traffic_Plan(Base):

    __versioned__ = {}
    __tablename__ = 'traffic_plan'

    id = sa.Column(sa.Integer, primary_key=True)
    traffic_plan_name = sa.Column(sa.String(45))
    desc = sa.Column(sa.Text())
    traffic_plancol = sa.Column(sa.String(45))
    partner_location = sa.Column(sa.Integer())
    download_speed = sa.Column(sa.Integer())
    upload_speed = sa.Column(sa.Integer())
    guaranteed_speed_limit = sa.Column(sa.Integer())
    qos_priority = sa.Column(sa.String(45))
    aggregation = sa.Column(sa.Integer())
    burst_limit = sa.Column(sa.Integer())
    burst_threshold = sa.Column(sa.Integer())
    burst_time = sa.Column(sa.String(45))
    service_plan_id = sa.Column(sa.Integer())
    service_plan_customer_id = sa.Column(sa.Integer())

    def __init__(self,
            id=None,
            traffic_plan_name=None,
            desc=None,
            traffic_plancol=None,
            partner_location=None,
            download_speed=None,
            upload_speed=None,
            guaranteed_speed_limit=None,
            qos_priority=None,
            aggregation=None,
            burst_limit=None,
            burst_threshold=None,
            burst_time=None,
            service_plan_id=None,
            service_plan_customer_id=None):
        self.id = id
        self.traffic_plan_name = traffic_plan_name
        self.desc = desc
        self.traffic_plancol = traffic_plancol
        self.partner_location = partner_location
        self.download_speed = download_speed
        self.upload_speed = upload_speed
        self.guaranteed_speed_limit = guaranteed_speed_limit
        self.qos_priority = qos_priority
        self.aggregation = aggregation
        self.burst_limit = burst_limit
        self.burst_threshold = burst_threshold
        self.burst_time = burst_time
        self.service_plan_id = service_plan_id
        self.service_plan_customer_id = service_plan_customer_id

    def __repr__(self):
        k_v = ', '.join([f'{k}={v}' for k, v in self.__dict__.items()])
        return f'<{self.__tablename__} {k_v}>'
