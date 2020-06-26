import random
import pytest


@pytest.mark.usefixtures("client")
def test_router_index(client):
    resp = client.get("/routers/")
    assert resp.status_code == 200 and isinstance(resp.get_json(), list)


@pytest.mark.usefixtures("client")
def test_router_create(client):
    data = dict(
        partner_locations_id=1,
        username="root",
        login="root",
        enable_api=True,
        radius_secret="testpwd",
        authorization_accounting_type="",
        nas_address="192.168.200.1",
        host_address="192.168.100.1",
        physical_address="aa:bb:cc:dd:ee:01",
        vendor_model="Vendor Model #1",
        nas_type="",
        name="Room #1",
    )
    resp = client.post("/routers/", json=data)
    assert 200 == resp.status_code and resp.data.isdigit()


@pytest.mark.usefixtures("client")
def test_router_get_one(client):
    router_id = 1
    resp = client.get(f"/boards/{router_id}")
    assert 200 == resp.status_code and isinstance(resp.get_json(), dict)
