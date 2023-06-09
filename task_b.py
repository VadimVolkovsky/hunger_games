# B. Реализовать функцию, принимающую два списка и возвращающую 
# словарь (ключ из первого списка, значение из второго), 
# упорядоченный по ключам. Результат вывести в консоль. 
# Длина первого списка не должна быть равна длине второго. 
# Результат вывести в консоль.


from collections import OrderedDict


list_1 = [
    "c",
    "b",
    "a",
    "d",
]

list_2 = [
    "1",
    "2",
    "3",
    "4",
    "5"
]


def make_dict_from_lists(list_1: list, list_2: list) -> dict:
    for i in range(len(list_1)):
        result = dict(zip(list_1, list_2))
        sorted_result = sorted(result.items(), key=lambda x: x[0])
    print(sorted_result)


make_dict_from_lists(list_1, list_2)
