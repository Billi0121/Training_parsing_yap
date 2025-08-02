import requests
from bs4 import BeautifulSoup
import requests_cache
from urllib.parse import urljoin
from tqdm import tqdm

news = 'https://docs.python.org/3/whatsnew/'
DOWNLOADS_URL = 'https://docs.python.org/3/download.html'

if __name__ == '__main__':
    session = requests_cache.CachedSession()
    response = session.get(news)
    soup = BeautifulSoup(response.text, features='lxml')


    main_div = soup.find('section', attrs={'id': 'what-s-new-in-python'})
    div_with_ul = main_div.find('div', attrs={'class': 'toctree-wrapper'})
    sections_by_python = div_with_ul.find_all('li', attrs={'class': 'toctree-l1'})

    result = []
    for section in tqdm(sections_by_python, desc='Links'):
        version_a_tag = section.find('a')
        href = version_a_tag['href']
        version_link = urljoin(news, href)
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