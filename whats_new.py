import requests
from bs4 import BeautifulSoup
import requests_cache
from urllib.parse import urljoin

news = 'https://docs.python.org/3/whatsnew/'

if __name__ == '__main__':
    session = requests_cache.CachedSession()
    response = session.get(news)
    soup = BeautifulSoup(response.text, features='lxml')


    main_div = soup.find('section', attrs={'id': 'what-s-new-in-python'})
    div_with_ul = main_div.find('div', attrs={'class': 'toctree-wrapper'})
    sections_by_python = div_with_ul.find_all('li', attrs={'class': 'toctree-l1'})

    for section in sections_by_python:
        version_a_tag = section.find('a')
        href = version_a_tag['href']
        version_link = urljoin(news, href)
        print(version_link) 