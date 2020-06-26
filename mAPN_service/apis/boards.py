from http import HTTPStatus
from flask import Blueprint, request, jsonify, abort
from mAPN_service.config import session_scope
from mAPN_service.models.boards import Boards
from mAPN_service.modules import row2dict
from mAPN_service.modules.auth import check_api_key


blueprint_boards = Blueprint("boards", __name__)


def get_boards():
    boards = list()
    with session_scope() as db:
        found = db.query(Boards).all()
        boards = [row2dict(row) for row in found]
    return boards


def create() -> int:
    data = -1
    payload = request.get_json()
    required_fields = []
    for k in required_fields:
        if k not in payload:
            abort(HTTPStatus.BAD_REQUEST, f"{k} is required.")

    with session_scope() as db:
        found = db.query(Boards).filter_by(id=payload.get("id")).first()
        if not found:
            board = Boards(**payload)
            db.add(board)
            db.flush()
            db.refresh(board)
            data = board.id
        else:
            abort(
                HTTPStatus.CONFLICT,
                "Board {} already exists.".format(payload.get("id")),
            )
    return data


def get_boards_by_id(board_id) -> dict:
    found = dict()
    with session_scope() as db:
        record = db.query(Boards).filter_by(id=board_id).first()
        if record:
            found = row2dict(record)
    return found


@blueprint_boards.route("/<int:board_id>", methods=["GET"])
@check_api_key
def index_board_id(board_id):
    if request.method == "GET":
        return get_boards_by_id(board_id)


@blueprint_boards.route("/", methods=["GET", "POST"])
@check_api_key
def index():
    if request.method == "GET":
        return jsonify(get_boards())
    else:
        return str(create())
