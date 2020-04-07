from flask import Flask
from mAPN_service.routes import register_routes


app = Flask(__name__)
register_routes(app)
