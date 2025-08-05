import sys
import argparse

if __name__ == '__main__':
    # Инициализация парсера аргументов с описанием.
    parser = argparse.ArgumentParser(description='Вежливый скрипт')
    # Извлечение аргументов командной строки в переменную args.
    parser.add_argument('name')
    parser.add_argument('-s', '--surname')
    args = parser.parse_args() 