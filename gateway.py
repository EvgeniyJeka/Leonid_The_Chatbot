import logging
from flask import Flask, request
import jwt

try:
    from midlayer import MiddleLayer

except ModuleNotFoundError:
    from .midlayer import MiddleLayer

logging.basicConfig(level=logging.INFO)


class GatewayApp:
    def __init__(self):
        self.app = Flask(__name__)

        @self.app.route("/receive_prompt", methods=['POST'])
        def receive_user_prompt():
            request_content = request.get_json()

            try:
                user_data = request_content['user_data']  # User name & token as JWT
                user_prompt = request_content['user_prompt']

            except KeyError:
                return {"error": "Invalid Log In request"}

            # Getting user name and user token - the former is used to verify the current user is authorized
            user_name, user_token = self.extract_user_data(user_data)
            token_validation = self.user_token_validator(user_token)

            if token_validation is False:
                logging.warning(f"Gateway: authorization issue - user {user_name} tried to use"
                                f" an invalid access token {user_token}")
                return {"error": "Access denied"}

            logging.info(f"Gateway: Forwarding to the model {user_name} : {user_prompt}")
            # return {"test": "ok"}

            # Forwarding user name and user prompt to the model
            return MiddleLayer.handle_user_prompt(user_name, user_prompt)

    def run(self, host='0.0.0.0', port=5001):
        self.app.run(host=host, port=port)

    def extract_user_data(self, jwt_token):

        # Decode the JWT without verifying the signature
        decoded_payload = jwt.decode(jwt_token, algorithms=["HS256"], options={"verify_signature": False})
        logging.info(f"Gateway: decoded user token {decoded_payload}")

        return decoded_payload['user_name'], decoded_payload['user_token']

    def user_token_validator(self, token_to_validate):
        # Authorization method - temporary stub
        return True


if __name__ == "__main__":
    gateway_app = GatewayApp()
    gateway_app.run()
