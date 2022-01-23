import requests
import json
from .decorators import start_new_thread

url = 'http://0.0.0.0:8001/order'


@start_new_thread
def create_handler(instance, payload):
    r = requests.get(url + '/' + str(instance.label))
    if r.status_code == 404:
        requests.post(url, data=payload)


@start_new_thread
def update_handler(instance, payload):
    r = requests.get(url + '/' + str(instance.label))
    if r.status_code == 200 and json.loads(r.content).get('status') != instance.status:
        requests.patch(url + '/' + str(instance.label), data=payload)
