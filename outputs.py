from tabulate import tabulate


def create_table(obj: list, headers: list) -> tabulate:
    """Функция создаёт и возвращает таблицу для вывода в терминал."""
    table = tabulate(obj, headers=headers, tablefmt='grid')
    return table
