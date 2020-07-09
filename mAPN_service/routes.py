from mAPN_service import app
from mAPN_service.apis import blueprint_index
from mAPN_service.apis.pppoe_users import blueprint_pppoe_users
from mAPN_service.apis.pppoe_groups import blueprint_pppoe_user_groups


def register_routes(app):
    app.register_blueprint(blueprint_index, url_prefix="/")
    app.register_blueprint(blueprint_pppoe_users, url_prefix="/pppoe/users")
    app.register_blueprint(blueprint_pppoe_user_groups, url_prefix="/pppoe/user_groups")
