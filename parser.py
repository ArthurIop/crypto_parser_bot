import requests
from PIL import Image


# todo: use named tuple
class CoinItem:
    def __init__(self, image, text):
        self.image = image
        self.text = text


# todo: typings
def construct_coin_url(
        coin_name_id,
        order='market_cap_desc',
        vs_currency='usd',
        per_page='100',
        page='1',
        sparkline='false'
) -> str:
    base_url = 'https://api.coingecko.com'
    query_parameters = '?vs_currency=' + vs_currency + '&ids=' + coin_name_id + '&order=' \
                       + order + '&per_page=' + per_page + '&page=' + page + '&sparkline=' + sparkline
    endpoint = base_url + '/api/v3/coins/markets'

    return endpoint + query_parameters


def extract_image(url: str):
    load_image = requests.get(url)

    # todo: with open
    record_image = open("img.png", "wb")
    record_image.write(load_image.content)
    record_image.close()

    return open('img.png', "rb")


def get_content(name):
    coin_name_id = name.lower()
    coin_url = construct_coin_url(coin_name_id)

    coin_data = requests.get(coin_url).json()

    if len(coin_data) == 0:
        return 'Вы ввели неправильное значение, введите /help для подробной информации'

    coin_dict = coin_data[0]
    text = decorator(coin_dict)
    url_image = coin_dict['image']

    return CoinItem(extract_image(url_image), text)


def decorator(coin_dict):
    name, symbol = coin_dict['name'], coin_dict['symbol']
    current_price = str(coin_dict['current_price'])
    change = str(round(coin_dict['price_change_percentage_24h'], 1))
    market_cap = str(coin_dict['market_cap'])

    # todo: loop with spaces
    return 'Название криптовалюты: ' + name + '\n' + 'Монета: ' + symbol + '\n' + 'Курс: ' \
             + current_price + ' $' + '\n' + 'Изменения за последние 24 часа: ' \
             + change + '%' + '\n' + 'Рыночная капитализация: ' + market_cap + ' $' + '\n'


