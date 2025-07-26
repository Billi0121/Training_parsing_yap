# from time import sleep
# a = 'Hi '
# b = a + 'Bilol'

# print(f'{b}')

# sleep(1)

# c = b + ' How are you'
# print(c)

from tqdm import tqdm
from time import sleep

if __name__ == '__main__':
    for i in tqdm(range(2000), desc='First'):
        sleep(0.003)