import requests
import yaml
from flask import Flask, request, abort, jsonify
from requests.utils import requote_uri

from alert import PrometheusAlert

config_file_path = '/etc/telegram-alert-bot/config.yml'

with open(config_file_path) as f:
    config = yaml.load(f, Loader=yaml.FullLoader)

token = config['token']
chat_id = config['chat_id']
proxies = config['proxies']

app = Flask(__name__)


@app.route('/', methods=['GET'])
def status():
    return jsonify({'status': 0}), 200


@app.route("/", methods=['POST'])
def send():
    if not request.json:
        abort(400)
    msg_chat = PrometheusAlert(request.json).plain()
    msg_url = 'https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}'.format(token, chat_id, msg_chat)
    msg_url = requote_uri(msg_url)
    response = requests.get(msg_url, proxies=proxies)
    if response.status_code != 200:
        abort(500)
    return '', 204


if __name__ == '__main__':
    app.run(host='0.0.0.0')
