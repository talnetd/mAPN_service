import random

import pytest


@pytest.mark.usefixtures("client")
def test_ctp_index(client):
    resp = client.get('/internet_traffic_plan/')
    assert resp.status_code == 200 and isinstance(resp.get_json(), list)


@pytest.mark.usefixtures("client")
def test_ctp_create(client):
    data = dict(title='CTP #1',
                service_name='Service #1',
                price=random.randrange(1000, 2000),
                upload_speed=random.randrange(10, 100),
                download_speed=random.randrange(10, 100))
    resp = client.post('/internet_traffic_plan/', json=data)
    assert 200 == resp.status_code and resp.data.isdigit()


@pytest.mark.usefixtures("client")
def test_ctp_get_one(client):
    plan_id = 1
    resp = client.get(f"/internet_traffic_plan/{plan_id}")
    assert 200 == resp.status_code and isinstance(resp.get_json(), dict)
