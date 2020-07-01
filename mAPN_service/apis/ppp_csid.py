from http import HTTPStatus
from flask import Blueprint, request, jsonify, abort
from mAPN_service.modules.libmysql import get_connection, select, execute
from mAPN_service.modules.auth import check_api_key


blueprint_ppp_csid = Blueprint("ppp_csid", __name__)


def create() -> int:
    data = -1
    payload = request.get_json()
    required_fields = ["param1", "param2"]
    for k in required_fields:
        if k not in payload:
            abort(HTTPStatus.BAD_REQUEST, f"{k} is required.")

    # TODO: do things here

    return data


@blueprint_ppp_csid.route("/", methods=["GET", "POST"])
@check_api_key
def index():
    if request.method == "GET":
        return jsonify(dict())
    else:
        return str(create())
