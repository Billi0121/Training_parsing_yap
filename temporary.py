from bs4 import BeautifulSoup
import requests_cache
import requests
from urllib.parse import urljoin
from tqdm import tqdm

if __name__ == '__main__':
    URL = 'https://docs.python.org/3/whatsnew/'
    
    sessions = requests_cache.CachedSession()
    response = sessions.get(URL)

    soup = BeautifulSoup(response.text, 'lxml')

    main_tag = soup.find('section', id='what-s-new-in-python')
    inner_tag = main_tag.find('div', class_='toctree-wrapper compound')
    throttle1 = inner_tag.find_all('li', class_='toctree-l1')

    result = []
    for url in tqdm(throttle1, desc='Loading Url'):
        find = url.find('a')
        href = find['href']
        join = urljoin(URL, href)

        response = sessions.get(join)
        soup = BeautifulSoup(response.text, 'lxml')
        h1 = soup.find('h1')
        dl = soup.find('dl')
        dl_text = dl.text.replace('\n', ' ')
        # print(join, h1.text, dl.text)
        result.append(
            (join, h1.text, dl.text)
        )

for row in result:
    print(*row)