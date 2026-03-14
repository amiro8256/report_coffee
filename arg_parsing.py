from argparse import ArgumentParser


def configure_argument_parser() -> ArgumentParser:
    """Функция описывает ожидаемые аргументы командной строки."""
    parser = ArgumentParser()
    parser.add_argument('-f', '--files', nargs='+', help='Название файлов')
    parser.add_argument('-r', '--report', help='Название отчета')
    return parser
