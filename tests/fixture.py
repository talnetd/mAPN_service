import os
import pytest
from flask import request
from mAPN_service.app import app
from mAPN_service.config import API_KEY


@pytest.fixture
def client():

    tc = app.test_client()
    tc.environ_base['HTTP_AUTHORIZATION'] = f'Bearer {API_KEY}'
    return tc
