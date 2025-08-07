import re
from urllib.parse import urljoin
import requests_cache
from bs4 import BeautifulSoup
from tqdm import tqdm
from contanst import BASE_DIR, MAIN_DOC_URL 
from configs import configure_argument_parser

def whats_new():
    # Вместо константы WHATS_NEW_URL, используйте переменную whats_new_url.
    whats_new_url = urljoin(MAIN_DOC_URL, 'whatsnew/')
    if __name__ == '__main__':
        session = requests_cache.CachedSession()
        response = session.get(whats_new_url)
        soup = BeautifulSoup(response.text, features='lxml')


        main_div = soup.find('section', attrs={'id': 'what-s-new-in-python'})
        div_with_ul = main_div.find('div', attrs={'class': 'toctree-wrapper'})
        sections_by_python = div_with_ul.find_all('li', attrs={'class': 'toctree-l1'})

        result = []
        for section in tqdm(sections_by_python, desc='Links'):
            version_a_tag = section.find('a')
            href = version_a_tag['href']
            version_link = urljoin(whats_new_url, href)
            response = session.get(version_link)
            soup = BeautifulSoup(response.text, 'lxml')
            h1 = soup.find('h1')
            dl = soup.find('dl')
            dl_text = dl.text.replace('\n', ' ')
            result.append(
                (version_link, h1.text, dl_text)
            )
        for row in result:
            print(*row) 

# def latest_versions():


# def download():
#     # Вместо константы DOWNLOADS_URL, используйте переменную downloads_url.
#     downloads_url = urljoin(MAIN_DOC_URL, 'download.html')

# Скопируйте весь код ниже.
MODE_TO_FUNCTION = {
    'whats-new': whats_new,
    # 'latest-versions': latest_versions,
    # 'download': download,
}

def main():    
    # Конфигурация парсера аргументов командной строки —
    # передача в функцию допустимых вариантов выбора.
    arg_parser = configure_argument_parser(MODE_TO_FUNCTION.keys())
    # Считывание аргументов из командной строки.
    args = arg_parser.parse_args()
    # Получение из аргументов командной строки нужного режима работы.
    parser_mode = args.mode
    # Поиск и вызов нужной функции по ключу словаря.
    results = MODE_TO_FUNCTION[parser_mode]()

if __name__ == '__main__':
    main() 