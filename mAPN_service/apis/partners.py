from flask import Blueprint, request
from mAPN_service.config import session_scope
from mAPN_service.models.partner import Partner
from mAPN_service.modules import row2dict


blueprint_partners = Blueprint('partners', __name__)


def show_all():
    return 'All Partners'


def create():

    with session_scope() as db:
        partner = Partner(**request.form)
        db.add(partner)
        db.flush()
        db.refresh(partner)
        data = row2dict(partner)
        return data


@blueprint_partners.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return show_all()
    else:
        return create()
