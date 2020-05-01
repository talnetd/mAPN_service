from mAPN_service import app
from mAPN_service.apis import blueprint_index
from mAPN_service.apis.customers import blueprint_customers
from mAPN_service.apis.partners import blueprint_partners
from mAPN_service.apis.locations import blueprint_locations
from mAPN_service.apis.boards import blueprint_boards
from mAPN_service.apis.network_olts import blueprint_olts
from mAPN_service.apis.network_routers import blueprint_routers
from mAPN_service.apis.microtik import blueprint_microtik

def register_routes(app):
    app.register_blueprint(blueprint_index, url_prefix='/')
    app.register_blueprint(blueprint_customers, url_prefix='/customers')
    app.register_blueprint(blueprint_partners, url_prefix='/partners')
    app.register_blueprint(blueprint_locations, url_prefix='/locations')
    app.register_blueprint(blueprint_boards, url_prefix='/boards')
    app.register_blueprint(blueprint_olts, url_prefix='/olts')
    app.register_blueprint(blueprint_routers, url_prefix='/routers')
    app.register_blueprint(blueprint_microtik, url_prefix='/microtik')
