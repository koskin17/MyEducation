from bs4 import BeautifulSoup
import urllib.request

class Parser:

    raw_html = ''
    html = ''
    results = []

    def __init__(self, url, path):
        self.url = url
        self.path = path

    def get_html(self):
        request = urllib.request.urlopen(self.url)
        self.raw_html = request.read()
        self.html = BeautifulSoup(self.raw_html, 'html.parser')

    def parsing(self):
        news = self.html.find_all('li', class_ = 'liga-news-item')

        for item in news:
            title = item.find('span', class_ = 'd-block').get_text(strip = True)
            desc = item.find('span', class_ = 'name-dop').get_text(strip = True)
            href = item.a.get('href')
            self.results.append({
                'title': title,
                'desc': desc,
                'href': href})        

    def save(self):
        with open(self.path, 'w', encoding = 'utf-8') as f:
            i = 1
            for item in self.results:
                f.write(f'Новость № {i}\nЗаголовок новости: {item["title"]}\n')
                f.write(f'Описание новости: {item["desc"]}\n')
                f.write(f'Ссылка на новость: {item["href"]}\n')
                f.write('\n*****************************************\n')
                i += 1

        print('Парсинг завершён.')

    def run(self):
        self.get_html()
        self.parsing()
        self.save()       
