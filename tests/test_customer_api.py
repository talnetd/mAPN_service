import random

import pytest


@pytest.mark.usefixtures("client")
def test_customer_index(client):
    resp = client.get('/customers/')
    assert resp.status_code == 200 and isinstance(resp.get_json(), list)


@pytest.mark.usefixtures("client")
def test_customer_create(client):
    data = dict(id=random.randint(0, 100),
                username='name1',
                email='name1@email.com',
                password='name1',
                full_name='Name One')
    resp = client.post('/customers/', json=data)
    assert 200 == resp.status_code and resp.data.isdigit()


@pytest.mark.usefixtures("client")
def test_customer_get_one(client):
    customer_id = 1
    resp = client.get(f'/customers/{customer_id}')
    assert 200 == resp.status_code and isinstance(resp.get_json(), dict)
