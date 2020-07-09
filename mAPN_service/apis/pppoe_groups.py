import os

from http import HTTPStatus
from flask import Blueprint, request, jsonify, abort
from mAPN_service.config import session_scope
from mAPN_service.models.radius.radgroupreply import RadGroupReply as Rgr
from mAPN_service.models.radius.radusergroup import RadUserGroup as Rug

from mAPN_service.modules import row2dict
from mAPN_service.modules.auth import check_api_key


blueprint_pppoe_user_groups = Blueprint("pppoe_user_groups", __name__)
radius_rate_limi_op = os.environ.get(
    'RADIUS_MIKROTIK_RATE_LIMIT_OP',
    'Rate-Limit')

def get_all_rgr_replies():
    replies = list()
    with session_scope() as db:
        found = db.query(Rgr).all()
        replies = [row2dict(row) for row in found ]
    return replies

def bind_ppp_group():
    data = -1
    payload = request.get_json()
    required_fields = ["ppp_username", "ppp_groupname","ppp_priority"]
    for k in required_fields:
        if k not in payload:
            abort(HTTPStatus.BAD_REQUEST, f"{k} is required.")

    with session_scope() as db:
        found = db.query(Rug).filter_by(username=payload.get("ppp_username"),
                                        groupname=payload.get("ppp_groupname")).first()
        if not found:
            rug = Rug(username=payload.get("ppp_username"),
                        groupname=payload.get("ppp_groupname"),
                        priority=payload.get("ppp_priority")
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

def get_rgr_by_group_name(ppp_groupname):
    replies = list()
    with session_scope() as db:
        found = db.query(Rgr).filter_by(groupname=ppp_groupname).all()
        replies = [row2dict(row) for row in found]
    return replies


def create() -> int:
    data = -1
    payload = request.get_json()
    required_fields = ["groupname", "group_rate_limit"]
    for k in required_fields:
        if k not in payload:
            abort(HTTPStatus.BAD_REQUEST, f"{k} is required.")

    with session_scope() as db:
        found = db.query(Rgr).filter_by(groupname=payload.get("groupname")).first()
        if not found:
            rgr = Rgr(id=None,
                        groupname=payload.get("groupname"),
                        attribute=radius_rate_limi_op,
                        op="==",
                        value=payload.get("group_rate_limit")
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

@blueprint_pppoe_user_groups.route("/<ppp_groupname>", methods=["GET"])
@check_api_key
def get_group(ppp_groupname):
    if request.method == "GET":
        return jsonify(get_rgr_by_group_name(ppp_groupname))

@blueprint_pppoe_user_groups.route("/bind", methods=["POST"])
@check_api_key
def bind_group():
    if request.method == "POST":
        return jsonify(bind_ppp_group())

@blueprint_pppoe_user_groups.route("/", methods=["GET", "POST"])
@check_api_key
def index():
    if request.method == "GET":
        return jsonify(get_all_rgr_replies())
    else:
        return str(create())
