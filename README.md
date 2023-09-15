# Leonid_The_Chatbot
Chat bot based on vicuna model and llama-cpp-python library. 

In progress, early stages.

Please note: while the model itself (almost 8 GB) won't be uploaded to Git, it will be a part of my Docker container.
If you are interested in running the chat bot in a Docker container I suggest you download the model from <b>https://huggingface.co/eachadea/legacy-ggml-vicuna-13b-4bit/tree/main</b>
and place it in the 'models' folder under this project. Although right now the PATH to the model is hardcoded, eventually it will be taken from an ENV. VARIABLE (PATH_TO_MODEL), 
and you will be able to add YOUR path to the model under that env. var. 
