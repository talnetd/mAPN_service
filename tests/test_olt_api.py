import random
import pytest
from datetime import datetime


@pytest.mark.usefixtures("client")
def test_olt_index(client):
    resp = client.get('/olts/')
    assert resp.status_code == 200 and isinstance(resp.get_json(), list)


@pytest.mark.usefixtures("client")
def test_olt_create(client):
    data = dict(
        network_router_partner_location_id=1,
        network_router_id=1,
        uplink_interface='eth0',
        uplink_board=1,
        ssh_password='testing',
        ssh_user='root',
        ssh_port=22,
        ip_address='192.168.1.1',
        create_time=datetime.now().isoformat(),
        model='Model #1',
        vendor='Vendor #1',
    )
    resp = client.post('/olts/', json=data)
    assert 200 == resp.status_code and resp.data.isdigit()


@pytest.mark.usefixtures("client")
def test_olt_get_one(client):
    olt_id = 1
    resp = client.get(f'/olts/{olt_id}')
    assert 200 == resp.status_code and isinstance(resp.get_json(), dict)
