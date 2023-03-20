from bs4 import BeautifulSoup
import requests



# поиск в определённой зоне
url = 'https://student.itmo.ru/ru/dormitory/'
html_text = requests.get(url).text  # получение текста страницы

# используем парсер lxml
soup = BeautifulSoup(html_text, 'lxml')

# общая информация о скидках
block_hostels = soup.find('div', class_= 'cell lg-9 md-12 content-block').find('section').find_all('div', class_='card')  # нахождение нужного блока с информацией
with open("hostels-scrape", "w", encoding="utf-8") as file:  # запись данных в файл
    for el in block_hostels:
        file.write(el.find('div', class_='card__info').text.replace('Подробнее', '').replace('\n\n', '\n').replace('\xa0', ''))  # убираем проблемы и ненужные символы

