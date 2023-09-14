from chatbot import ChatBot
import logging

logging.basicConfig(level=logging.INFO)


class MiddleLayer:

    users_conversations = {}

    @classmethod
    def handle_user_prompt(cls, user_name, user_prompt):

        if user_name not in cls.users_conversations.keys():
            # Initiate a new conversation, a new ChatBot instance
            logging.info(f"Middle Layer: initiating a new conversation for user {user_name}")
            new_conversation_partner = ChatBot()
            cls.users_conversations[user_name] = new_conversation_partner
            return new_conversation_partner.send_prompt(user_prompt)

        else:
            # Forwarding user prompt to the related ChatBot instance
            logging.info(f"Middle Layer: continuing a conversation with user {user_name}")
            conversation_partner = cls.users_conversations[user_name]
            return conversation_partner.send_prompt(user_prompt)


if __name__ == "__main__":
    user_lisa = "Lisa"
    user_avi = "Avi"

    print(MiddleLayer.handle_user_prompt(user_lisa, "Hello. My name is Lisa."))
    print(MiddleLayer.handle_user_prompt(user_avi, "Hello. My name is Avi."))

    print(MiddleLayer.handle_user_prompt(user_lisa, "Take one silver coin."))
    print(MiddleLayer.handle_user_prompt(user_avi, "Take three silver coins."))

    print(MiddleLayer.handle_user_prompt(user_lisa, "Take 2 silver more coins."))
    print(MiddleLayer.handle_user_prompt(user_avi, "Take 5 silver more coins"))

    print(MiddleLayer.handle_user_prompt(user_lisa, "How many coins you took?"))
    print(MiddleLayer.handle_user_prompt(user_avi, "How many coins you took?"))

