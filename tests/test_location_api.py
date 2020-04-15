import random
import pytest


@pytest.mark.usefixtures("client")
def test_location_index(client):
    resp = client.get('/locations/')
    assert resp.status_code == 200 and isinstance(resp.get_json(), list)


@pytest.mark.usefixtures("client")
def test_location_create(client):
    data = dict()
    resp = client.post('/locations/', json=data)
    assert 200 == resp.status_code and resp.data.isdigit()


@pytest.mark.usefixtures("client")
def test_location_get_one(client):
    location_id = 1
    resp = client.get(f'/locations/{location_id}')
    assert 200 == resp.status_code and isinstance(resp.get_json(), dict)
