from bs4 import BeautifulSoup
import requests


# поиск в определённой зоне
url = 'https://student.itmo.ru/ru/benefits/'
html_text = requests.get(url).text  # получение текста страницы

# используем парсер lxml
soup = BeautifulSoup(html_text, 'lxml')

# общая информация о скидках
block_discount = soup.find('div', class_= 'cell lg-9 md-12 content-block')  # нахождение нужного блока с информацией
blocks_info = block_discount.find('section').find_all('section')  # создание списка из инфы о скидках и контактной информации
result = (block_discount.find('section').find('h1').text+blocks_info[0].text).replace('\xa0', '')   # выделение текста и удаление невидимых символов
with open("discounts", "w", encoding="utf-8") as file:  # запись данных в файл
     file.write(result)

