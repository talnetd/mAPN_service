from flask import Blueprint, request
from mAPN_service.config import session_scope
from mAPN_service.models.network_olt import  Network_Olt
from mAPN_service.modules import row2dict


blueprint_olts = Blueprint('network_olts', __name__)


def show_all():
    return 'All OLTs'


def create():

    with session_scope() as db:
        olt = Network_Olt(**request.form)
        db.add(olt)
        db.flush()
        db.refresh(olt)
        data = row2dict(olt)
        return data


@blueprint_olts.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return show_all()
    else:
        return create()
