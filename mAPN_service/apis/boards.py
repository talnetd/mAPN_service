from flask import Blueprint, request, jsonify
from mAPN_service.config import session_scope
from mAPN_service.models.boards import Boards
from mAPN_service.modules import row2dict
from mAPN_service.modules.auth import check_api_key


blueprint_boards = Blueprint('boards', __name__)


def get_boards():
    boards = list()
    with session_scope() as db:
        found = db.query(Boards).all()
        boards = [row2dict(row) for row in found]
    return boards


def create() -> int:
    data = -1
    with session_scope() as db:
        board = Boards(**request.get_json())
        db.add(board)
        db.flush()
        db.refresh(board)
        data = board.id
    return data


def get_boards_by_id(board_id) -> dict:
    found = dict()
    with session_scope() as db:
        found = db.query(Boards).filter_by(id=board_id).first()
        found = row2dict(found)
    return found


@blueprint_boards.route('/<int:board_id>', methods=['GET'])
@check_api_key
def index_board_id(board_id):
    if request.method == 'GET':
        return get_boards_by_id(board_id)


@blueprint_boards.route('/', methods=['GET', 'POST'])
@check_api_key
def index():
    if request.method == 'GET':
        return jsonify(get_boards())
    else:
        return str(create())
