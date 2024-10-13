
# Telegram Weather Bot

Этот Telegram бот предназначен для получения текущей погоды по названию города. Он использует сервис OpenWeatherMap для получения данных о температуре, влажности и описания погоды.

## Возможности
- Получение текущей погоды (температура, влажность, описание) для любого города.
- Поддержка двух языков: русский и английский.
- Команда для смены языка в любой момент.

## Требования
- [Python 3.11+](https://www.python.org/downloads/)
- [Telegram Bot API](https://core.telegram.org/bots#botfather)
- [OpenWeatherMap API](https://home.openweathermap.org/users/sign_up)
- Docker (для использования Docker Compose)

## Установка

### Локальная установка:

1. Клонируйте репозиторий:

   ```bash
   git clone https://github.com/insomniafox/Telegram-Weather-Bot
   cd Telegram-Weather-Bot/
   ```

2. Установите зависимости:

   ```bash
   pip install -r requirements.txt
   ```

3. Создайте файл `.env` и добавьте туда ваш Telegram Bot Token и OpenWeatherMap API ключ:

   ```env
   TELEGRAM_BOT_TOKEN=your_telegram_bot_token
   WEATHER_MAP_API_KEY=your_openweathermap_api_key
   ```

4. Запустите бота:

   ```bash
   python src/main.py
   ```

### Использование Docker:

1. Убедитесь, что Docker и Docker Compose установлены.
2. Создайте файл `.env` в корне проекта и добавьте туда ваш Telegram Bot Token и OpenWeatherMap API ключ:

   ```env
   TELEGRAM_BOT_TOKEN=your_telegram_bot_token
   OPENWEATHER_API_KEY=your_openweathermap_api_key
   ```

3. Запустите приложение с помощью Docker Compose:

   ```bash
   docker-compose up --build
   ```

## Команды бота

- `/start` — приветствие и выбор языка.
- `/change_language` — позволяет сменить язык общения с ботом.
- Отправьте название города (на русском или английском языке), чтобы получить информацию о погоде.

## Использование

После запуска бота в Telegram:

1. Введите команду `/start`, чтобы получить приветственное сообщение и выбрать язык.
2. Выберите язык (Русский или English).
3. Введите название города (например, "Москва" или "New York"), чтобы получить информацию о текущей погоде в этом городе.

## Пример использования

```
Погода в городе Москва:
Температура: 5°C
Влажность: 80%
Описание: облачно с прояснениями
```

## Инструменты разработки

- [OpenWeatherMap API](https://openweathermap.org/)
- [Aiogram](https://docs.aiogram.dev/)

## Лицензия

Этот проект лицензируется на условиях MIT License.
