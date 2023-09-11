#!!/usr/bin/python3
import gradio as gr
from llm_openai import *


# print("I am an AI shopping assistant ...\nHow can I help you?")
# user_question = input()
# prompt = f"What are the key categories to consider when selecting {user_question}? list them, don't explain.\
#         i want response in this format Categories: <numbered_list_of_categories> Then in one word, tell me what product we are talking about"

# response = gpt_caller(prompt)

# product_name, requirements = product_requirements_parser(response)
# requirement_lines = []

# for requirement in requirements:
#         print(
#             f"\nwhat {requirement} do you want\nType the value, press enter. if none, press enter: ")
#         user_choice = input()
#         if user_choice:
#             requirement_lines.append(f'{requirement} = {user_choice}')

# specification = ", ".join(requirement_lines)

# product_prompt = f"which kind of {product_name} have this kind of specifications or come close, {specification} list them if not one and don't explain.\
#         i want response in a list"

# products = gpt_caller(product_prompt)


def prompt_new(name):
    prompt = f"What are the key categories to consider when selecting {name}? list them, don't explain.\
            i want response in this format Categories: <numbered_list_of_categories> Then in one word, tell me what product we are talking about"

    response = gpt_caller(prompt)

    product_name, requirements = product_requirements_parser(response)
    return [requirements, product_name]
    return [", ".join(requirements)]


def greet(name):
    greeting = f"Hello {name}"
    return greeting


state = "start"

with gr.Blocks() as demo_prompt:
    # name = gr.Textbox(label="Name")
    # output = gr.Textbox(label="Output Box")
    # prompt_btn = gr.Button("Prompt")
    # if state == "prompt":
    #     prompt_btn.click(fn=greet, inputs=name, outputs=output, api_name="greet")
    # else:
    #     state = "prompt"
    #     prompt_btn.click(fn=prompt, inputs=name, outputs=output, api_name="prompt")
    chatbot = gr.Chatbot()
    message = gr.Textbox(label="Message")
    state = gr.State()
    submit_btn = gr.Button("Submit")
    submit_btn.click(fn=prompt_new, inputs=message, outputs=chatbot)


# with gr.Blocks() as demo:
#     name = gr.Textbox(label="Name")
#     output = gr.Textbox(label="Output Box")
#     greet_btn = gr.Button("Greet")
#     greet_btn.click(fn=greet, inputs=name, outputs=output, api_name="greet")


if __name__ == "__main__":
    demo_prompt.launch()
    # demo.launch()
