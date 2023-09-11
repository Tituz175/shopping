#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup

header = ({'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
          'Accepted-Language': 'en-US,en;q=0.5'})

def amazon_search(product):
    url = f'https://www.amazon.com/s?k={product}'
    response = requests.get(url, headers=header)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'lxml')
        print(f"Starting with {product}\n")

        try:
            for span in soup.find_all('div', class_='a-section a-spacing-small a-spacing-top-small'):
                product_name = span.find(
                    'span', class_='a-size-medium a-color-base a-text-normal')
                rating = span.find("span", class_="a-icon-alt")
                price = span.find("span", class_="a-offscreen")
                delivery_date = span.find(
                    "span", class_="a-color-base a-text-bold")
                product_url = span.find(
                    'a', class_="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal")
                product_name_lowercase = f"{product.split(' ')[0].lower()} {product.split(' ')[1].lower()}"

                if product_name and ("battery" in product_name.text.lower() or "screen" in product_name.text.lower()):
                    continue

                if all((product_name, rating, price, delivery_date)) and product_name_lowercase in product_name.text.lower():
                    print(
                        f"{product_name.text}\n{rating.text}\n{price.text}\n{delivery_date.text}\nwww.amazon.com{product_url.get('href')}\n")
                    break
        except:
            pass
    else:
        print(
            f"Failed to retrieve data for {product}. Status code: {response.status_code}")


def ebay_search(product):
    url = f"https://www.ebay.com/sch/i.html?_from=R40&_nkw={product}&_sacat=0&rt=nc&LH_ItemCondition=1000"
    response = requests.get(url, headers=header)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'lxml')

        try:
            for div in soup.find_all('div', class_="s-item__info clearfix"):
                product_name = div.find("div", class_="s-item__title")
                price = div.find("span", class_="s-item__price")
                product_url = div.find("a", class_="s-item__link")
                product_name_lowercase = f"{product.split(' ')[0].lower()} {product.split(' ')[1].lower()}"

                if product_name and ("battery" in product_name.text.lower() or "screen" in product_name.text.lower()):
                    continue

                if all((product_name, price)) and product_name_lowercase in product_name.get_text().lower():
                    print(
                        f"{product_name.text}\n{price.text}\n{product_url.get('href')}\n")
                    break
        except:
            pass
    else:
        print(
            f"Failed to retrieve data for {product}. Status code: {response.status_code}")


def bestbuy_search(product):
    url = f"https://www.bestbuy.com/site/searchpage.jsp?id=pcat17071&st={product}"
    response = requests.get(url, headers=header)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'lxml')

        try:
            for div in soup.find_all("div", class_="list-item lv"):
                    product_name = div.find('h4', class_='sku-title').text
                    product_price = div.find(
                        'div', class_="priceView-hero-price priceView-customer-price").text.split("$")[-1]
                    product_rating = div.find('p', class_="visually-hidden").text
                    product_url = f"www.bestbuy.com{div.find('h4', class_ = 'sku-title').find('a').get('href')}"

                    if all((product_name, product_rating, product_price, product_url)):
                        print(
                            f"{product_name}\n${product_price}\n{product_rating}\n{product_url}\n")
                        break
        except:
            pass
    else:
        print(
            f"Failed to retrieve data for {product}. Status code: {response.status_code}")