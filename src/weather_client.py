from typing import Optional
from urllib.parse import urlencode

import httpx
import structlog

from exceptions import WeatherAPIException
from variables import WEATHER_MAP_API_KEY

logger = structlog.get_logger(__name__)


class WeatherClient:
    client = httpx.AsyncClient(verify=False)
    api_key = WEATHER_MAP_API_KEY
    base_url = 'http://api.openweathermap.org/data/2.5/weather'

    @classmethod
    async def get_weather(cls, city: str, lang: Optional[str] = None) -> str | dict:
        lang = lang if lang else 'ru'
        response = await cls._request(
            method='GET',
            url=cls.base_url,
            query_params={
                'q': city,
                'appid': cls.api_key,
                'units': 'metric',
                'lang': lang
            }
        )
        weather = {
            "temperature": response["main"]["temp"],  # Температура
            "humidity": response["main"]["humidity"],  # Влажность
            "description": response["weather"][0]["description"]  # Описание погоды
        }
        return weather

    @classmethod
    async def _request(
        cls,
        method: str,
        url: str,
        data: dict | None = None,
        query_params: dict | None = None,
        headers: dict | None = None,
    ) -> dict:

        if query_params:
            url = url + '?' + urlencode(query_params)

        try:
            response = await cls.client.request(
                method=method,
                url=url,
                json=data,
                headers=headers,
                timeout=10
            )
        except (httpx.TimeoutException,) as e:
            logger.error('Error occured!', error=str(e))
            raise WeatherAPIException("Ошибка при отправке запроса.")
        cls._check_response(response)
        response = response.json()
        logger.info('Response', response=response)
        return response

    @staticmethod
    def _check_response(response: httpx.Response):
        if response.status_code in (200, 201, 202):
            return

        if response.status_code == 401:
            logger.error('Unauthorized.', error=response.text)
            raise WeatherAPIException("Не достаточно прав.")

        if response.status_code == 404:
            logger.error('City not found.', error=response.text)
            raise WeatherAPIException("Город не найден.")

        if 400 <= response.status_code < 500:
            logger.error('Error occured!', error=response.text)
            raise WeatherAPIException("Что-то пошло не так. Попробуйте позже.")

        if response.status_code >= 500:
            raise WeatherAPIException("Произошла внутренняя ошибка.")
