#!/usr/bin/python3

from llm_openai import *
from web_scrape import *


def main():
    shopping_functions_dict = {
    'amazon': amazon_search,
    'ebay': ebay_search,
    'bestbuy': bestbuy_search,
    }


    print("I am an AI assistant for ...\nHow can I help you?")
    user_question = input()
    prompt = f"What are the key categories to consider when selecting {user_question}? list them, don't explain.\
        i want response in this format Categories: <numbered_list_of_categories> Then in one word, tell me what product we are talking about"

    response = gpt_caller(prompt)

    product_name, requirements = product_requirements_parser(response)
    requirement_lines = []

    for requirement in requirements:
        print(
            f"\nwhat {requirement} do you want\nType the value, press enter. if none, press enter: ")
        user_choice = input()
        if user_choice:
            requirement_lines.append(f'{requirement} = {user_choice}')

    specification = ", ".join(requirement_lines)

    product_prompt = f"which kind of {product_name} have this kind of specifications or come close, {specification} list them if not one and don't explain.\
        i want response in a list"

    products = gpt_caller(product_prompt)

    product_suggestions = products_parser(products)
    user_product_list = user_product_option(product_suggestions)
    user_store_list = user_store_option()

    for product in user_product_list:
        for store in user_store_list:
            shopping_functions_dict[store](product)


if __name__ == "__main__":
    main()