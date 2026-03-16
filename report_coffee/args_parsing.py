from argparse import ArgumentParser

from constants import MODE_TO_FUNCTION


def configure_argument_parser() -> ArgumentParser:
    """Функция описывает ожидаемые аргументы командной строки."""
    parser = ArgumentParser()
    parser.add_argument('-f', '--files', nargs='+', help='Название файлов')
    parser.add_argument(
        '-r',
        '--report',
        choices=list(MODE_TO_FUNCTION.keys()),
        help='Название отчета',
    )
    return parser
