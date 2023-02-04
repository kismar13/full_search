import requests

from sys import argv

from geocoder_api import (
    get_coordinates,
    get_coordinates_and_span,
)
from show_map import show_map


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


main()
