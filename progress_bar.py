from time import sleep
from tqdm import tqdm
import requests

# if __name__ == '__main__':
#     for i in tqdm(range(2000), desc='First itaration'):
#         sleep(0.003)
#     # print('Finaly we waited for this!')
#     for i in tqdm(range(1000), desc='А вот и второй'):
#         sleep(0.001) 

# reponse = requests.get('https://google.com')
# print(reponse.content)


1
simple_string = (
    'Осень наступила,\n'
    'высохли цветы,\n'
    'и глядят уныло\n'
    'голые кусты.\t А.Н. Плещеев'
)
raw_string = (
    r'Осень наступила,\n'
    r'высохли цветы,\n'
    r'и глядят уныло\n'
    r'голые кусты.\t А.Н. Плещеев'
)

print(simple_string)
print(raw_string)