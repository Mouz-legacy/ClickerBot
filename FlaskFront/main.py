from flask import request
from app.config import *
from app.validator import validate_request
from app import flask_front
from time import sleep
import requests
import threading


def working_loop():
    url = URL_WEB + "/rest-users/"
    while True:
        sleep(15)
        requests.put(url=url)


@flask_front.route('/', methods=['POST'])
def index():
    request_info = request.json
    data = validate_request(request_info)
    if data is None:
        return {"ok": True}
    return data


def set_webhook():
    requests.post(SET_WEBHOOK_URL, DATA)


if __name__ == '__main__':
    try:
        set_webhook()
        x = threading.Thread(target=working_loop)
        x.start()
        flask_front.run(host='0.0.0.0', port=5001)
    except KeyboardInterrupt:
        print("End of program!")