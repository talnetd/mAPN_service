from mAPN_service import app
from mAPN_service.apis import blueprint_index
from mAPN_service.apis.customers import blueprint_customers
from mAPN_service.apis.partners import blueprint_partners
from mAPN_service.apis.locations import blueprint_locations


def register_routes(app):
    app.register_blueprint(blueprint_index, url_prefix='/')
    app.register_blueprint(blueprint_customers, url_prefix='/customers')
    app.register_blueprint(blueprint_partners, url_prefix='/partners')
    app.register_blueprint(blueprint_locations, url_prefix='/locations')
