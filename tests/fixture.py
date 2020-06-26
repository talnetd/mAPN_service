import pytest
from mAPN_service.app import app
from mAPN_service.config import APP_API_KEY
from mAPN_service.modules import libmysql


@pytest.fixture
def client():

    tc = app.test_client()
    tc.environ_base["HTTP_AUTHORIZATION"] = f"Bearer {APP_API_KEY}"
    return tc


@pytest.fixture
def mysql_lib():
    return libmysql
