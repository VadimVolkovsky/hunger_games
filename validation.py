import logging

from exceptions import (EMPTY_LIST_EXCEPTION, NOT_A_LIST_EXCEPTION,
                        NOT_INT_OR_STR_EXCEPTION, NOT_STR_EXCEPTION,
                        EmptyListException, NotListException, NotStrException,
                        NotStrOrIntException)


def validate_is_list(data: list) -> None:
    if not isinstance(data, list):
        logging.warning(NOT_A_LIST_EXCEPTION)
        raise NotListException(NOT_A_LIST_EXCEPTION)


def validate_not_empty_list(data: list) -> None:
    if not data:
        logging.warning(EMPTY_LIST_EXCEPTION)
        raise EmptyListException(EMPTY_LIST_EXCEPTION)


def validate_not_int_or_str(element):
    if not isinstance(element, (str, int)):
        logging.warning(NOT_INT_OR_STR_EXCEPTION)
        print(f'Передан: {type(element)}')
        print(f'Передан: {element}')
        raise NotStrOrIntException(NOT_INT_OR_STR_EXCEPTION)


def validate_is_str(element):
    if not isinstance(element, str):
        logging.warning(NOT_STR_EXCEPTION)
        raise NotStrException(NOT_STR_EXCEPTION)
