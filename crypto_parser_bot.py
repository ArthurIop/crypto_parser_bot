from bs4 import BeautifulSoup
import requests


URL = 'https://www.coingecko.com/'

HEADERS = {'user-agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36', 'accept': '*/*' }

def get_html(url,params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r

def get_content (html, name):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('tr')

    listing = []
    crypto = {}
    default = 0
    for item in items:
        try:
            short_coin_name = item.find('a', class_='d-lg-none font-bold').get_text().strip('\n')
            coin_name = item.find('a', class_='d-none d-lg-flex font-bold align-items-center justify-content-between').get_text().strip('\n')
            currency_rate = item.find('span', class_='no-wrap').get_text().strip('\n')
            change_percent_1h = item.find('td',
                                          class_='td-change1h change1h stat-percent text-right col-market').get_text().strip(
                '\n')
            change_percent_24h = item.find('td', class_='td-change24h change24h stat-percent text-right col-market').get_text().strip('\n')
            change_percent_7d = item.find('td',
                                          class_='td-change7d change7d stat-percent text-right col-market').get_text().strip(
                '\n')
            market_capitalization = item.find('td',
                                              class_='td-market_cap cap col-market cap-price text-right').get_text().strip(
                '\n')

        except AttributeError:
            short_coin_name = ''
            coin_name = ''
            currency_rate = ''
            change_percent_1h = ''
            change_percent_24h = ''
            change_percent_7d = ''
            market_capitalization = ''

        if coin_name and short_coin_name != '':
            listing.append({
                    'short_coin_name': short_coin_name,
                    'coin_name': coin_name,
                    'currency_rate': currency_rate,
                    'change_percent_1h': change_percent_1h,
                    'change_percent_24h': change_percent_24h,
                    'change_percent_7d': change_percent_7d,
                    'market_capitalization': market_capitalization,

            })
            crypto.update({coin_name:listing[default
            ]})
            default+=1

    coin_dict = dict(crypto[name])
    decorator(coin_dict)


def decorator(coin_dict):

    output =('Название криптовалюты: '+ coin_dict['coin_name']+'\n'+ 'Короткое название: '+ coin_dict['short_coin_name'] +'\n'+
          'Курс: ' + coin_dict['currency_rate']+ '\n' + 'Изменения за последний час: ' + coin_dict['change_percent_1h']+ '\n' +
          'Изменения за последние 24 часа: ' + coin_dict['change_percent_24h']+ '\n' + 'Изменения за неделю: ' + coin_dict['change_percent_7d']+ '\n' +
          'Рыночная капитализация: '  + coin_dict['market_capitalization'])

    return print(output)

def parse (name):
    html = get_html(URL)
    if html.status_code == 200:
        return str(get_content(html.text, name))
    else:
        print('Error')

parse('Kusama')
