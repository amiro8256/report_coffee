import sys

from args_parsing import configure_argument_parser
from calculate_funcs import get_median_coffee
from constants import MODE_TO_FUNCTION
from outputs import create_table
from read_file import get_students_info


MODE_TO_FUNCTION['median_coffee'] = get_median_coffee


def main():
    parser = configure_argument_parser()
    args = parser.parse_args()

    if args.files is None:
        print('Не указаны файлы для обработки.')
        sys.exit(1)
    if args.report not in MODE_TO_FUNCTION:
        print(f'Укажите название отчёта.'
              f' Используйте -h/--help для получения справки.'
              )
        sys.exit(1)

    try:
        students_info = get_students_info(args.files)
    except FileNotFoundError as error:
        print(f'Файл не найден, {error}')
        sys.exit(1)
    except Exception as error:
        print(f'Ошибка при чтении файла, {error}')
        sys.exit(1)

    output_data = MODE_TO_FUNCTION[args.report](students_info)
    headers = ['student', args.report]
    table = create_table(output_data, headers)
    print(table)


if __name__ == '__main__':
    main()
