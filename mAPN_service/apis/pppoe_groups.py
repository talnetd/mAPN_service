import os
from http import HTTPStatus

from flask import Blueprint, abort, jsonify, request
from mAPN_service.config import session_scope
from mAPN_service.models.radius.radgroupreply import RadGroupReply as Rgr
from mAPN_service.models.radius.radusergroup import RadUserGroup as Rug
from mAPN_service.modules import row2dict
from mAPN_service.modules.auth import check_api_key

blueprint_pppoe_user_groups = Blueprint("pppoe_user_groups", __name__)
radius_rate_limi_op = os.environ.get("RADIUS_MIKROTIK_RATE_LIMIT_OP", "Rate-Limit")


def get_all_rgr_replies():
    replies = list()
    with session_scope("radius") as db:
        found = db.query(Rgr).all()
        replies = [row2dict(row) for row in found]
    return replies


def get_rgr_by_group_name(ppp_groupname):
    replies = list()
    with session_scope("radius") as db:
        found = db.query(Rgr).filter_by(groupname=ppp_groupname).all()
        replies = [row2dict(row) for row in found]
    return replies


def create_rate_limit():
    data = -1
    payload = request.get_json()
    required_fields = ["ppp_groupname", "group_rate_limit"]
    for k in required_fields:
        if k not in payload:
            abort(HTTPStatus.BAD_REQUEST, f"{k} is required.")
    with session_scope("radius") as db:
        found = (
            db.query(Rgr)
            .filter_by(
                groupname=payload.get("ppp_groupname"), attribute=radius_rate_limi_op,
            )
            .first()
        )
        if not found:
            rgr = Rgr(
                id=None,
                groupname=payload.get("ppp_groupname"),
                attribute=radius_rate_limi_op,
                op="==",
                value=payload.get("group_rate_limit"),
            )
            db.add(rgr)
            db.flush()
            db.refresh(rgr)
            data = rgr.groupname
        else:
            abort(
                HTTPStatus.CONFLICT,
                "Group {} already binded to user.".format(payload.get("ppp_username")),
            )
    return data


def update_rate_limit():
    data = None
    payload = request.get_json()
    required_fields = ["ppp_groupname", "group_rate_limit"]
    for k in required_fields:
        if k not in payload:
            abort(HTTPStatus.BAD_REQUEST, f"{k} is required.")
    with session_scope("radius") as db:
        found = db.query(Rgr).filter_by(groupname=payload.get("ppp_groupname"),).first()
        if found:
            found.attribute = radius_rate_limi_op
            found.op = "=="
            found.value = payload.get("group_rate_limit")
            db.add(found)
            data = found.id
        else:
            abort(
                HTTPStatus.NOT_FOUND,
                "Group {} not found to update rate limit.".format(
                    payload.get("ppp_username")
                ),
            )
    return data


def bind_ppp_group():
    data = -1
    payload = request.get_json()
    required_fields = ["ppp_username", "ppp_groupname", "ppp_priority"]
    for k in required_fields:
        if k not in payload:
            abort(HTTPStatus.BAD_REQUEST, f"{k} is required.")

    with session_scope("radius") as db:
        found = (
            db.query(Rug)
            .filter_by(
                username=payload.get("ppp_username"),
                groupname=payload.get("ppp_groupname"),
            )
            .first()
        )
        if not found:
            rug = Rug(
                username=payload.get("ppp_username"),
                groupname=payload.get("ppp_groupname"),
                priority=payload.get("ppp_priority"),
            )
            db.add(rug)
            db.flush()
            db.refresh(rug)
            data = rug.username
        else:
            abort(
                HTTPStatus.CONFLICT,
                "Group {} already binded to user.".format(payload.get("ppp_username")),
            )
    return data


def unbind_ppp_group():
    data = -1
    payload = request.get_json()
    required_fields = ["ppp_username", "ppp_groupname"]
    for k in required_fields:
        if k not in payload:
            abort(HTTPStatus.BAD_REQUEST, f"{k} is required.")
    with session_scope("radius") as db:
        found = (
            db.query(Rug)
            .filter_by(
                username=payload.get("ppp_username"),
                groupname=payload.get("ppp_groupname"),
            )
            .first()
        )
        if found:
            db.delete(found)
        else:
            abort(
                HTTPStatus.NOT_FOUND,
                "Group information not found with {} and {}.".format(
                    payload.get("ppp_username"), payload.get("ppp_groupname")
                ),
            )
    return data


def update_ppp_group():
    data = None
    payload = request.get_json()
    required_fields = ["ppp_username", "ppp_groupname", "new_groupname"]
    for k in required_fields:
        if k not in payload:
            abort(HTTPStatus.BAD_REQUEST, f"{k} is required.")

    with session_scope("radius") as db:
        found = (
            db.query(Rug)
            .filter_by(
                username=payload.get("ppp_username"),
                groupname=payload.get("ppp_groupname"),
            )
            .first()
        )
        if found:
            found.groupname = payload.get("new_groupname")
            db.add(found)
            data = found.username
        else:
            abort(
                HTTPStatus.NOT_FOUND,
                "No plan information with {} and {} not found.".format(
                    payload.get("ppp_username"), payload.get("ppp_groupname")
                ),
            )
    return data


def create() -> int:
    data = -1
    payload = request.get_json()
    required_fields = ["groupname", "group_rate_limit"]
    for k in required_fields:
        if k not in payload:
            abort(HTTPStatus.BAD_REQUEST, f"{k} is required.")

    with session_scope("radius") as db:
        found = db.query(Rgr).filter_by(groupname=payload.get("groupname")).first()
        if not found:
            rgr = Rgr(
                id=None,
                groupname=payload.get("groupname"),
                attribute=radius_rate_limi_op,
                op="==",
                value=payload.get("group_rate_limit"),
            )
            db.add(rgr)
            db.flush()
            db.refresh(rgr)
            data = rgr.id
        else:
            abort(
                HTTPStatus.CONFLICT,
                "Group {} already exists.".format(payload.get("groupname")),
            )
    return data


@blueprint_pppoe_user_groups.route("/update_rate_limit", methods=["POST", "PUT"])
@check_api_key
def update_rate_limit_route():
    if request.method == "POST":
        return jsonify(create_rate_limit())
    elif request.method == "PUT":
        return jsonify(update_rate_limit())


@blueprint_pppoe_user_groups.route("/<ppp_groupname>", methods=["GET"])
@check_api_key
def get_group(ppp_groupname):
    if request.method == "GET":
        return jsonify(get_rgr_by_group_name(ppp_groupname))


@blueprint_pppoe_user_groups.route("/bind", methods=["POST", "PUT", "DELETE"])
@check_api_key
def bind_group():
    if request.method == "POST":
        return jsonify(bind_ppp_group())
    elif request.method == "PUT":
        return jsonify(update_ppp_group())
    elif request.method == "DELETE":
        return jsonify(unbind_ppp_group())


@blueprint_pppoe_user_groups.route("/", methods=["GET", "POST"])
@check_api_key
def index():
    if request.method == "GET":
        return jsonify(get_all_rgr_replies())
    else:
        return str(create())
