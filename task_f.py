# F. Написать декоратор к предыдущему классу,
# который будет выводить в консоль время выполнения каждого метода.
# Результат выполнения задания должен быть оформлен в виде файла с кодом.


import logging
from datetime import datetime


def time_of_function(func):
    """Декоратор замеряющий время выполнения функции"""
    def wrapper(self):
        start_time = datetime.now()
        result = func(self)
        execution_time = datetime.now() - start_time
        logging.info(
            f'Время выполнения функции {func.__name__}: '
            f'{execution_time.seconds} сек.'
        )
        return result
    return wrapper
