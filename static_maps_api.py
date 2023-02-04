import requests


def get_map(*, ll: tuple[float, float] = None, spn: tuple[float, float], map_type: str,
            pt) -> str:
    params = {
        'spn': ','.join(map(str, spn)),
        'l': map_type,
    }
    if ll is not None:
        params['ll'] = ','.join(map(str, ll))
    if pt is not None:
        params['pt'] = ','.join(map(str, pt)) if isinstance(pt, tuple) else pt
    response = requests.get('http://static-maps.yandex.ru/1.x/', params=params)

    if not response:
        raise RuntimeError(
            f'''Ошибка выполнения запроса:
            {response.request.url}
            Http статус: {response.status_code} ({response.reason})''')

    filename = 'map.png'
    with open(filename, 'wb') as file:
        file.write(response.content)
    return filename