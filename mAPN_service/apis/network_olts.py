from http import HTTPStatus
from flask import Blueprint, request, jsonify, abort
from mAPN_service.config import session_scope
from mAPN_service.models.network_olt import Network_Olt
from mAPN_service.modules import row2dict
from mAPN_service.modules.auth import check_api_key


blueprint_olts = Blueprint("network_olts", __name__)


def get_olts():
    olts = list()
    with session_scope() as db:
        found = db.query(Network_Olt).all()
        olts = [row2dict(row) for row in found]
    return olts


def create() -> int:
    data = -1
    payload = request.get_json()
    required_fields = []
    for k in required_fields:
        if k not in payload:
            abort(HTTPStatus.BAD_REQUEST, f"{k} is required.")

    with session_scope() as db:
        found = db.query(Network_Olt).filter_by(id=payload.get("id")).first()
        if not found:
            olt = Network_Olt(**payload)
            db.add(olt)
            db.flush()
            db.refresh(olt)
            data = olt.id
        else:
            abort(
                HTTPStatus.CONFLICT, "OLT {} already exists.".format(payload.get("id"))
            )
    return data


def get_olts_id(olt_id) -> dict:
    found = dict()
    with session_scope() as db:
        found = db.query(Network_Olt).filter_by(id=olt_id).first()
        found = row2dict(found)
    return found


@blueprint_olts.route("/<int:olt_id>", methods=["GET"])
@check_api_key
def index_olts_id(olt_id):
    if request.method == "GET":
        return get_olts_id(olt_id)


@blueprint_olts.route("/", methods=["GET", "POST"])
@check_api_key
def index():
    if request.method == "GET":
        return jsonify(get_olts())
    else:
        return str(create())
