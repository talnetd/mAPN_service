import pytest


@pytest.mark.usefixtures("client")
def test_app(client):

    resp = client.get('/')
    assert 200 == resp.status_code
