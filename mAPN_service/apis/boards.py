from flask import Blueprint, request
from mAPN_service.config import session_scope
from mAPN_service.models.boards import Boards
from mAPN_service.modules import row2dict


blueprint_boards = Blueprint('boards', __name__)


def show_all():
    return 'All Boards'


def create():

    with session_scope() as db:
        board = Boards(**request.form)
        db.add(board)
        db.flush()
        db.refresh(board)
        data = row2dict(board)
        return data


@blueprint_boards.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return show_all()
    else:
        return create()
