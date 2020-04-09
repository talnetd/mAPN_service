from flask import Blueprint, request
from mAPN_service.config import session_scope
from mAPN_service.models.customer import Customer


blueprint_customers = Blueprint('customers', __name__)


def show_all():
    return 'All customers'


def create():
    with session_scope() as db:
        customer = Customer(**request.form)
        db.add(customer)
        return customer


@blueprint_customers.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return show_all()
    else:
        return create()
