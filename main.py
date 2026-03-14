from arg_parsing import configure_argument_parser
from outputs import create_table
from read_file import get_students_info


def get_coffee_avg_sum(students_data: dict) -> list:
    """
    Функция получает медиану затрат на кофе для каждого уникального студента.
    """
    students_coffee = []
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

        students_coffee.append((name, avg_price))
        students_coffee.sort(key=lambda x: x[1], reverse=True)
    return students_coffee


MODE_TO_FUNCTION = {'median_coffee': get_coffee_avg_sum}


def main():
    parser = configure_argument_parser()
    args = parser.parse_args()

    # Проверка на существование файлов
    students_data = get_students_info(args.files)

    # проверка на несуществующий отчёт
    output_data = MODE_TO_FUNCTION[args.report](students_data)
    headers = ['student', args.report]
    table = create_table(output_data, headers)
    print(table)


if __name__ == '__main__':
    main()
