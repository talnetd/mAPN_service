from flask import Blueprint, request
from mAPN_service.config import session_scope
from mAPN_service.models.network_router import Network_Router
from mAPN_service.modules import row2dict


blueprint_routers = Blueprint('network_routers', __name__)


def show_all():
    return 'All Boards'


def create():

    with session_scope() as db:
        router = Network_Router(**request.form)
        db.add(router)
        db.flush()
        db.refresh(router)
        data = row2dict(router)
        return data


@blueprint_routers.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return show_all()
    else:
        return create()
