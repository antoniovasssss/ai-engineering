# import os
# from dotenv import load_dotenv
# from openai import OpenAI
# import gradio as gr

# # Load environment variables in a file called .env
# # Print the key prefixes to help with any debugging

# load_dotenv(override=True)
# openai_api_key = os.getenv('OPENAI_API_KEY')

# knowledge= {
# "python":"Python is a programming language.",
# "ai":"AI means Artificial Intelligence.",
# }

# def get_answer(query):
#     query = query.lower()
#     return knowledge.get(query,"I don't know that yet.")

# def chatbot(user_input,history):
#     response=get_answer(user_input)
#     history.append((user_input,response))
#     return "", history

import gradio as gr

knowledge= {
"python":"Python is a programming language.",
"ai":"AI stands for Artificial Intelligence.",
"ml":"Machine Learning is a subset of AI."
}

def get_answer(query):
    query=query.lower()
    return knowledge.get(query,"Sorry, I don't know that.")

def chatbot(user_input,history):
    response=get_answer(user_input)
    history.append((user_input,response))
    return "",history

with gr.Blocks() as demo:
     gr.Markdown("# 🤖 Knowledge Bot")

     chatbot_ui=gr.Chatbot()
     msg=gr.Textbox(placeholder="Ask something...")

     msg.submit(chatbot, [msg,chatbot_ui], [msg,chatbot_ui])

     demo.launch()