from flask import (
    Blueprint,
    request,
    jsonify
)
from mAPN_service.config import session_scope
from mAPN_service.models.customer import Customer
from mAPN_service.modules import row2dict


blueprint_customers = Blueprint('customers', __name__)


def get_customers():
    customers = list()
    with session_scope() as db:
        found = db.query(Customer).all()
        customers = [row2dict(row) for row in found]
    return customers


def create() -> int:
    data = -1
    with session_scope() as db:
        customer = Customer(**request.get_json())
        db.add(customer)
        db.flush()
        db.refresh(customer)
        data = customer.id
    return data


def get_customer_id(customer_id) -> dict:
    found = dict()
    with session_scope() as db:
        found = db.query(Customer).filter_by(id=customer_id).first()
        found = row2dict(found)
    return found


@blueprint_customers.route('/<int:customer_id>', methods=['GET'])
def index_customer_id(customer_id):
    if request.method == 'GET':
        return get_customer_id(customer_id)


@blueprint_customers.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return jsonify(get_customers())
    else:
        return str(create())
