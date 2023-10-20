import flask
import json
import http

from flask import request
from terra import Terra

terra = Terra(api_key='YOUR API KEY', dev_id='YOUR DEV ID', secret='YOUR TERRA SECRET')

def hello_terra():
    # Print it here
    # print(json.dumps(request.get_json(), indent = 4))

    # You can directly use this to handle a terra webhook:
    response = terra.handle_flask_webhook(request)
    
    return flask.Response("Yay Terra is awesome",  http.HTTPStatus.OK)

def setup(app: flask.Flask):
    bp = flask.Blueprint("sample", __name__, "")
    bp.add_url_rule("/hello", view_func = hello_terra, methods = ["POST"])
    app.register_blueprint(bp)