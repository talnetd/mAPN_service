from http import HTTPStatus
from flask import Blueprint, request, jsonify, abort
from mAPN_service.config import session_scope
from mAPN_service.models.partner import Partner
from mAPN_service.modules import row2dict
from mAPN_service.modules.auth import check_api_key


blueprint_partners = Blueprint('partners', __name__)


def get_partners() -> list:
    partners = list()
    with session_scope() as db:
        found = db.query(Partner).all()
        partners = [row2dict(row) for row in found]
    return partners


def create() -> int:
    data = -1
    payload = request.get_json()
    required_fields = []
    for k in required_fields:
        if k not in payload:
            abort(HTTPStatus.BAD_REQUEST, f'{k} is required.')

    with session_scope() as db:
        found = db.query(Partner).filter_by(id=payload.get('id')).first()
        if not found:
            partner = Partner(**payload)
            db.add(partner)
            db.flush()
            db.refresh(partner)
            data = partner.id
        else:
            abort(
                HTTPStatus.CONFLICT,
                'Partner {} already exists.'.format(payload.get('id')))
    return data


def get_partners_by_id(partner_id) -> dict:
    found = dict()
    with session_scope() as db:
        found = db.query(Partner).filter_by(id=partner_id).first()
        found = row2dict(found)
    return found


@blueprint_partners.route('/<int:partner_id>', methods=['GET'])
@check_api_key
def index_partnersid(partner_id):
    if request.method == 'GET':
        return get_partners_by_id(partner_id)


@blueprint_partners.route('/', methods=['GET', 'POST'])
@check_api_key
def index():
    if request.method == 'GET':
        return jsonify(get_partners())
    else:
        return str(create())
