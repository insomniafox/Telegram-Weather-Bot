import os

from dotenv import load_dotenv

load_dotenv()

WEATHER_MAP_API_KEY = os.getenv('WEATHER_MAP_API_KEY')
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
