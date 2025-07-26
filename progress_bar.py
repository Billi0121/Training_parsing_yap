from time import sleep
from tqdm import tqdm

if __name__ == '__main__':
    for i in tqdm(range(2000), desc='First itaration'):
        sleep(0.003)
    # print('Finaly we waited for this!')
    for i in tqdm(range(1000), desc='А вот и второй'):
        sleep(0.001) 
