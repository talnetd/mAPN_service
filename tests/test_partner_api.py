import random
import pytest


@pytest.mark.usefixtures("client")
def test_partner_index(client):
    resp = client.get('/partners/')
    assert resp.status_code == 200 and isinstance(resp.get_json(), list)


@pytest.mark.usefixtures("client")
def test_partner_create(client):
    data = dict(
        name='Partner #1'
    )
    resp = client.post('/partners/', json=data)
    assert 200 == resp.status_code and resp.data.isdigit()


@pytest.mark.usefixtures("client")
def test_board_get_one(client):
    board_id = 1
    resp = client.get(f'/partners/{board_id}')
    assert 200 == resp.status_code and isinstance(resp.get_json(), dict)
