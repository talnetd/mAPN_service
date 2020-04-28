from flask import Flask, make_response, jsonify
from mAPN_service.routes import register_routes


app = Flask(__name__)
register_routes(app)


@app.errorhandler(Exception)
def generic_error_handler(error):
    resp = make_response(jsonify(
        message=error))
    resp.headers['Content-Type'] = 'application/json'
    return resp
