from bs4 import BeautifulSoup
import requests



# поиск в определённой зоне
url = 'https://student.itmo.ru/ru/dormitory/'
html_text = requests.get(url).text  # получение текста страницы

# используем парсер lxml
soup = BeautifulSoup(html_text, 'lxml')

# общая информация о скидках
block_hostels = soup.find('div', class_= 'cell lg-9 md-12 content-block').find('section').find_all('div', class_='card')  # нахождение нужного блока с информацией

with open("hostels-scrape.txt", "w", encoding="utf-8") as file:  # запись данных в файл
    for el in block_hostels:
        file.write(el.find('h5').text+'\n')
        for i in el.find_all('p'):
            file.write(i.text.replace('\xa0', '')+'\n')
    contacts = soup.find('div', class_='footer__main').find('div', class_='cell lg-12 md-7 sm-6 xs-12')
    file.write((contacts.find('p').text+contacts.find('div').text).replace('\n\n\n', '\n').replace('\xa0', ''))
    # информация о каждой общаге
    url_hostels = 'https://student.itmo.ru/ru/'
    def hostel(campus):  # передается название или номер кампуса
        responce = requests.get(f'{url_hostels}{campus}').text
        soup = BeautifulSoup(responce, 'lxml')
        responce_soup = soup.find('div', class_='cell lg-9 md-12 content-block').find('section')
        file.write(responce_soup.find('h1').text)
        for x in responce_soup.find_all('section')[1:3]:
            if x.find('h2'): file.write(x.find('h2').text)
            for y in x.find_all('div', class_='grid icon-block__row')[1:]:
                file.write(y.text.replace('\n\n', '\n'))
        contacts = soup.find('div', class_='speakers')
        file.write(contacts.text.replace('\n\n\n', '\n').replace('\xa0', ''))

    for i in ['campus1', 'campus2', 'campus3', 'campus4']:
        hostel(i)  # функция для 4 кампусов общежитий от ИТМО
    
    def other_hostel(campus):
        other_link = requests.get(f'{url_hostels}{campus}').text
        other_hostel = BeautifulSoup(other_link, 'lxml')
        file.write(other_hostel.find('div', class_='cell lg-9 md-12 content-block').text.replace('\n\n\n', '\n'))
    for i in ['karpovki', 'LTA_dormitory/']:
        other_hostel(i)
