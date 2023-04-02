import requests
from telegraph import Telegraph
import json
from bs4 import BeautifulSoup


def dop(el, info, table_flag=True):
    for k in el:
        if str(k).startswith('<h') or str(k).startswith('<img') or str(k).startswith('<p><img'):
            continue
        if str(k).startswith('<div') or str(k).startswith('<section') or str(k).startswith('<button'):
            dop(k, info)
            continue
        if str(k).startswith('<table') or str(k).startswith('<tbody') or str(k).startswith('<tr') or str(k).startswith('<td'):
            if str(k).startswith('<tr') and table_flag:
                table_flag = False
                continue
            if str(k).startswith('<td style="text-align:center">'):  # если отсутствует тег <p> в строке
                string = str(k).replace('<td style="text-align:center">', '<p>').replace('</td>', '</p>')
                dop(string, info, table_flag)
                continue
            dop(k, info, table_flag)
            continue
        else:
            if k == '\n':
                continue
            
            info.append(str(k).replace('<a href="', '<a href="https://student.itmo.ru'))
    return ''.join(info)


def req(link):
    info = []
    url = link
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    for i in soup.select('body > main > div > section > div > div.cell.lg-9.md-12.content-block > section '):
        dop(i, info)

    return ''.join(info).replace('\n', "")


def telegraph_api(text):
    with open('graph_bot.json') as f:
        graph_bot = json.load(f)

    #создание страницы
    data={
        'access_token':graph_bot["access_token"],
        'title':'article_head', # Заголовок, обязательный параметр
        'author_name':'', # это поле можно не заполнять
        'content': '<p>Hello, world!</p>',# Текст (массив Node), обязательный параметр
        'return_content':'false' # если стоит true в ответе придет и то, что размещено, если false, то поле не вернется
    }
    page=requests.get("https://api.telegra.ph/createPage?", params=data)

    telegraph = Telegraph(graph_bot["access_token"]) # передаём токен доступ к страницам аккаунта  
    response = telegraph.create_page(
        "Hey", # заголовок страницы
        html_content=text # ставим параметр html_content, добавляем текст страницы
    )

    print('https://telegra.ph/{}'.format(response['path'])) # распечатываем адрес страницы

links = ['https://student.itmo.ru/ru/repeat_interim_exams/',
         'https://student.itmo.ru/ru/scholarship_basic/',
         'https://student.itmo.ru/ru/scholarship_up/',
         'https://student.itmo.ru/ru/scholarship_social/',
         'https://student.itmo.ru/ru/scholarship_social_2/',
         'https://student.itmo.ru/ru/booking/',
         'https://student.itmo.ru/ru/pushkin_card/',
         'https://student.itmo.ru/ru/discounts/',
         'https://student.itmo.ru/ru/preferential_ticket/',
         'https://student.itmo.ru/ru/bsk/',]

for link in links:
    telegraph_api(req(link))
