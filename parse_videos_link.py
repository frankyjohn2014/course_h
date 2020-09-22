from bs4 import BeautifulSoup
import requests
import lxml
import codecs
import json
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# import geckodriver_autoinstaller
import ast


def get_html(site):
# https://curl.trillworks.com/

    headers = {
        'authority': 'coursehunter.net',
        'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiIsImp0aSI6IjRmMWcyM2ExMmFhIn0.eyJpc3MiOiJodHRwczpcL1wvY291cnNlaHVudGVyLm5ldCIsImF1ZCI6Imh0dHBzOlwvXC9jb3Vyc2VodW50ZXIubmV0IiwianRpIjoiNGYxZzIzYTEyYWEiLCJpYXQiOjE2MDA3NzkyNjYsIm5iZiI6MTYwMDc3OTMyNiwiZXhwIjoxNjAxMzg0MDY2LCJ1c2VyX2lkIjoiNTE5ODMiLCJlX21haWwiOiJmcmFua3lqb2huMjAxNEBnbWFpbC5jb20ifQ.TfC-J-mVvcyJz1m_s1abOsQTp5vXoAKvlaUkp97KWg8',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
        'content-type': 'application/json',
        'accept': '*/*',
        'origin': 'https://coursehunter.net',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://coursehunter.net/course/osnovy-matematiki-dlya-data-science',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'cookie': '_ga=GA1.2.792073693.1596020765; _gid=GA1.2.1532052560.1600665226; CHUNTERS=o3l35e03h5f0066r8btt35op02; ch_quiz=d2a3718978519ebaf5147cda5a1d4138; locale=ru; redirect_after_login=https://coursehunter.net/; user_ident=3774ecfd-7f7d-46d7-9eab-fa4bed46783f; accessToken=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiIsImp0aSI6IjRmMWcyM2ExMmFhIn0.eyJpc3MiOiJodHRwczpcL1wvY291cnNlaHVudGVyLm5ldCIsImF1ZCI6Imh0dHBzOlwvXC9jb3Vyc2VodW50ZXIubmV0IiwianRpIjoiNGYxZzIzYTEyYWEiLCJpYXQiOjE2MDA3NzkyNjYsIm5iZiI6MTYwMDc3OTMyNiwiZXhwIjoxNjAxMzg0MDY2LCJ1c2VyX2lkIjoiNTE5ODMiLCJlX21haWwiOiJmcmFua3lqb2huMjAxNEBnbWFpbC5jb20ifQ.TfC-J-mVvcyJz1m_s1abOsQTp5vXoAKvlaUkp97KWg8; _gat=1; _gat_user=1',
    }

    data = '{"course_id":"3472","user_id":"51983","current_track":null,"current_seek":0}'

    response = requests.post('https://coursehunter.net/api/history', headers=headers, data=data)


    r = requests.get(site, headers=headers, data=data)
    return r.text

def get_page_data(html):                         #sources
    soup = BeautifulSoup(html, 'lxml')           #(format_in, parser)
    script = soup.find_all('script')[2]
    dic = []
    for i in script:
        s = i.find('"title": "1')
        file_x = i[s-1:]
        spli_x = file_x.split(',')
        for o in spli_x:
            z = o.lstrip()
            dic.append(z)
        i = 0
        f = 1
        '''В массиве 1 title , в два link'''
        urls = []
        while True:
            
            try:
                # print(dic[i].split(': ')[1].strip('"'))
                # print(dic[f].split(': ')[1].strip('"'))
                ras = dic[f].split(': ')[1].strip('"')
                urls.append(ras)
                handle = codecs.open('333.csv','w')
                handle.writelines(str(urls))
                handle.close
                i += 4
                f += 4
            except:
                break

def main():
    with open("1.html", "r") as read_file:
        ss = {}
        data = read_file.read()
        clear_data=data.replace('\'', '')
        clear_data1 = clear_data.strip('[ ]')
        clear_data2 = clear_data1.split(',')
        ''' Вставить перебор для получения всех ссылок текущего урока'''
        print(clear_data2[1])
        get_page_data(get_html(clear_data2[1]))

if __name__ == '__main__':
    main()