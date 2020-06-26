from http import HTTPStatus
from flask import Blueprint, request, jsonify, abort
from mAPN_service.config import session_scope
from mAPN_service.models.location import Location
from mAPN_service.modules import row2dict
from mAPN_service.modules.auth import check_api_key


blueprint_locations = Blueprint("locations", __name__)


def get_locations():
    locations = list()
    with session_scope() as db:
        found = db.query(Location).all()
        locations = [row2dict(row) for row in found]
    return locations


def create() -> int:
    data = -1
    payload = request.get_json()
    required_fields = []
    for k in required_fields:
        if k not in payload:
            abort(HTTPStatus.BAD_REQUEST, f"{k} is required.")

    with session_scope() as db:
        found = db.query(Location).filter_by(id=payload.get("id")).first()
        if not found:
            location = Location(**payload)
            db.add(location)
            db.flush()
            db.refresh(location)
            data = location.id
        else:
            abort(
                HTTPStatus.CONFLICT,
                "Location {} already exists.".format(payload.get("id")),
            )
    return data


def get_locations_id(location_id) -> dict:
    found = dict()
    with session_scope() as db:
        found = db.query(Location).filter_by(id=location_id).first()
        found = row2dict(found)
    return found


@blueprint_locations.route("<int:location_id>", methods=["GET"])
@check_api_key
def index_location_id(location_id):
    if request.method == "GET":
        return get_locations_id(location_id)


@blueprint_locations.route("/", methods=["GET", "POST"])
@check_api_key
def index():
    if request.method == "GET":
        return jsonify(get_locations())
    else:
        return str(create())
