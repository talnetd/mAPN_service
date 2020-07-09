from mAPN_service import app
from mAPN_service.apis import blueprint_index
from mAPN_service.apis.boards import blueprint_boards
from mAPN_service.apis.custom_traffic_plan import blueprint_CTP
from mAPN_service.apis.customers import blueprint_customers
from mAPN_service.apis.internet_traffic_plan import blueprint_ITP
from mAPN_service.apis.locations import blueprint_locations
from mAPN_service.apis.microtik import blueprint_microtik
from mAPN_service.apis.network_olts import blueprint_olts
from mAPN_service.apis.network_routers import blueprint_routers
from mAPN_service.apis.partners import blueprint_partners
from mAPN_service.apis.ppp_csid import blueprint_ppp_csid
from mAPN_service.apis.pppoe_groups import blueprint_pppoe_user_groups

# from mAPN_service.apis.ppp_rsid import blueprint_ppp_rsid
from mAPN_service.apis.pppoe_users import blueprint_pppoe_users
from mAPN_service.apis.voip_traffic_plan import blueprint_VTP


def register_routes(app):
    app.register_blueprint(blueprint_index, url_prefix="/")
    app.register_blueprint(blueprint_customers, url_prefix="/customers")
    app.register_blueprint(blueprint_CTP, url_prefix="/custom_traffic_plan")
    app.register_blueprint(blueprint_ITP, url_prefix="/internet_traffic_plan")
    app.register_blueprint(blueprint_partners, url_prefix="/partners")
    app.register_blueprint(blueprint_locations, url_prefix="/locations")
    app.register_blueprint(blueprint_boards, url_prefix="/boards")
    app.register_blueprint(blueprint_olts, url_prefix="/olts")
    app.register_blueprint(blueprint_routers, url_prefix="/routers")
    app.register_blueprint(blueprint_microtik, url_prefix="/microtik")
    app.register_blueprint(blueprint_VTP, url_prefix="/voip_traffic_plan")
    app.register_blueprint(blueprint_ppp_csid, url_prefix="/ppp_csid")
    # app.register_blueprint(blueprint_ppp_rsid, url_prefix="/ppp_rsid")
    app.register_blueprint(blueprint_pppoe_users, url_prefix="/pppoe/users")
    app.register_blueprint(
        blueprint_pppoe_user_groups, url_prefix="/pppoe/user_groups"
    )
