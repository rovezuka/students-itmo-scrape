import requests
import json
from telegraph import Telegraph

def telegraph_api(text, header):
    with open('graph_bot.json') as f:
        graph_bot = json.load(f)

    #создание страницы
    data={
        'access_token':graph_bot["access_token"],
        'title':'article_head', # Заголовок, обязательный параметр
        'author_name':'', # это поле можно не заполнять
        'content': '<p>Hello, world!</p>',# Текст (массив Node), обязательный параметр
        'return_content':'true' # если стоит true в ответе придет и то, что размещено, если false, то поле не вернется
    }
    page=requests.get("https://api.telegra.ph/createPage?", params=data)

    telegraph = Telegraph(graph_bot["access_token"]) # передаём токен доступ к страницам аккаунта  
    response = telegraph.create_page(
        header, # заголовок страницы
        html_content=''.join(list(map(str, text))) # ставим параметр html_content, добавляем текст страницы
    )

    print('https://telegra.ph/{}'.format(response['path'])) # распечатываем адрес страницы