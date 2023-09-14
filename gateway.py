import logging
import time
from datetime import datetime, timedelta
from flask import Flask, request
import os
import jwt

try:
    from midlayer import MiddleLayer

except ModuleNotFoundError:
    from .midlayer import MiddleLayer

logging.basicConfig(level=logging.INFO)


class Gateway:

    def __init__(self):
        self.app = Flask(__name__)

    def run(self):

        @self.app.route("/user/receive_prompt", methods=['POST'])
        def receive_user_prompt():
            request_content = request.get_json()

            try:
                user_data = request_content['user_data']  # User name & token as JWT
                user_prompt = request_content['user_prompt']

            except KeyError:
                return {"error": "Invalid Log In request"}

            # Decode user name
            # Decode user token
            # Validate token (T.B.D.) - > If validated forward user prompt - > return model output.

