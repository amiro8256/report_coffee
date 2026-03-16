import pytest

from report_coffee.calculate_funcs import get_median_coffee

ONE_ROW = {
    'Иван Кузнецов': [
        {
            'date': '2024-06-01',
            'coffee_spent': '600',
            'sleep_hours': '3.0',
            'study_hours': '15',
            'mood': 'зомби',
            'exam': 'Математика',
        },
    ]
}

TWO_ROWS = {
    'Джузеппе Бальзамо': [
        {
            'date': '2024-06-01',
            'coffee_spent': '600',
            'sleep_hours': '2.5',
            'study_hours': '17',
            'mood': 'зомби',
            'exam': 'Математика',
        },
        {
            'date': '2024-06-02',
            'coffee_spent': '650',
            'sleep_hours': '4.0',
            'study_hours': '12',
            'mood': 'отлично',
            'exam': 'Физика',
        },
    ]
}

THREE_ROWS = {
    'Кристобаль Хунта': [
        {
            'date': '2024-06-01',
            'coffee_spent': '600',
            'sleep_hours': '2.5',
            'study_hours': '17',
            'mood': 'зомби',
            'exam': 'Математика',
        },
        {
            'date': '2024-06-02',
            'coffee_spent': '650',
            'sleep_hours': '4.0',
            'study_hours': '12',
            'mood': 'отлично',
            'exam': 'Физика',
        },
        {
            'date': '2024-06-03',
            'coffee_spent': '700',
            'sleep_hours': '2.0',
            'study_hours': '18',
            'mood': 'не выжил',
            'exam': 'Математика',
        },
    ]
}

FOUR_ROWS = {
    'Антон Амперян': [
        {
            'date': '2024-06-01',
            'coffee_spent': '600',
            'sleep_hours': '2.5',
            'study_hours': '17',
            'mood': 'зомби',
            'exam': 'Математика',
        },
        {
            'date': '2024-06-02',
            'coffee_spent': '650',
            'sleep_hours': '4.0',
            'study_hours': '12',
            'mood': 'отлично',
            'exam': 'Физика',
        },
        {
            'date': '2024-06-03',
            'coffee_spent': '700',
            'sleep_hours': '2.0',
            'study_hours': '18',
            'mood': 'не выжил',
            'exam': 'Математика',
        },
        {
            'date': '2024-06-04',
            'coffee_spent': '750',
            'sleep_hours': '2.0',
            'study_hours': '18',
            'mood': 'не выжил',
            'exam': 'Математика',
        },
    ]
}

TWO_STUDENTS = TWO_ROWS.copy()
TWO_STUDENTS.update(THREE_ROWS)


@pytest.mark.parametrize(
        ['dict_rows', 'exp_res'],
        [
            (ONE_ROW, [('Иван Кузнецов', 600)]),
            (TWO_ROWS, [('Джузеппе Бальзамо', 625)]),
            (THREE_ROWS, [('Кристобаль Хунта', 650)]),
            (FOUR_ROWS, [('Антон Амперян', 675)]),
        ]
)
def test_calculate_median_coffee(dict_rows, exp_res):
    """Проверяет функцию get_median_coffee на корректность расчёта медианы."""
    res = get_median_coffee(dict_rows)
    assert res == exp_res


def test_sort_report():
    """Проверяет функцию get_median_coffee. Сортировка по убыванию медианы."""
    res = get_median_coffee(TWO_STUDENTS)
    print(res)
    assert res == [('Кристобаль Хунта', 650), ('Джузеппе Бальзамо', 625),]


def test_return_tupe():
    """Проверяет функцию get_median_coffee. Возвращает список кортежей."""
    res = get_median_coffee(ONE_ROW)
    assert isinstance(res, list)
    assert isinstance(res[0], tuple)
