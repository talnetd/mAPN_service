import pytest
from mAPN_service.app import app


@pytest.fixture
def client():
    app.testing = True
    return app.test_client()
