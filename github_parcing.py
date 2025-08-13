from bs4 import BeautifulSoup
import requests

URL = 'https://github.com/'

if __name__ == '__main__':

    response = requests.get(URL)

    soup = BeautifulSoup(response.text, 'lxml')
    f = soup.find('div', class_='mb-3 dashboard-changelog <color-bg-default border color-border-default p-3 rounded-2')
    print(f)