import requests


def get_map(*, ll: tuple[float, float], spn: tuple[float, float], map_type: str,
            **kwarg: tuple[float, float]) -> str:
    response = requests.get('http://static-maps.yandex.ru/1.x/', params={
        'll': ','.join(map(str, ll)),
        'spn': ','.join(map(str, spn)),
        'l': map_type,
        **{key: ','.join(map(str, value)) for key, value in kwarg.items()},
    })

    if not response:
        raise RuntimeError(
            f'''Ошибка выполнения запроса:
            {response.request.url}
            Http статус: {response.status_code} ({response.reason})''')

    filename = 'map.png'
    with open(filename, 'wb') as file:
        file.write(response.content)
    return filename


import os
from sys import argv
import pygame

from geocoder_api import (
    get_coordinates,
    get_coordinates_and_span,
)
from static_maps_api import get_map


def main() -> None:
    toponym_to_find = ' '.join(argv[1:])

    if toponym_to_find == '':
        print('No data')
        return

    # Показываем карту с фиксированным масштабом.
    lat, lon = get_coordinates(toponym_to_find)
    show_map(ll=(lat, lon), spn=(0.005, 0.005), map_type='map')

    # Показываем карту с масштабом, подобранным по заданному объекту.
    (lat, lon), (dx, dy) = get_coordinates_and_span(toponym_to_find)
    show_map(ll=(lat, lon), spn=(dx, dy), map_type='map')

    # Добавляем исходную точку на карту.
    show_map(ll=(lat, lon), spn=(dx, dy), map_type='map', pt=(lat, lon))


def show_map(*, ll: tuple[float, float], spn: tuple[float, float], map_type: str,
             **kwarg: tuple[float, float]) -> None:
    map_filename = get_map(ll=ll, spn=spn, map_type=map_type, **kwarg)
    # Инициализируем pygame
    pygame.init()
    screen = pygame.display.set_mode((600, 450))
    # Рисуем картинку, загружаемую из только что созданного файла.
    screen.blit(pygame.image.load(map_filename), (0, 0))
    # Переключаем экран и ждем закрытия окна.
    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()
    # Удаляем за собой файл с изображением.
    os.remove(map_filename)


main()
