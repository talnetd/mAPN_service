from flask import Blueprint, request, jsonify
from mAPN_service.config import session_scope
from mAPN_service.models.partner import Partner
from mAPN_service.modules import row2dict


blueprint_partners = Blueprint('partners', __name__)


def get_partners() -> list:
    partners = list()
    with session_scope() as db:
        found = db.query(Partner).all()
        partners = [row2dict(row) for row in found]
    return partners


def create() -> int:
    data = -1
    with session_scope() as db:
        partner = Partner(**request.form)
        db.add(partner)
        db.flush()
        db.refresh(partner)
        data = partner.id
    return data


def get_partners_by_id(partner_id) -> dict:
    found = dict()
    with session_scope() as db:
        found = db.query(Partner).filter_by(id=partner_id).first()
        found = row2dict(found)
    return found


@blueprint_partners.route('/<int:partner_id>', methods=['GET'])
def index_partnersid(partner_id):
    if request.method == 'GET':
        return get_partners_by_id(partner_id)


@blueprint_partners.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return jsonify(get_partners())
    else:
        return str(create())
