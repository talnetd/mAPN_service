import random
import pytest


@pytest.mark.usefixtures("client")
def test_board_index(client):
    resp = client.get('/boards/')
    assert resp.status_code == 200 and isinstance(resp.get_json(), list)


@pytest.mark.usefixtures("client")
def test_board_create(client):
    data = dict(
        name='board #1',
        port_count=random.choice([8, 16, 24])
    )
    resp = client.post('/boards/', json=data)
    assert 200 == resp.status_code and resp.data.isdigit()


@pytest.mark.usefixtures("client")
def test_board_get_one(client):
    board_id = 1
    resp = client.get(f'/boards/{board_id}')
    assert 200 == resp.status_code and isinstance(resp.get_json(), dict)
