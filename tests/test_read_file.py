import csv
import pathlib

import pytest

from report_coffee.read_file import get_students_info

TEST_DIR = pathlib.Path(__file__).resolve().parent

CONTEXT = '''
        student,date,coffee_spent,sleep_hours,study_hours,mood,exam
        Алексей Смирнов,2024-06-01,450,4.5,12,норм,Математика
        Алексей Смирнов,2024-06-02,500,4.0,14,устал,Математика
        Алексей Смирнов,2024-06-03,550,3.5,16,зомби,Математика
        Дарья Петрова,2024-06-01,200,7.0,6,отл,Математика
        Дарья Петрова,2024-06-02,250,6.5,8,норм,Математика
        Дарья Петрова,2024-06-03,300,6.0,9,норм,Математика
        Иван Кузнецов,2024-06-01,600,3.0,15,зомби,Математика
        Иван Кузнецов,2024-06-02,650,2.5,17,зомби,Математика
        Иван Кузнецов,2024-06-03,700,2.0,18,не выжил,Математика
        Мария Соколова,2024-06-01,100,8.0,3,отл,Математика
        Мария Соколова,2024-06-02,120,8.5,2,отл,Математика
        Мария Соколова,2024-06-03,150,7.5,4,отл,Математика
        Павел Новиков,2024-06-01,380,5.0,10,норм,Математика
        Павел Новиков,2024-06-02,420,4.5,11,устал,Математика
        Павел Новиков,2024-06-03,470,4.0,13,устал,Математика
        Елена Волкова,2024-06-01,280,6.0,8,норм,Математика
        Елена Волкова,2024-06-02,310,5.5,9,норм,Математика
        Елена Волкова,2024-06-03,340,5.0,10,устал,Математика
'''


@pytest.fixture(scope='module')
def create_files():
    """Фикстура для создания тестовых файлов с данными о студентах."""
    empty_file = TEST_DIR/'empty_file.csv'
    empty_file.touch()

    for i in range(1, 4):
        file_name = f'test_file{i}.csv'
        with open(TEST_DIR/file_name, mode='w', encoding='utf-8') as f:
            writer = csv.writer(f, delimiter=',', lineterminator='\n')
            rows_lst = CONTEXT.strip().split('\n')
            headers = rows_lst[0].split(',')
            writer.writerow(headers)
            middle = len(rows_lst) // 2
            if i == 1:
                writer.writerows(
                    [row.strip().split(',') for row in rows_lst[1:middle]]
                )
            elif i == 2:
                writer.writerows(
                    [row.strip().split(',') for row in rows_lst[middle:]]
                )
            else:
                writer.writerows(
                    [row.strip().split(',') for row in rows_lst[1:]]
                )

    yield

    for i in range(1, 4):
        file_name = f'test_file{i}.csv'
        (TEST_DIR/file_name).unlink()
    (TEST_DIR/empty_file).unlink()


@pytest.mark.parametrize(
        ['file_names', 'exp_res'],
        [
            ([TEST_DIR/'test_file1.csv'], 3),
            ([
                TEST_DIR/'test_file1.csv',
                TEST_DIR/'test_file2.csv',
                TEST_DIR/'test_file3.csv'
            ], 6),
        ]
)
def test_read_one_file(create_files, file_names, exp_res):
    """Проверка чтения одного и нескольких файлов."""
    res = get_students_info(file_names)
    assert len(res) == exp_res


def test_return_type(create_files):
    """
    Проверка возвращаемых типов.

    Функция возвращает словарь, значение каждого ключа - список.
    """
    files = [
        TEST_DIR/'test_file1.csv',
        TEST_DIR/'test_file2.csv',
    ]
    res = get_students_info(files)
    assert isinstance(res, dict)
    assert isinstance(list(res.values())[0], list)
    # assert all([isinstance(value, list) for value in res.values()])


def test_empty_file(create_files):
    """Проверка, если файл пустой, функция возвращает пустой словарь."""
    file = TEST_DIR/'empty_file.csv'
    res = get_students_info([file])
    assert res == {}


def test_one_student_in_dif_files(create_files):
    """
    Проверка, если один студент указан в разных файлах,

    его данные объединяются в одном списоке.
    """
    files = [
            TEST_DIR/'test_file1.csv',
            TEST_DIR/'test_file2.csv',
            TEST_DIR/'test_file3.csv'
    ]
    res = get_students_info(files)
    assert len(res['Иван Кузнецов']) == 6
