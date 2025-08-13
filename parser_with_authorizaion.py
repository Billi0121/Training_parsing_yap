import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

LOGIN_URL = 'https://billibi.zapto.org/auth/login/'

if __name__ == '__main__':
    session = requests.Session()
    response = session.get(LOGIN_URL)
    soup = BeautifulSoup(response.text, 'lxml')
    token_tag = soup.find("input", type="hidden")
    token = token_tag["value"]
    data = {
        "csrfmiddlewaretoken": token,
        "username": "BG",
        "password": "lifeisok55",
    }
    
    response = session.post(LOGIN_URL, data=data)
    print(response.text)
    print(session.cookies.get_dict()) 

