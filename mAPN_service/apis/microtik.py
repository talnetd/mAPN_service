"""
EXAMPLE CURL:

curl -X POST <api-host>:<api-port>/microtik/ \
-H 'Authorization: Bearer 123' \
-H 'Content-Type: application/json' \
-d '{"ip": "<router-ip>", "username": "admin", "password": "<router-password>", "resource": "/ip/address", "action": "call", "command": "print"}'
"""

from http import HTTPStatus
from flask import (
    Blueprint,
    request,
    jsonify,
    make_response,
    abort
)
import routeros_api
from mAPN_service.modules.auth import check_api_key


blueprint_microtik = Blueprint('microtik', __name__)


def execute_command():

    result = None
    payload = request.get_json()
    required_fields = ['ip', 'username', 'password', 'resource', 'action']
    for k in required_fields:
        if k not in payload:
            abort(HTTPStatus.BAD_REQUEST, f'{k} is required.')

    # NOTE:
    # `get` is equivalent to `call('print')`
    # `add` is to set new value
    # `set` is to update value
    # `remove` is to remove value
    # `call` is to execute command (`get`, `add`, `set`, and `remove` are
    #                               also wrapper actions which execute `call`)
    supported_actions = ['get', 'add', 'set', 'remove', 'call']
    action = payload.get('action')
    if action not in supported_actions:
        abort(HTTPStatus.BAD_REQUEST, f'Unsupported action: {action}')

    router = routeros_api.RouterOsApiPool(
        payload.get('ip'),
        username=payload.get('username'),
        password=payload.get('password'),
        plaintext_login=True
    )
    try:
        api = router.get_api()
        resource = api.get_resource(
            payload.get('resource')
        )
        fn_resource = getattr(resource, action)
        command = payload.get('command')
        params = payload.get('payload') or dict()
        if action == 'call':
            if not command:
                abort(HTTPStatus.BAD_REQUEST,
                      f'Attribute "command" is required '
                      f'for action "{action}".')
            result = fn_resource(
                command=command,
                arguments=params)
        else:
            # NOTE:
            # if action is `remove`, param needs only `id` attribute and value.
            if action in ['set', 'remove'] and 'id' not in params:
                abort(HTTPStatus.BAD_REQUEST,
                      f'Attribute "id" is required for action "{action}".')
            result = fn_resource(**params)

        router.disconnect()
    except Exception as exc:
        abort(HTTPStatus.SERVICE_UNAVAILABLE, exc)
    return result


@blueprint_microtik.route('/', methods=['POST'])
@check_api_key
def index():
    if request.method == 'POST':
        result = execute_command()
        resp = make_response(jsonify(result))
        resp.headers['Content-Type'] = 'application/json'
        return resp
    else:
        abort(HTTPStatus.METHOD_NOT_ALLOWED)
