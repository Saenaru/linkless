import os
import requests
from urllib.parse import urlparse
from dotenv import load_dotenv


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
    key = short_url.split('/')[-1]
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
    return urlparse(url).netloc == "vk.cc"


def main():
    load_dotenv("token.env")
    token = os.environ["API_VK_TOKEN"]
    user_url = input("Введите ссылку: ")
    try:
        if is_short_link(token, user_url):
            clicks = count_clicks(token, user_url)
            print('Количество кликов по ссылке: ', clicks)
        else:
            response = requests.get(user_url)
            response.raise_for_status()
            short_link = shorten_link(token, user_url)
            print('Сокращённая ссылка: ', short_link)
    except requests.exceptions.HTTPError as error:
        print(f"Данные с сервера недоступны:\n{error}")


if __name__ == "__main__":
    main()
