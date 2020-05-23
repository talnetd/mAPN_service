from http import HTTPStatus

from flask import Blueprint, abort, jsonify, request

from mAPN_service.config import session_scope
from mAPN_service.models.voip_traffic_plan import VoipTrafficPlan
from mAPN_service.modules import row2dict
from mAPN_service.modules.auth import check_api_key

blueprint_VTP = Blueprint('voip_traffic_plan', __name__)


def create() -> int:
    data = -1
    payload = request.get_json()
    required_fields = ['title', 'service_name', 'price']
    for k in required_fields:
        if k not in payload:
            abort(HTTPStatus.BAD_REQUEST, f'{k} is required.')

    with session_scope() as db:
        found = db.query(VoipTrafficPlan).filter_by(
            id=payload.get('id')).first()
        if not found:
            plan_info = VoipTrafficPlan(**payload)
            db.add(plan_info)
            db.flush()
            db.refresh(plan_info)
            data = plan_info.id
        else:
            abort(
                HTTPStatus.CONFLICT,
                'Custom Traffic Plan {} already exists.'.format(
                    payload.get('id')))

    return data


def get_plans():
    plans = list()
    with session_scope() as db:
        found = db.query(VoipTrafficPlan).all()
        plans = [row2dict(row) for row in found]

    return plans


def get_plan_by_id(plan_id):
    found = dict()
    with session_scope() as db:
        record = db.query(VoipTrafficPlan).filter_by(id=plan_id).first()
        if record:
            found = row2dict(record)
    return found


@blueprint_VTP.route('/<int:plan_id>', methods=['GET'])
@check_api_key
def index_plan_id(plan_id):
    if request.method == 'GET':
        return get_plan_by_id(plan_id)


@blueprint_VTP.route('/', methods=['GET', 'POST'])
@check_api_key
def index():
    if request.method == 'GET':
        return jsonify(get_plans())
    else:
        return str(create())
