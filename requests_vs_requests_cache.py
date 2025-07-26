import requests
import pprint
# import requests_cache
# from tqdm import tqdm

# DELAYED_URL = 'http://httpbin.org/delay/3'

# if __name__ == '__main__':
#     for i in tqdm(range(3), desc='First'):
#         # Загрузка веб-страницы с сервера.
#         requests.get(DELAYED_URL)

#     # Сессия для работы с кешированной загрузкой.
#     session = requests_cache.CachedSession()
#     # Очистка кеша, чтобы каждый новый запуск программы
#     # не зависел от предыдущего.
#     session.cache.clear()
    
#     # Допишите к циклу прогресс-бар, дайте ему название "Загрузка из кеша".
#     for i in tqdm(range(3), desc='Hello world'):
#         # Загрузка веб-страницы через кеширующую сессию.
#         session.get(DELAYED_URL) 

response = requests.get('https://api.github.com')
# print(response.text)
# print(response.status_code)
if response.ok:
    print('What you want!')