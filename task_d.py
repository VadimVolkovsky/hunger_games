# D. Реализовать функцию, которая замеряет время на 
# исполнение 100 запросов к адресу: http://httpbin.org/delay/3.
# Запросы должны выполняться асинхронно.
# Допускается написание вспомогательных функций и использование
# сторонних библиотек.
# Результат замера времени выводит в консоль.
# Ожидаемое время не должно превышать 10 секунд.


import asyncio
from datetime import datetime

import aiohttp

URL = 'http://httpbin.org/delay/3'
REQUESTS_AMOUNT = 100

timeout = aiohttp.ClientTimeout(total=9)


async def task(task_id):
    async with aiohttp.ClientSession() as session:
        try:
            await session.get(URL, timeout=timeout)
        except TimeoutError:
            print(f'Таска: {task_id} - сайт не отвечает более 9 сек')
    print(f'Задача {task_id} выполнена.')


async def async_execute():
    tasks = [asyncio.ensure_future(task(i)) for i in range(
        1, REQUESTS_AMOUNT+1)
    ]
    await asyncio.wait(tasks)


if __name__ == '__main__':
    print(f'Запуск асинхронной отправки запросов к сайту: {URL}')
    start_time = datetime.now()
    asyncio.run(async_execute())
    end_time = datetime.now()
    print(f'Итоговое время выполнения: {end_time - start_time} секунд.')
