from mAPN_service import app
from mAPN_service.apis import blueprint_index
from mAPN_service.apis.ppp_csid import blueprint_ppp_csid
from mAPN_service.apis.ppp_rsid import blueprint_ppp_rsid


def register_routes(app):
    app.register_blueprint(blueprint_index, url_prefix="/")
    app.register_blueprint(blueprint_ppp_csid, url_prefix="/ppp_csid")
    app.register_blueprint(blueprint_ppp_rsid, url_prefix="/ppp_rsid")
