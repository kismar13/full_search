import requests

from config import SEARCH_MAPS_API_KEY


def find_nearest_organization(ll: tuple[float, float], span: tuple[float, float],
                              organization_type: str):
    # Выполняем запрос.
    response = requests.get('http://search-maps.yandex.ru/1.x/', params={
        'apikey': SEARCH_MAPS_API_KEY,
        'spn': ','.join(map(str, span)),
        'll': ','.join(map(str, ll)),
        'text': organization_type,
        'lang': 'ru_RU',
        'type': 'biz',
    })

    if not response:
        raise RuntimeError(
            f'''Ошибка выполнения запроса:
                {response.request.url}
                Http статус: {response.status_code} ({response.reason})''')

    # Преобразуем ответ в словарь
    data = response.json()
    # Получаем первую найденную организацию.
    organizations = data['features']
    if len(organizations) == 0:
        return None
    return organizations[0]


