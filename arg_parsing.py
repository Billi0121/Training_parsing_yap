import sys
import argparse

MURZIK = '=^..^=______/'

if __name__ == '__main__':
    # Инициализация парсера аргументов с описанием.
    parser = argparse.ArgumentParser(description='Вежливый скрипт')
    # Извлечение аргументов командной строки в переменную args.
    parser.add_argument('name', help='Имя')
    parser.add_argument('-s', '--surname' , help='Фамилия')
    parser.add_argument('-c', '--city', help='Город', choices=['Chekhov', 'Dublin', 'Minsk', 'Simbirsk'])
    parser.add_argument('-m', '--murzik', action='store_false', help=f'Отправить кота Мурзика {MURZIK}'
    )
    args = parser.parse_args()
    parts = []

    parts.append(f'Hello {args.name}')

    if args.surname is not None:
        parts.append(f'{args.surname}')
    if args.city is not None:
        parts.append(f'From {args.city}')
    if args.murzik:
        parts.append(f'{MURZIK}')
    print(*parts)