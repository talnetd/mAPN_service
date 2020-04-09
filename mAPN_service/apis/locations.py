from flask import Blueprint, request
from mAPN_service.config import session_scope
from mAPN_service.models.location import Location
from mAPN_service.modules import row2dict


blueprint_locations = Blueprint('locations', __name__)


def show_all():
    return 'All Locations'


def create():
    with session_scope() as db:
        location = Location(**request.form)
        db.add(location)
        db.flush()
        db.refresh(location)
        data = row2dict(location)
        return data


@blueprint_locations.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return show_all()
    else:
        return create()
