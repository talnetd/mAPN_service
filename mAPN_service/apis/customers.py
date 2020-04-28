from http import HTTPStatus
from flask import (
    Blueprint,
    request,
    jsonify,
    abort
)
from mAPN_service.config import session_scope
from mAPN_service.models.customer import Customer
from mAPN_service.modules import row2dict
from mAPN_service.modules.auth import check_api_key


blueprint_customers = Blueprint('customers', __name__)


def get_customers():
    customers = list()
    with session_scope() as db:
        found = db.query(Customer).all()
        customers = [row2dict(row) for row in found]
    return customers


def create() -> int:
    data = -1
    payload = request.get_json()
    required_fields = ['id', 'username', 'password', 'email', 'phone']
    for k in required_fields:
        if k not in payload:
            abort(HTTPStatus.BAD_REQUEST, f'{k} is required.')

    with session_scope() as db:
        found = db.query(Customer).filter_by(id=payload.get('id')).first()
        if not found:
            customer = Customer(**payload)
            db.add(customer)
            db.flush()
            db.refresh(customer)
            data = customer.id
        else:
            abort(
                HTTPStatus.CONFLICT,
                'User {} already exists.'.format(payload.get('id')))
    return data


def get_customer_id(customer_id) -> dict:
    found = dict()
    with session_scope() as db:
        record = db.query(Customer).filter_by(id=customer_id).first()
        if record:
            found = row2dict(record)
    return found


@blueprint_customers.route('/<int:customer_id>', methods=['GET'])
@check_api_key
def index_customer_id(customer_id):
    if request.method == 'GET':
        return get_customer_id(customer_id)


@blueprint_customers.route('/', methods=['GET', 'POST'])
@check_api_key
def index():
    if request.method == 'GET':
        return jsonify(get_customers())
    else:
        return str(create())
