from flask import Flask, jsonify
from flask_restful import Api

from core.settings import DEVELOPMENT_API_HOST, DEVELOPMENT_API_PORT, DEVELOPMENT_API_DEBUG
from core.api.resources import add_endpoints, Status, Method


app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True
app.url_map.strict_slashes = False
api = Api(app)


def handle_error(status_code, message):
    return jsonify(errorCode=status_code, errorMsg=message), status_code


add_endpoints(api)


@app.after_request
def close_db_session(response):
    return response


@app.route('/')
def server_info():
    return 'EcobiciStatistics - A little project related use ECOBICI BA'


if __name__ == '__main__':
    app.run(
        host=DEVELOPMENT_API_HOST,
        port=DEVELOPMENT_API_PORT,
        debug=DEVELOPMENT_API_DEBUG
    )
