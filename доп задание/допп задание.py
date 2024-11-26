def my_count(l: list, item):
    """
    Функция для подсчёта числа вхождения элементов  список
    """

    cnt = 0  # Создаём счётчик для подсчёта элементов

    for element in l:  # Начинаем проходить по всему списку
        if element == item:
            # Если находим нужный элемент, то увеличиваем значение счётчика
            cnt += 1
    return cnt


"""
Проверка работоспособности функции
"""
numbers = [1, 2, 2, 3, 2, 4, 3, 2, 5, 4, 4]

print(my_count(numbers, 2))
print(my_count(numbers, 3))
print(my_count(numbers, 6))
