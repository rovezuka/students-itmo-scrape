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
discounts = (block_discount.find('section').find('h1').text+blocks_info[0].text+'\n'+blocks_info[1].find('p').text + blocks_info[1].find('ul').text).replace('\xa0', '')   # выделение текста и удаление невидимых символов

discounts_url = 'https://student.itmo.ru/ru/discounts/'
discounts_get = requests.get(discounts_url).text
disconuts_soup = BeautifulSoup(discounts_get, 'lxml')
all_discounts = disconuts_soup.find('div', class_='cell lg-9 md-12 content-block').find('section').find_all('div', class_='card')
with open("discounts-scrape.txt", "w", encoding="utf-8") as file:  # запись данных в файл
      file.write(discounts)
      for disc in all_discounts:
          file.write(disc.find('h5').text.replace("'", "")+'\n')
          for el in disc.find_all('p'):
               file.write(el.text.replace('\xa0', '')+'\n')

