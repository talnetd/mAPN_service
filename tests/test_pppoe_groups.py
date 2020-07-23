import pytest


@pytest.mark.usefixtures("client")
def test_create_radius_groupreply(client):
    data = dict(groupname="testing PPPOE group #1", group_rate_limit=999)
    resp = client.post("/pppoe/user_groups/", json=data)
    assert resp.status_code == 200


@pytest.mark.usefixtures("client")
def test_get_radius_groupreply(client):
    resp = client.get("/pppoe/user_groups/")
    assert resp.status_code == 200 and isinstance(resp.get_json(), list)


@pytest.mark.usefixtures("client")
def test_bind_ppp_group(client):
    data = dict(ppp_username="test user #10", ppp_groupname="testing PPPOE group #1", ppp_priority=1)
    resp = client.post("/pppoe/user_groups/bind", json=data)
    assert resp.status_code == 200


@pytest.mark.usefixtures("client")
def test_update_ppp_group(client):
    data = dict(
        ppp_username="test user #10",
        ppp_groupname="testing PPPOE group #1",
        new_groupname="new PPPOE group #2",
    )
    resp = client.put("/pppoe/user_groups/bind", json=data)
    assert resp.status_code == 200


@pytest.mark.usefixtures("client")
def test_unbind_ppp_group(client):
    data = dict(ppp_username="test user #10", ppp_groupname="new PPPOE group #2")
    resp = client.delete("/pppoe/user_groups/bind", json=data)
    assert resp.status_code == 200


@pytest.mark.usefixtures("client")
def test_get_ppp_groupname(client):
    resp = client.get("/pppoe/user_groups/{}".format("testing PPPOE group #1"))
    assert resp.status_code == 200 and isinstance(resp.get_json(), list)


@pytest.mark.usefixtures("client")
def test_create_rate_limit(client):
    data = dict(
        ppp_groupname="group #008",
        group_rate_limit=100
    )
    resp = client.post("/pppoe/user_groups/update_rate_limit", json=data)
    assert resp.status_code == 200


@pytest.mark.usefixtures("client")
def test_update_rate_limit(client):
    data = dict(
        ppp_groupname="group #008",
        group_rate_limit=150
    )
    resp = client.put("/pppoe/user_groups/update_rate_limit", json=data)
    assert resp.status_code == 200
