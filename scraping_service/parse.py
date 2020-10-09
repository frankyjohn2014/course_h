

# @periodic_task(run_every=(crontab(minute='*/1')), name="run_scrap")
# def Parse():
#     def get_html(site):
#     # https://curl.trillworks.com/

#         headers = {
#             'authority': 'coursehunter.net',
#             'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiIsImp0aSI6IjRmMWcyM2ExMmFhIn0.eyJpc3MiOiJodHRwczpcL1wvY291cnNlaHVudGVyLm5ldCIsImF1ZCI6Imh0dHBzOlwvXC9jb3Vyc2VodW50ZXIubmV0IiwianRpIjoiNGYxZzIzYTEyYWEiLCJpYXQiOjE2MDA3NzkyNjYsIm5iZiI6MTYwMDc3OTMyNiwiZXhwIjoxNjAxMzg0MDY2LCJ1c2VyX2lkIjoiNTE5ODMiLCJlX21haWwiOiJmcmFua3lqb2huMjAxNEBnbWFpbC5jb20ifQ.TfC-J-mVvcyJz1m_s1abOsQTp5vXoAKvlaUkp97KWg8',
#             'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
#             'content-type': 'application/json',
#             'accept': '*/*',
#             'origin': 'https://coursehunter.net',
#             'sec-fetch-site': 'same-origin',
#             'sec-fetch-mode': 'cors',
#             'sec-fetch-dest': 'empty',
#             'referer': 'https://coursehunter.net/course/osnovy-matematiki-dlya-data-science',
#             'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
#             'cookie': '_ga=GA1.2.792073693.1596020765; _gid=GA1.2.1532052560.1600665226; CHUNTERS=o3l35e03h5f0066r8btt35op02; ch_quiz=d2a3718978519ebaf5147cda5a1d4138; locale=ru; redirect_after_login=https://coursehunter.net/; user_ident=3774ecfd-7f7d-46d7-9eab-fa4bed46783f; accessToken=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiIsImp0aSI6IjRmMWcyM2ExMmFhIn0.eyJpc3MiOiJodHRwczpcL1wvY291cnNlaHVudGVyLm5ldCIsImF1ZCI6Imh0dHBzOlwvXC9jb3Vyc2VodW50ZXIubmV0IiwianRpIjoiNGYxZzIzYTEyYWEiLCJpYXQiOjE2MDA3NzkyNjYsIm5iZiI6MTYwMDc3OTMyNiwiZXhwIjoxNjAxMzg0MDY2LCJ1c2VyX2lkIjoiNTE5ODMiLCJlX21haWwiOiJmcmFua3lqb2huMjAxNEBnbWFpbC5jb20ifQ.TfC-J-mVvcyJz1m_s1abOsQTp5vXoAKvlaUkp97KWg8; _gat=1; _gat_user=1',
#         }

#         data = '{"course_id":"3472","user_id":"51983","current_track":null,"current_seek":0}'

#         'Передача данных на сайт о user '
#         requests.post('https://coursehunter.net/api/history', headers=headers, data=data)
#         r = requests.get(site, headers=headers, data=data)
#         r_text = r.text

#         return r_text

#     def get_page_data(html,count,site):

#         name_post_m  = []
#         descr_post_m = []
#         time_videos_m = []
#         quantity_videos_m = []
#         time_add_m = []
#         language_videos_m = [] 
#         picture_post_m = []
#         desc_large_m = []
#         site_m = []
#         download_material_href_m = []
#         zip_files_href_m = []
#         company_name_m = []

#         soup = BeautifulSoup(html, 'lxml') #(format_in, parser)
#         script = soup.find_all('script')[2]

#         '''Парсим наименования поста'''
#         name_post = soup.find('p',class_='hero-description').text
#         descr_post = soup.find('div',class_='course-description').text
#         time_videos = soup.find_all('div',class_='course-box-value')[0].text
#         quantity_videos = soup.find_all('div',class_='course-box-value')[1].text
#         time_add = soup.find_all('div',class_='course-box-value')[2].text
#         language_videos = soup.find_all('div',class_='course-box-value')[3].text
#         picture_post = soup.find('img',class_='course-img')['src']
#         desc_large = soup.find('div', class_='course-wrap-description').text
#         download_link_block = soup.find('div', class_='course-wrap-bottom')
#         download_link_a = download_link_block.find_all('a')
#         downoad_material = download_link_a[0]
#         try:
#             zip_files = download_link_a[1]
#         except:
#             zip_files = ''

#         try:
#             download_material_href = downoad_material['href']
#         except:
#             download_material_href = ''
#         try:
#             zip_files_href = zip_files['href']
#         except:
#             zip_files_href = ''

#         company_name = soup.find('a',class_='course-box-value').text
#         '''Сохраняем в словарь'''
#         name_post_m.append(name_post)
#         descr_post_m.append(descr_post)
#         time_videos_m.append(time_videos)
#         quantity_videos_m.append(quantity_videos)
#         time_add_m.append(time_add)
#         language_videos_m.append(language_videos)
#         picture_post_m.append(picture_post)
#         desc_large_m.append(desc_large)
#         site_m.append(site)
#         download_material_href_m.append(download_material_href)
#         zip_files_href_m.append(zip_files_href)
#         company_name_m.append(company_name)

#         d = [name_post_m, descr_post_m, time_videos_m, quantity_videos_m, time_add_m, language_videos_m, picture_post_m,desc_large_m,site_m,download_material_href_m,zip_files_href_m,company_name_m]
#         export_data = zip_longest(*d, fillvalue = '')
#         '''Делаем запись модели Пост для экспорта'''
#         with open('csv/posts.csv', 'a+', encoding="utf-8", newline='') as myfile:
#             wr = csv.writer(myfile)
#             wr.writerows(export_data)
#             myfile.close()

#         '''Ищем нужный скрипт и достаём title:'''
#         dic = []
#         for i in script:
#             s = i.find('"title": "1')
#             file_x = i[s-1:]
#             spli_x = file_x.split(',')
#             for o in spli_x:
#                 z = o.lstrip()
#                 dic.append(z)
#         get_links(dic,count)
#         '''Вызываем функцию сохранения csv ссылок'''

#     def get_links(dic,count):
#         i = 0
        
#         while True:
 
#             name = []
#             urls = []
#             posts_id = []
#             try:
#                 '''В массиве 1 title , в два link'''
#                 all_video = [s for s in dic if "mp4" in s]
#                 all_video_title = [s for s in dic if "|" in s]
#                 try:
#                     all_video_m = all_video[i].split(': ')[1].strip('"')
#                     all_video_title_m = all_video_title[i].split(': ')[1].strip('"')

#                 except:
#                     all_video_title_m = all_video_title[i]
#                 i += 1
#                 name.append(all_video_title_m)
#                 urls.append(all_video_m)
#                 posts_id.append(count+1)
#                 d = [posts_id, name, urls]
  
#                 export_data2 = zip_longest(*d, fillvalue = '')
#                 '''save videos link'''

#                 with open('csv/links.csv', 'a+', encoding="utf-8", newline='') as myfile:
#                     wr = csv.writer(myfile)
#                     wr.writerows(export_data2)
#                     myfile.close()
#             except:
#                 print('break')
#                 break

#     def title_csv():
#         '''Создаём заголовки в csv'''
#         with open('csv/posts.csv', 'w+', encoding="utf-8", newline='') as myfile:
#             wr = csv.writer(myfile)
#             wr.writerow(("title", "descr_post", "time_videos","quantity_videos", "time_add", "language_videos", "picture_post","desc_large","site","download_material_href","zip_files_href","company_name"))
#             myfile.close()
#         with open('csv/links.csv', 'w+', encoding="utf-8", newline='') as myfile:
#             wr = csv.writer(myfile)
#             wr.writerow(("posts","title", "videos"))
#             myfile.close()
        
#     def main():
#         with open("1.html", "r") as read_file:
        
#             data = read_file.read()
#             clear_data = data.replace('\'', '')
#             clear_data1 = clear_data.strip('[ ]')
#             clear_data2 = clear_data1.split(',')
#             '''Вставить перебор для получения всех ссылок текущего урока'''
#             count = 0
#             loop = 0
#             while loop < 4:
#                 print(loop)
#                 get_page_data(get_html(clear_data2[count]), count, clear_data2[count])

#                 count +=1
#                 loop +=1
#     title_csv()
#     main()
#     return HttpResponse('Парсинг прошёл успешно')

# '''Запуск celery'''
# # celery -A scraping_service worker -B -l INFO 