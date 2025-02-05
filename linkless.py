import os
import requests
from dotenv import load_dotenv


def shorten_link(token, url):
    url_link = "https://api.vk.com/method/utils.getShortLink"
    params = {
        "access_token": token,
        "v": "5.199",
        "url": url,
    }
    response = requests.get(url_link, params=params)
    response.raise_for_status()
    data = response.json()
    return data["response"]["short_url"]


def count_clicks(token, short_url):
    url_stats = "https://api.vk.com/method/utils.getLinkStats"
    key = short_url.split('/')[-1]
    params = {
        "access_token": token,
        "key": key,
        "interval": "forever",
        "v": "5.199",
    }
    response = requests.get(url_stats, params=params)
    response.raise_for_status()
    data = response.json()
    if "response" in data and "stats" in data["response"] and data["response"]["stats"]:
        return data["response"]["stats"][0]["views"]
    else:
        return 0


def is_short_link(url):
    short_prefix = "https://vk.cc/"
    return url.startswith(short_prefix)


def main():
    load_dotenv("token.env")
    token = os.getenv("TOKEN")
    url_user = input("Введите ссылку: ")
    try:
        if is_short_link(url_user):
            clicks = count_clicks(token, url_user)
            print('Количество кликов по ссылке: ', clicks)
        else:
            response = requests.get(url_user)
            response.raise_for_status()
            short_link = shorten_link(token, url_user)
            print('Сокращённая ссылка: ', short_link)
            short_link = shorten_link(token, url_user)
    except requests.exceptions.HTTPError as error:
        print(f"Данные с сервера недоступны:\n{error}")


if __name__ == "__main__":
    main()
