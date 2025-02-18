import os
import requests
from urllib.parse import urlparse
from dotenv import load_dotenv
import argparse


def shorten_link(token, url):
    link_url = "https://api.vk.com/method/utils.getShortLink"
    params = {
        "access_token": token,
        "v": "5.199",
        "url": url,
    }
    response = requests.get(link_url, params=params)
    response.raise_for_status()
    data = response.json()
    return data["response"]["short_url"]


def count_clicks(token, short_url):
    stats_url = "https://api.vk.com/method/utils.getLinkStats"
    parsed_url = urlparse(short_url)
    key = parsed_url.path.lstrip('/').split('/')[-1]
    params = {
        "access_token": token,
        "key": key,
        "interval": "forever",
        "v": "5.199",
    }
    response = requests.get(stats_url, params=params)
    response.raise_for_status()
    data = response.json()
    if "response" in data and "stats" in data["response"] and data["response"]["stats"]:
        return data["response"]["stats"][0]["views"]
    else:
        return 0


def is_short_link(token, url):
    parsed_url = urlparse(url)
    key = parsed_url.path.lstrip('/').split('/')[-1]
    stats_url = "https://api.vk.com/method/utils.getLinkStats"
    params = {
        "access_token": token,
        "key": key,
        "v": "5.199",
    }

    response = requests.get(stats_url, params=params)
    response.raise_for_status()
    data = response.json()
    return "response" in data and "stats" in data["response"]


def main():
    load_dotenv("token.env")
    parser = argparse.ArgumentParser(description="Утилита для сокращения ссылок и подсчета кликов.")
    parser.add_argument("url", nargs='?', help="URL ссылка, которую нужно обработать")
    args = parser.parse_args()
    user_url = args.url
    token = os.environ["API_VK_TOKEN"]
    if args.url:
        user_url = args.url
    else:
        user_url = input("Введите ссылку: ")
    try:
        if is_short_link(token, user_url):
            clicks = count_clicks(token, user_url)
            print('Количество кликов по ссылке: ', clicks)
        else:
            short_link = shorten_link(token, user_url)
            print('Сокращённая ссылка: ', short_link)
    except requests.exceptions.HTTPError as error:
        print(f"Данные с сервера недоступны:\n{error}")


if __name__ == "__main__":
    main()
