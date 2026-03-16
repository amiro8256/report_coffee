import csv


def get_students_info(files: list[str]) -> dict[str, list[dict]]:
    """Функция собирает данные о всех студентах из разных файлов.

        Возвращает словарь: {
            'name': [
                {'coffee_spent': str,
                'date': str,
                'exam': str,
                'mood': str,
                'sleep_hours': str,
                'study_hours': str,},
                {...},
                ]
            'name': [
                {...},
                {...},
                ]
            }
    """
    students_data = {}
    for csv_file in files:
        with open(csv_file, encoding='UTF-8', newline='') as file:
            csv_reader = csv.DictReader(file)

            for row in csv_reader:
                name_student = row.pop('student')
                if name_student not in students_data:
                    students_data[name_student] = [row]
                else:
                    students_data[name_student].append(row)
    return students_data
