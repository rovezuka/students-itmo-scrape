from bs4 import BeautifulSoup
import requests
import json
from telegraph import Telegraph
from req import responce
from telegapi import telegraph_api

def responce(link):
    url = link
    html_text = requests.get(url).text  # получение текста страницы

    # используем парсер lxml
    soup = BeautifulSoup(html_text, 'lxml')

    # общая информация
    info_div = soup.find('div', class_ = 'cell lg-9 md-12 content-block').find('section')
    head = info_div.find('h1')
    return info_div, head

bsk_soup, bsk_header = responce('https://student.itmo.ru/ru/bsk/')
bsk_info = []
bsk_header = bsk_soup.find('h1').text
for i in bsk_soup.find_all('section'):
    bsk_info.append(str(i).replace('<section>', '').replace('</section>', '').replace('<h2>', '\n').replace('<ul>', '').replace('</ul>', '').replace('</h2>', ''))
telegraph_api(bsk_info, bsk_header)


'''def main(link):
    url = link
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    head = soup.find('h1')
    info = []
    for i in soup.select("body > main > div > section > div > div.cell.lg-9.md-12.content-block > section"):        
        informations = i.select('p')
        for el in range(len(informations)):
            info.append(str(informations[el]))
    return info, head


def pushkin_card(link):
    url = link
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    head = soup.find('h1')
    info = []
    for i in soup.select("body > main > div > section > div > div.cell.lg-9.md-12.content-block > section"):        
        informations = i.select('p')
        start = informations.pop(-3)
        how_to_start = informations.pop(-2)
        informations.pop(0)
        for el in informations:
            info.append(str(el))
        how_to_take = i.select('li')
        for el in how_to_take[:3]:
            info.append(el)
        info.append(start)
        info.append(how_to_start)
        for el in how_to_take[3:]:
            info.append(str(el))
    return info, head

parse, header = main('https://student.itmo.ru/ru/bsk/')
telegraph_api(parse, header)'''

# скидки
'''html_discounts, header_discounts = responce('https://student.itmo.ru/ru/discounts/')
discounts_text = []
for i in html_discounts.find_all('div', class_='card'):
    block = i.find('div', class_='card__info')
    h5 = block.find('h5').text
    link = block.find_all('a')
    block_text = block.find('div', class_='card__info-text').find_all('p')
    discounts_text.append(f'<b>{h5}</b><br>')
    for el in block_text:
        discounts_text.append(el)
    if link: 
        link = link[-1]
        discounts_text.append(link)
    discounts_text.append('<br>')
discounts_name = 'discounts.txt'
telegraph_api(discounts_text, discounts_name, header_discounts)'''

# пушкинская карта
'''html_pushkin, header_pushkin = responce('https://student.itmo.ru/ru/pushkin_card/')
pushkin_text = []

for i in html_pushkin.find('section').find_all('p')[1:-1]:
    pushkin_text.append(i)
for y in html_pushkin.find('section').find('ul'):
    pushkin_text.append(y)
pushkin_text.append(html_pushkin.find('section').find_all('p')[-1])
pushkin_text.append(html_pushkin.find('div', 'accordion').find('p'))
for x in html_pushkin.find('div', 'accordion').find('div', class_='accordion__item').find('div', class_='accordion__body').find_all('li'):
    pushkin_text.append(x)
pushkin_name = 'pushkin.txt'
telegraph_api(pushkin_text, pushkin_name, header_pushkin)'''

