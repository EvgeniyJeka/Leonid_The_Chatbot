from llama_cpp import Llama
import logging
import json

logging.basicConfig(level=logging.INFO)

MAX_TOKENS_TOTAL_CONVERSATION = 15000
MAX_TOKENS_TO_GENERATE = 100

# TO DO:
# 1. Model path - to env. variable, take it from there

class ChatBot:

    context = "Your name is Leonid. Lisa and Avi are developers, they are debugging code, assist them, do what they ask."
    llm = None

    def __init__(self):
        logging.info("Loading the model..")
        self.llm = Llama(model_path="./models/ggml-vicuna-13b-4bit-rev1.bin", n_ctx=MAX_TOKENS_TOTAL_CONVERSATION)
        logging.info("Model loaded.")

    def send_prompt(self, user_input):

        output = self.llm(f"Context: ({self.context}). Question: {user_input} Answer:",
                          max_tokens=MAX_TOKENS_TO_GENERATE,
                          stop=["\n", "Question:", "Q:"],
                          echo=True)

        text_line = output['choices'][0]['text']
        logging.info(f"Context: {text_line}")

        text_line_list = text_line.split("Answer:")
        response_returned = text_line_list[-1]

        adding_to_conversation_context = f" Question: {user_input}, Answer: {response_returned}"
        self.context = self.context + adding_to_conversation_context

        return response_returned


# if __name__ == "__main__":
#     bot = ChatBot()
#     print(bot.send_prompt("Hello. How are you?"))
#     print(bot.send_prompt("Imagine you have 3 coins in your hand"))
#     print(bot.send_prompt("Add 2 more coins"))
#     print(bot.send_prompt("How many coins are now in your hand?"))



