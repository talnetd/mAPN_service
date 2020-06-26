import random

import pytest


@pytest.mark.usefixtures("client")
def test_vtp_index(client):
    resp = client.get("/voip_traffic_plan/")
    assert resp.status_code == 200 and isinstance(resp.get_json(), list)


@pytest.mark.usefixtures("client")
def test_vtp_create(client):
    data = dict(
        title="VTP #1", service_name="Service #1", price=random.randrange(1000, 2000)
    )
    resp = client.post("/voip_traffic_plan/", json=data)
    assert 200 == resp.status_code and resp.data.isdigit()


@pytest.mark.usefixtures("client")
def test_vtp_get_one(client):
    plan_id = 1
    resp = client.get(f"/voip_traffic_plan/{plan_id}")
    assert 200 == resp.status_code and isinstance(resp.get_json(), dict)


@pytest.mark.usefixtures("client")
def test_vtp_update_one(client):
    plan_id = 1
    data = dict(
        title="VTP #1", service_name="Service #1", price=random.randrange(1000, 2000)
    )
    resp = client.put(f"/voip_traffic_plan/{plan_id}", json=data)
    assert 204 == resp.status_code
