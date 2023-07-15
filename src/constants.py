import os

SUBSCRIPTION_SERVICE_HOST = os.environ["SUBSCRIPTION_SERVICE_HOST"]

CREATE_URL = f"http://{SUBSCRIPTION_SERVICE_HOST}:8080/subscriptions/create"
GET_URL = f"http://{SUBSCRIPTION_SERVICE_HOST}:8080/" + "subscriptions/{user_id}"
REMOVE_URL = f"http://{SUBSCRIPTION_SERVICE_HOST}:8080/" + "subscriptions/{user_id}/telegram"
