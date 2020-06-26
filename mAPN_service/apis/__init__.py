from flask import Blueprint


blueprint_index = Blueprint("index", __name__)


@blueprint_index.route("/")
def index():
    return "Hello, world!!!"
