# Задание А
# A. Функция принимает в качестве аргумента набор ссылок. 
# Ссылки имеют формат ссылок на проекты на 
# гитхабе (например: https://github.com/miguelgrinberg/Flask-SocketIO, 
#          https://github.com/miguelgrinberg/Flask-SocketIO.git). 
# Функция должна обработать полученные ссылки и вывести в консоль 
# названия самих гит-проектов. 
# Стоит рассмотреть защиту от ссылок "вне формата".

import re

urls = [
    "https://github.com/miguelgrinberg/Flask-SocketIO",
    "https://github.com/miguelgrinberg/Flask-SocketIO.git",
    "https://github.com/aio-libs/aiohttp",
    "https://github.com/psf/requests-html",
    "https://github.com/tornadoweb/tornado",
    "https://github.com/VadimVolkovsky/hice_messenger",
    "https://anyhub.com/TrololoLink/dummy_project",
    "www.github.com/TrololoLink/dummy_project",
    "github.com/TrololoLink/dummy_project.negit",
    "https://github.com/miguelgrinberg/Flask-SocketIO.negit",
]


pattern = r'https:\/\/github\.com\/.+\/(?P<name>[\w-]+)(?:\.git)?$'


def get_project_name():
    for url in urls:
        match = re.search(pattern, url)
        if match:
            print(match.group('name'))


get_project_name()
