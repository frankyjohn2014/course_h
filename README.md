Сервис по парсингу и сохранению видео с сайта cousehunter
Парсинг вручную(2 csv в папке csv/links.csv и csv/posts.csv) и автоматически.
Запуск парсинга celery+redis раз в минуту проверяет есть ли ошибка получения видео, если ошибка то парсит и пересохраняет данные: celery -A scraping_service worker -B -l INFO 
