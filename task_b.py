# B. Реализовать функцию, принимающую два списка и возвращающую
# словарь (ключ из первого списка, значение из второго),
# упорядоченный по ключам. Результат вывести в консоль.
# Длина первого списка не должна быть равна длине второго.
# Результат вывести в консоль.


from validation import validate_is_list


def make_dict_from_lists(data_1: list, data_2: list) -> dict:
    """Функция принимает два списка и возвращает
    словарь отсортированный по ключам"""
    validate_is_list(data_1)
    validate_is_list(data_2)
    for i in range(len(data_1)):
        result = dict(zip(data_1, data_2))
        sorted_result = dict(sorted(result.items(), key=lambda x: x[0]))
    return sorted_result
