# Leonid_The_Chatbot

### General

Chat bot based on <b>Vicuna</b> model (ggml-vicuna-13b-4bit-rev1.bin) and llama-cpp-python library. 
It receives you prompt via HTTP request (listening on port 5001), the response contains bot's response,
as a text. 

The conversation relies on the initial context, which can be introduced through an HTTP request. 
With each new replica added to the context, the conversation remains coherent and maintains its continuity.

The chat bot has the capacity to concurrently manage multiple conversations. 
When a new user addresses the bot, a fresh bot instance is generated.
If the bot receives notification (via an API request) that the user has terminated the connection, 
the instance is gracefully shut down.

### API documentation

All the requests are HTTP POST request (see examples attached).

1. <b>Prompt sending</b>: the request should be sent to <b>http://localhost:5001/receive_prompt</b> 
(providing the service is running on local host, if it isn't - just insert your host name).

It should contain two properties:

+ <b>user_data</b> - user name and user token packed in a JWT. The user's name and user token are encoded within 
a JSON Web Token (JWT). The user's name plays a crucial role because the chat bot has the capability to engage in 
multiple concurrent conversations while preserving the context of each. For instance, if you address the bot as 'John',
it will exclusively employ the context from that specific conversation when crafting its responses, addressing you as 
'John' in subsequent interactions within that conversation.

For ex. payload = {"user_name": "Lisa", "user_token": "token"} = > convert to JWT = > use as 'user_data' in the request

At the moment user token isn't validated.

+ <b>user_prompt</b> - your prompt as string. 


2.<b>Content injection</b>: the request should be sent to <b>http://localhost:5001/inject_context</b>.

Should contain:

+ <b>user_data</b> - same as above. Note that the context will be injected into the conversation
with the selected user and won't affect other conversations. 

+ <b>injected_context</b> - the context you want to inject

3.<b>User disconnection</b> - notifying the chat bot on user disconnection .
should be sent to <b>http://localhost:5001/user_disconnection</b>.
The chat bot instance that was engaged in a conversation with that user will be removed.

Should contain:

+ <b>user_data</b> - same as above.















### Important
Please note: while the model itself (almost 8 GB) won't be uploaded to Git, it will be a part of my 
Docker container. If you are interested in running the chat bot in a Docker container I suggest 
you download the model  from <b>https://huggingface.co/eachadea/legacy-ggml-vicuna-13b-4bit/tree/main</b> 
and place it in  the 'models' folder (create it in 'Leonid', './Leonid/models') and build the image. 

The PATH to the model is  taken from an ENV. VARIABLE (MODEL_PATH), 
and you will be able to add YOUR path to the model under that env. var. 
If you wan't to use another model please make sure that the version of llama-cpp-python is compatible with it.

Right now the MVP can run in Docker container and forward user prompts from several different users to the model (POST requests to port 5001). 
