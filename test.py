from bs4 import BeautifulSoup
import requests_cache
import requests
from urllib.parse import urljoin

if __name__ == '__main__':
    
    docs = """<!DOCTYPE html>
        <html>
        <head>
        <title>Моя библиотека</title>
        </head>
        <body>

        <header id="main-header">
            <h1>Библиотека</h1>
            <nav>
            <a href="#fiction">Художественные</a>
            <a href="#nonfiction">Научные</a>
            </nav>
        </header>

        <main>
            <section id="fiction">
            <h2 class="section-title">Художественные книги</h2>

            <div class="book-card" id="book1">
                <h3 class="book-title">Преступление и наказание</h3>
                <p class="author">Фёдор Достоевский</p>
                <p class="genre">Роман</p>
                <p class="description">История студента, совершившего убийство.</p>
            </div>

            <div class="book-card" id="book2">
                <h3 class="book-title">Анна Каренина</h3>
                <p class="author">Лев Толстой</p>
                <p class="genre">Трагедия</p>
                <p class="description">История любви и предательства.</p>
            </div>
            </section>

            <section id="nonfiction">
            <h2 class="section-title">Научные книги</h2>

            <div class="book-card" id="book3">
                <h3 class="book-title">Краткая история времени</h3>
                <p class="author">Стивен Хокинг</p>
                <p class="genre">Наука</p>
                <p class="description">О времени, пространстве и Вселенной.</p>
            </div>

            <div class="book-card" id="book4">
                <h3 class="book-title">Геном</h3>
                <p class="author">Мэтт Ридли</p>
                <p class="genre">Биология</p>
                <p class="description">Исследование генетики человека.</p>
            </div>
            </section>
        </main>

        <footer id="main-footer">
            <p>Контакты: <a href="mailto:library@example.com">library@example.com</a></p>
            <small>&copy; 2025 Моя библиотека</small>
        </footer>

        </body>
        </html>
    """

    URL = 'https://docs.python.org/3/whatsnew/'
    
    # sessions = requests_cache.CachedSession()
    # response = sessions.get(docs)

    soup = BeautifulSoup(docs ,'lxml')
    book = soup.find('div', id='book4')
    print(book.text)
    