import logging

try:
    from Leonid.chatbot import ChatBot

except ModuleNotFoundError:
    from chatbot import ChatBot

logging.basicConfig(level=logging.INFO)

# TO DO:
#
# 1. Think how can we STOP an instance in case the dialog is terminated (to save resources)
# Example:
# import llama_cpp_python as llama
# model = llama.Llama("path/to/model.gguf")
# model.stop()
# del model
# Recommended: stop instance mapped to user that has disconnected



class MiddleLayer:
    """
    This class serves as a mediator between Gateway (REST API) and ChatBot -
    it redirects user prompts to the right ChatBot instance and starts new ChatBot
    instances when required.
    """

    users_conversations = {}

    @classmethod
    def handle_user_prompt(cls, user_name, user_prompt):
        """
        This method handles user input. The input can come from one or several users.
        If new user wishes to start a conversation, a new ChatBot created for that user
        and stored against his name in 'users_conversations' dict.
        I a user that has already a conversation with one of the ChatBot instances
        sends a prompt, it is forwarded to the relevant instance (mapped against his name in dict).
        The method returns the output generated by the ChatBot instance
        :param user_name: str
        :param user_prompt: ChatBot instance
        :return: str
        """

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

    @classmethod
    def user_disconnection_internal_handling(cls, user_name):
        # TO DO
        pass


# if __name__ == "__main__":
#     user_lisa = "Lisa"
#     user_avi = "Avi"
#
#     print(MiddleLayer.handle_user_prompt(user_lisa, "Hello. My name is Lisa."))
#     print(MiddleLayer.handle_user_prompt(user_avi, "Hello. My name is Avi."))
#
#     print(MiddleLayer.handle_user_prompt(user_lisa, "Imagine you have 3 coins in your hand"))
#     print(MiddleLayer.handle_user_prompt(user_avi, "Imagine you have 5 stones in your hand"))
#
#     print(MiddleLayer.handle_user_prompt(user_lisa, "Add 2 more coins."))
#     print(MiddleLayer.handle_user_prompt(user_avi, "Add 5 more stones."))
#
#     print(MiddleLayer.handle_user_prompt(user_lisa, "How many coins do you have?"))
#     print(MiddleLayer.handle_user_prompt(user_avi, "How many stones do you have?"))

