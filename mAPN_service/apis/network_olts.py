from flask import Blueprint, request, jsonify
from mAPN_service.config import session_scope
from mAPN_service.models.network_olt import Network_Olt
from mAPN_service.modules import row2dict


blueprint_olts = Blueprint('network_olts', __name__)


def get_olts():
    olts = list()
    with session_scope() as db:
        found = db.query(Network_Olt).all()
        olts = [row2dict(row) for row in found]
    return olts


def create() -> int:
    data = -1
    with session_scope() as db:
        olt = Network_Olt(**request.get_json())
        db.add(olt)
        db.flush()
        db.refresh(olt)
        data = olt.id
    return data


def get_olts_id(olt_id) -> dict:
    found = dict()
    with session_scope() as db:
        found = db.query(Network_Olt).filter_by(id=olt_id).first()
        found = row2dict(found)
    return found


@blueprint_olts.route('/<int:olt_id>', methods=['GET'])
def index_olts_id(olt_id):
    if request.method == 'GET':
        return get_olts_id(olt_id)


@blueprint_olts.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return jsonify(get_olts())
    else:
        return str(create())
