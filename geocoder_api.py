import requests


def get_map(*, ll: tuple[float, float] = None, spn: tuple[float, float] = None,
            zoom: float = None,
            map_type: str,
            pt) -> bytes:
    params = {
        'l': map_type,
    }
    if ll is not None:
        params['ll'] = ','.join(map(str, ll))
    if spn is not None:
        params['spn'] = ','.join(map(str, spn)),
    if zoom is not None:
        params['z'] = zoom
    if pt is not None:
        params['pt'] = ','.join(map(str, pt)) if isinstance(pt, tuple) else pt
    response = requests.get('http://static-maps.yandex.ru/1.x/', params=params)

    if not response:
        raise RuntimeError(
            f'''Ошибка выполнения запроса:
            {response.request.url}
            Http статус: {response.status_code} ({response.reason})''')

    return response.content