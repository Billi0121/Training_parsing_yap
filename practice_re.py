import re
from bs4 import BeautifulSoup
# Lear To take info with re 

text = """ Он проживал в городе Иваново на улице Наумова. Номер дома 125 был зеркальной копией его номера квартиры 521.

Адрес: город Новосибирск, улица Фрунзе, дом 321, квартира 15. """


soup = BeautifulSoup(text, 'lxml')
first = re.search(r'\d+', text)
print(first)