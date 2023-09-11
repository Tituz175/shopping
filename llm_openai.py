#!/usr/bin/python3
import os
from dotenv import load_dotenv
import openai

load_dotenv()
api_key = os.environ.get('API_KEY')

openai.api_key = api_key

def gpt_caller(str=None):
    if str is None:
        return "Kindly ask your question"

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": f'{str}'},
        ]
    )
    return completion


def product_requirements_parser(response):
    response = response.choices[0].message.content
    product_response = response.split(':')
    product_name = product_response.pop(-1).strip(" ")
    numbered_requirements = product_response[1].split('\n')[1:-2]
    requirements = [line.strip('1234567890. ')
                    for line in numbered_requirements]

    requirements = [item for item in requirements if item != ""]
    return product_name, requirements


def products_parser(products):
    products = products.choices[0].message.content

    product_suggestions = [line.strip('1234567890.-() ')
                           for line in products.split('\n')]
    print("Below are the products i will recommend:\n")
    for i in range(len(product_suggestions)):
        print(f'{i+1}. {product_suggestions[i]}\n')

    return product_suggestions


def user_product_option(product_suggestions):
    user_product_option = input(
        "Kindly input the number(s) separated by comma of the product you would like to know more about then press enter\nif all press enter: ")
    if user_product_option:
        user_product_option = user_product_option.split(',')
        user_product_list = [product_suggestions[int(product)-1]
                             for product in user_product_option
                             if int(product)-1 < len(product_suggestions)]

    else:
        user_product_option = []
        for i in range(len(product_suggestions)):
            user_product_option.append(i)
        user_product_list = [product_suggestions[int(
            product)] for product in user_product_option]
    return user_product_list


def user_store_option():
    store_list = ["amazon", "ebay", "bestbuy"]
    print("Kindly select out of these store options(e.g. 1 for Amazon)\n")
    for i in range(len(store_list)):
        print(f'{i+1}. {store_list[i]}\n')
    user_store_option = input(
        "if more than one, seperate options with comma\nif all press enter: ")
    if len(user_store_option) != 0:
        user_store_option = user_store_option.split(',')
        user_store_list = [store_list[int(product)-1]
                           for product in user_store_option
                           if int(product)-1 < len(store_list)]

    else:
        user_store_list = store_list.copy()
    return (user_store_list)
