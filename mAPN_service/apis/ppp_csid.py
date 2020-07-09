import os
from http import HTTPStatus
from flask import Blueprint, request, jsonify, abort
from mAPN_service.config import session_scope
from mAPN_service.models.radius.radcheck import RadCheck
from mAPN_service.modules import row2dict
from mAPN_service.modules.auth import check_api_key


blueprint_ppp_csid = Blueprint("ppp_csid", __name__)
radius_radcheck_password_op = os.environ.get("RADIUS_USERNAME_PASSWORD_OP")


def get_all_pppoe_checks():
    checks = list()
    with session_scope() as db:
        found = db.query(RadCheck).all()
        checks = [row2dict(row) for row in found]
    # return all raw checks
    return checks


def get_checks_by_username(pppoe_username):
    checks = list()
    with session_scope() as db:
        found = db.query(RadCheck).filter_by(username=pppoe_username).all()
        checks = [row2dict(row) for row in found]
    return checks


def create() -> int:
    data = -1
    payload = request.get_json()
    required_fields = ["ppp_username", "ppp_password", "ppp_rate_limit"]
    for k in required_fields:
        if k not in payload:
            abort(HTTPStatus.BAD_REQUEST, f"{k} is required.")

    with session_scope() as db:
        found = (
            db.query(RadCheck)
            .filter_by(
                username=payload.get("ppp_username"),
                attribute=radius_radcheck_password_op,
            )
            .first()
        )
        if not found:
            radcheck = RadCheck(
                id=None,
                username=payload.get("ppp_username"),
                attribute=radius_radcheck_password_op,
                op=":=",
                value=payload.get("ppp_password"),
            )
            db.add(radcheck)
            db.flush()
            db.refresh(radcheck)
            data = radcheck.id
        else:
            abort(
                HTTPStatus.CONFLICT,
                "Board {} already exists.".format(payload.get("ppp_username")),
            )
    return data


@blueprint_ppp_csid.route("/<pppoe_username>", methods=["GET"])
@check_api_key
def get_check(pppoe_username):
    if request.method == "GET":
        return jsonify(get_checks_by_username(pppoe_username))


@blueprint_ppp_csid.route("/", methods=["GET", "POST"])
@check_api_key
def index():
    if request.method == "GET":
        return jsonify(get_all_pppoe_checks())
    else:
        return str(create())
