from statistics import median


def get_median_coffee(students_info: dict[str, list[dict]]) -> list[tuple]:
    """
    Функция получает медиану затрат на кофе для каждого уникального студента.
    """
    students_coffee = []
    for name, info in students_info.items():
        prices_coffee = []
        for detailed_info in info:
            prices_coffee.append(int(detailed_info['coffee_spent']))

        prices_coffee.sort()
        avg_price = median(prices_coffee)
        students_coffee.append((name, avg_price))

    students_coffee.sort(key=lambda x: x[1], reverse=True)
    return students_coffee
