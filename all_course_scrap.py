from bs4 import BeautifulSoup
import requests
import lxml
import codecs
import time

urls = []

def get_html(site):
    r = requests.get(site)
    return r.text

def get_page_data(html):                         #sources
    soup = BeautifulSoup(html, 'lxml')           #(format_in, parser)

    articles = soup.find('div', class_='course-list').find_all('article')
    
    for article in articles:
        a = article.find('div', class_='course-details-bottom').find_all('a')
        for href in a:
            dict_href = href['href']
            urls.append(dict_href)

    handle = codecs.open('1.html','w', 'utf-8')
    handle.write(str(urls))
    handle.close

def main():
    url = 'https://coursehunter.net/archive'
    get_page_data(get_html(url))
    i = 1
    while True:
        try:
            print(i)
            time.sleep(5)
            url_next = 'https://coursehunter.net/archive?page={0}'.format(i)
            get_page_data(get_html(url_next))
            i += 1
        except:
            print('range is all')
            break

if __name__ == '__main__':
        main()