from flask import Flask, make_response, jsonify
from mAPN_service.routes import register_routes


app = Flask(__name__)
register_routes(app)
