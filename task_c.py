# C. Реализовать функцию с помощью методов map и lambda.
# Функция принимает список элементов (состоящий из строк и цифр),
# возвращает новый список, с условием - если элемент списка был строкой,
# в начало строки нужно добавить текст "abc_", в конец строки - "_cba".
# Если элемент был int - то его значение нужно возвести в квадрат.
# Результат вывести в консоль.


from validation import (validate_is_list, validate_not_empty_list,
                        validate_not_int_or_str)

roater = {
    int: lambda x: x**2,
    str: lambda x: "abc_" + x + "_cba",
}


def check_and_update_element(element: int | str) -> int | str:
    validate_not_int_or_str(element)
    return roater.get(type(element), int)(element)


def upgrade_element(data: list) -> list:
    """Возвращает обновленный элемент в зависимости
    от его типа (str или int)"""
    validate_is_list(data)
    validate_not_empty_list(data)
    return list(map(check_and_update_element, data))
