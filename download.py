from bs4 import BeautifulSoup
import requests_cache
from urllib.parse import urljoin
import re
from pathlib import Path

BASE_DIR = Path(__file__).parent    
if __name__ == '__main__':

    DOWNLOAD_URL = 'https://docs.python.org/3/download.html'

    session = requests_cache.CachedSession()
    response = session.get(DOWNLOAD_URL)

    soup = BeautifulSoup(response.text, 'lxml')
    main_tag = soup.find('div', {'role': 'main'}) #we can use without him, find why & how?
    table_tag = main_tag.find('table', {'class': 'docutils'}) 
    pdf_a4_tag = table_tag.find('a', {'href': re.compile(r'.+pdf-a4\.zip$')})
    pdf_a4_link = pdf_a4_tag['href']
    archive_url = urljoin(DOWNLOAD_URL, pdf_a4_link) 
    print(archive_url)

    filename = archive_url.split('/')[-1]   
    downloads_dir = BASE_DIR / 'downloads'
    # Создайте директорию.
    downloads_dir.mkdir(exist_ok=True)
    # Получите путь до архива, объединив имя файла с директорией.
    archive_path = downloads_dir / filename 

    response =  session.get(archive_url)

    with open(archive_path, 'wb') as file:
        file.write(response.content) 