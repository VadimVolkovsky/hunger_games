# C. Реализовать функцию с помощью методов map и lambda. 
# Функция принимает список элементов (состоящий из строк и цифр), 
# возвращает новый список, с условием - если элемент списка был строкой, 
# в начало строки нужно добавить текст "abc_", в конец строки - "_cba". 
# Если элемент был int - то его значение нужно возвести в квадрат. 
# Результат вывести в консоль.


data = [
    2,
    "klukva",
    "smorodina",
    "klubnika",
    4,
    "malina",
]

roater = {
    int: lambda x: x**2,
    str: lambda x: "abc_" + x + "_cba",
}


def upgrade_element(element):
    """Возвращает значение по ключу из словаря router"""
    return roater.get(type(element), int)(element)


result = list(map(upgrade_element, data))
print(result)
