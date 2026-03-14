import argparse
import csv
from pprint import pprint


def read_file(csv_file: str) -> dict:
    """Функция читает csv файл.

    Возвращает словарь: {
    name: [
        {'coffee_spent': str,
        'date': str,
        'exam': str,
        'mood': str,
        'sleep_hours': str,
        'sleep_hours': str,},
        {...},
        ]
    name: [
        {...},
        {...},
        ]
    }
    """
    with open(csv_file, mode='r', encoding='UTF-8', newline='') as file:
        csv_reader = csv.DictReader(file)
        res = {}
        for row in csv_reader:
            name_student = row.pop('student')
            if name_student not in res:
                res[name_student] = [row]
            else:
                res[name_student].append(row)
    return res


def get_students_info() -> dict:
    """Функция собирает данные о всех студентах из разных файлов."""
    students_data = {}
    files = ['data_test.csv', 'data_test2.csv']
    for csv_file in files:
        data = read_file(csv_file)
        for name in data:
            if name not in students_data:
                students_data[name] = data[name]
            else:
                students_data[name].extend(data[name])

    # pprint(students_data)
    return students_data


def get_coffee_avg_sum():
    """
    Функция получает медиану затрат на кофе для каждого уникального студента.
    """
    students_data = get_students_info()
    students_coffee = {}
    for name, info in students_data.items():
        prices_coffee = []
        for detailed_info in info:
            prices_coffee.append(int(detailed_info['coffee_spent']))

        prices_coffee.sort()
        len_price = len(prices_coffee)
        if len_price % 2 == 0:
            avg_price = (
                prices_coffee[len_price // 2] + prices_coffee[len_price // 2 + 1]
                ) // 2
        else:
            avg_price = prices_coffee[len_price // 2]

        students_coffee[name] = avg_price
        # сортировка по убыванию!
    # pprint(students_coffee)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--files', nargs='+', help='Название файлов')
    parser.add_argument('-r', '--report', help='Название отчета')
    args = parser.parse_args()
    print(args.files)
