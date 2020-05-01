from http import HTTPStatus
from flask import Blueprint, request, jsonify, abort
from mAPN_service.config import session_scope
from mAPN_service.models.network_router import Network_Router
from mAPN_service.modules import row2dict
from mAPN_service.modules.auth import check_api_key


blueprint_routers = Blueprint('network_routers', __name__)


def get_routers():
    routers = list()
    with session_scope() as db:
        found = db.query(Network_Router).all()
        routers = [row2dict(row) for row in found]
    return routers


def create() -> -1:
    data = -1
    payload = request.get_json()
    required_fields = []
    for k in required_fields:
        if k not in payload:
            abort(HTTPStatus.BAD_REQUEST, f'{k} is required.')

    with session_scope() as db:
        found = db.query(Network_Router).filter_by(id=payload.get('id')).first()
        if not found:
            router = Network_Router(**payload)
            db.add(router)
            db.flush()
            db.refresh(router)
            data = router.id
        else:
            abort(
                HTTPStatus.CONFLICT,
                'Router {} already exists.'.format(payload.get('id')))
    return data


def get_routers_by_id(router_id) -> dict:
    found = dict()
    with session_scope() as db:
        found = db.query(Network_Router).filter_by(id=router_id).first()
        found = row2dict(found)
    return found


@blueprint_routers.route('/<int:router_id>', methods=['GET'])
@check_api_key
def index_router_id(router_id):
    if request.method == 'GET':
        return get_routers_by_id(router_id)


@blueprint_routers.route('/', methods=['GET', 'POST'])
@check_api_key
def index():
    if request.method == 'GET':
        return jsonify(get_routers())
    else:
        return str(create())
