from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import declarative_base, Session, declared_attr
from bs4 import BeautifulSoup
import requests
import pprint

Base = declarative_base()

class Pep(Base):
    __tablename__ = 'pep'

    id = Column(Integer, primary_key=True)
    type_status = Column(String(2))
    number = Column(Integer, unique=True)
    title = Column(String(200))
    author = Column(String(200))

URL = 'https://peps.python.org/#numerical-index'  

if __name__ == '__main__':
    engine = create_engine('sqlite:///sqlite.db', echo=False)
    Base.metadata.create_all(engine)
    # Base.metadata.drop_all(engine)
    session = Session(engine)

    response = requests.get(URL)
    soup = BeautifulSoup(response.text, 'lxml')
# спарсите таблицу построчно и запишите данные в БД
    section_tag = soup.find('table', class_='pep-zero-table docutils align-default')
    tbody_tag = section_tag.find('tbody')
    tr_tags = tbody_tag.find_all('tr')
    for tr_tag in tr_tags:
        type_status = tr_tag.find('td').text
        number = tr_tag.find('td').find_next_sibling().text
        title = tr_tag.find('td').find_next_sibling().find_next_sibling().text
        authors = tr_tag.find('td').find_next_sibling().find_next_sibling().find_next_sibling().text
        print(authors)
        pep = Pep(
        type_status=type_status,
        number=number,
        title=title,
        author=authors
    )
        session.add(pep)
    session.commit()