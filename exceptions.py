NOT_A_LIST_EXCEPTION = 'В функцию был передан не список'
EMPTY_LIST_EXCEPTION = "В функцию был передан пустой список"
NOT_INT_OR_STR_EXCEPTION = (
    "Проверьте тип элемента в списке. "
    "Можно передавать только int и str"
)
NOT_STR_EXCEPTION = 'В функцию была передана не строка'


class NotListException(Exception):
    pass


class NotStrException(Exception):
    pass


class NotStrOrIntException(Exception):
    pass


class EmptyListException(Exception):
    pass
