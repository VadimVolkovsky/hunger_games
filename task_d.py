# D. Реализовать функцию, которая замеряет время на
# исполнение 100 запросов к адресу: http://httpbin.org/delay/3.
# Запросы должны выполняться асинхронно.
# Допускается написание вспомогательных функций и использование
# сторонних библиотек.
# Результат замера времени выводит в консоль.
# Ожидаемое время не должно превышать 10 секунд.


import asyncio
import logging
from datetime import datetime
from http import HTTPStatus

import aiohttp

from services.user_agent_generator import user_agent_rotator
from testdata import TASK_D_REQUESTS_AMOUNT as REQUESTS_AMOUNT
from testdata import TASK_D_URL as URL

timeout = aiohttp.ClientTimeout(total=9)
headers = {
    "User-Agent": "default_value"
}
statuses = {
    HTTPStatus.OK: 0,
    HTTPStatus.BAD_GATEWAY: 0,
    HTTPStatus.GATEWAY_TIMEOUT: 0
}


async def task():
    """Функция создания асинхронной задачи"""
    async with aiohttp.ClientSession() as session:
        try:
            headers["User-Agent"] = user_agent_rotator.get_random_user_agent()
            response = await session.get(URL, headers=headers, timeout=timeout)
            statuses[response.status] += 1
        except TimeoutError:
            pass


async def async_execute():
    """Генератор асинхронных задач"""
    tasks = [
        asyncio.ensure_future(task()) for _ in range(REQUESTS_AMOUNT)
    ]
    await asyncio.wait(tasks)


def send_async_requests():
    """Асинхронная отправка запросов на указанный URL"""
    logging.info(
        f'Запуск асинхронной отправки '
        f'{REQUESTS_AMOUNT} запросов к сайту: {URL}'
    )
    start_time = datetime.now()
    asyncio.run(async_execute())
    end_time = datetime.now()
    logging.info(f'Итоговое время выполнения: {end_time - start_time} секунд.')
    logging.info(f'Успешных запросов: {statuses[HTTPStatus.OK]} шт.\n')
