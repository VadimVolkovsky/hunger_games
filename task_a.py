# Задание А
# A. Функция принимает в качестве аргумента набор ссылок.
# Ссылки имеют формат ссылок на проекты на
# гитхабе (например: https://github.com/miguelgrinberg/Flask-SocketIO,
#          https://github.com/miguelgrinberg/Flask-SocketIO.git).
# Функция должна обработать полученные ссылки и вывести в консоль
# названия самих гит-проектов.
# Стоит рассмотреть защиту от ссылок "вне формата".

import re

from testdata import TASK_A_PATTERN as pattern
from validation import validate_is_list, validate_not_empty_list


def get_projects_names(urls: list) -> list:
    """Возвращает названия гит-проектов"""
    validate_is_list(data=urls)
    validate_not_empty_list(data=urls)
    projects_names = []
    for url in urls:
        match = re.search(pattern, url)
        if match:
            projects_names.append(match.group('name'))
    return projects_names
