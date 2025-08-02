from bs4 import BeautifulSoup
import requests_cache
from tqdm import tqdm
import re
from urllib.parse import urljoin

if __name__ == '__main__':
    DOWNLOADS_URL = 'https://docs.python.org/3/download.html'
    session = requests_cache.CachedSession()
    response = session.get(DOWNLOADS_URL)

    soup = BeautifulSoup(response.text, 'lxml')
    main_tag = soup.find('div', {'role': 'main'})
    table_tag = main_tag.find('table', {'class': 'docutils'}) 
    pdf_a4_tag = table_tag.find('a', {'href': re.compile(r'.+pdf-a4\.zip$')}) 
    pdf_a4_tag = pdf_a4_tag['href']
    achire = urljoin(DOWNLOADS_URL, pdf_a4_tag)
    print(achire)
    
