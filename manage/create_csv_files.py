import csv
import pathlib

BASE_DIR = pathlib.Path(__file__).resolve().parent.parent

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


def create_files():
    """Функция для создания тестовых файлов с данными о студентах."""
    file_names = []
    for i in range(1, 4):
        file_name = f'test_file{i}.csv'
        file_names.append(file_name)
        with open(BASE_DIR/file_name, mode='w', encoding='utf-8') as f:
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
    print(
        f'Созданы файлы {', '.join(file_names)}. Что бы выполнить отчёт,'
        f' запустите main.py с этими файлами в аргументах из корня проекта.'
    )


if __name__ == '__main__':
    create_files()