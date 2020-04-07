from mAPN_service import app
from mAPN_service.apis import blueprint_index
from mAPN_service.apis.customers import blueprint_customers


def register_routes(app):
    app.register_blueprint(blueprint_index, url_prefix='/')
    app.register_blueprint(blueprint_customers, url_prefix='/customers')
