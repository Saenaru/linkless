# Сокращение ссылок и рассчёт кликов. / Shortening links and calculating clicks.

## Оглавление / Table of Contents

- [Русский](#русский)
- [English](#english)

---

## Русский

Скрипт сокращает ссылки через интерфейс vk.cc и считает статистику кликов.

## Как установить


1.Python3 должен быть уже установлен. 

2.Получить [сервисный токен приложения](https://id.vk.com/about/business/go/docs/ru/vkid/latest/vk-id/connection/tokens/service-token).

3.Это приложение использует файл .env для хранения конфиденциальных и конфигурируемых параметров настройки.

В корневом каталоге проекта создайте файл «token.env», и укажите токен приложения в формате КЛЮЧ=значение. Пример:

```plaintext
API_VK_TOKEN=***
```

Храните `.env` в безопасности: Убедитесь, что файл .env не попадает в систему контроля версий, как например Git, добавив его в .gitignore.

## Использование

Выполните команду для установки зависимостей:
```bash
pip install -r requirements.txt
```
Для запуска проекта используйте команду:

```bash
python linkless.py ваша_ссылка
```

## Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).

---

## English

The script shortens links via the vk.cc interface and calculates click statistics.

## How to install


1.Python3 should already be installed.

2.Get [application service token](https://id.vk.com/about/business/go/docs/ru/vkid/latest/vk-id/connection/tokens/service-token).

3.This application uses an .env file to store sensitive and configurable settings.

In the root directory of the project, create a file “token.env”, and specify the application token in the KEY=value format. Example:

```plaintext
API_VK_TOKEN=***
```

Keep `.env` safe: Make sure the .env file doesn't end up in a version control system like Git by adding it to .gitignore.

## Usage

Run the command to install dependencies:
```bash
pip install -r requirements.txt
```
To run the project use the command:

```bash
python linkless.py your_link
```

## Project Goals

This code was written for educational purposes as part of an online course for web developers at [dvmn.org](https://dvmn.org/).