import os

import requests
from dotenv import load_dotenv

load_dotenv()

user = os.environ['PUSHOVER_USER']
token = os.environ['PUSHOVER_TOKEN']
url = os.environ['PUSHOVER_URL']


def notify(message):
    print(f"Sending notification to Pushover: {message}")
    payload = {"user": user, "token": token, "message": message}
    requests.post(url, data=payload)

