import os

SUBSCRIPTION_SERVICE_HOST = os.environ["SUBSCRIPTION_SERVICE_HOST"]

CREATE_URL = f"https://{SUBSCRIPTION_SERVICE_HOST}/subscriptions/create"
GET_URL = f"https://{SUBSCRIPTION_SERVICE_HOST}/" + "subscriptions/{user_id}"
REMOVE_URL = f"https://{SUBSCRIPTION_SERVICE_HOST}/" + "subscriptions/{user_id}/telegram"
