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


# class Gateway:

    # def __init__(self):
    #     self.app = Flask(__name__)

# Initiating API Server
app = Flask(__name__)

def extract_user_data(jwt_token):

    # Temporary stub
    # Parsing JWT

    user_name = "Lisa"
    user_token = "xxx"

    return user_name, user_token

def user_token_validator(token_to_validate):
    # Authotization method - temporary stub
    return True


@app.route("/receive_prompt", methods=['POST'])
def receive_user_prompt():
    request_content = request.get_json()

    try:
        user_data = request_content['user_data']  # User name & token as JWT
        user_prompt = request_content['user_prompt']

    except KeyError:
        return {"error": "Invalid Log In request"}

    # Getting user name and user token - the former is used to verify the current user is authorized
    user_name, user_token = extract_user_data(user_data)
    token_validation = user_token_validator(user_token)

    if token_validation is False:
        logging.warning(f"Gateway: authorization issue - user {user_name} tried to use"
                        f" an invalid access token {user_token}")
        return {"error": "Access denied"}

    logging.info(f"Gateway: Forwarding to the model {user_name} : {user_prompt}")
    # return {"status": "ok"}

    # Forwarding user name and user prompt to the model
    return MiddleLayer.handle_user_prompt(user_name, user_prompt)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

