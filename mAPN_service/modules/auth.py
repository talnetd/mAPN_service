from functools import wraps
from http import HTTPStatus
from flask import request, abort
from mAPN_service.config import APP_API_KEY


def check_api_key(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        auth_header_value = request.headers.get("Authorization")

        if not auth_header_value:
            abort(HTTPStatus.UNPROCESSABLE_ENTITY)

        api_key = auth_header_value.replace("Bearer ", "")
        if api_key != APP_API_KEY:
            abort(HTTPStatus.UNAUTHORIZED)

        return f(*args, **kwargs)

    return wrap
