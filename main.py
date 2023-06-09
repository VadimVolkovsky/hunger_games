import logging

from constants import (TASK_A_TITLE, TASK_B_TITLE, TASK_C_TITLE, TASK_D_TITLE,
                       TASK_E_ALL_PALINDROMS_TITLE, TASK_E_FREQUENT_WORD_TITLE,
                       TASK_E_LONGEST_WORD_TITLE, TASK_E_SPEC_CHAR_SUM_TITLE,
                       TASK_E_TITLE)
from logging_config import configure_logging
from task_a import get_projects_names
from task_b import make_dict_from_lists
from task_c import upgrade_element
from task_d import send_async_requests
from task_e import textedit
from testdata import TASK_A_URLS, TASK_B_DATA_1, TASK_B_DATA_2, TASK_C_DATA_1


def main():
    projects_names = get_projects_names(TASK_A_URLS)
    logging.info(f'{TASK_A_TITLE} {projects_names}')

    sorted_result = make_dict_from_lists(TASK_B_DATA_1, TASK_B_DATA_2)
    logging.info(f'{TASK_B_TITLE} {sorted_result}')

    upgraded_list = upgrade_element(TASK_C_DATA_1)
    logging.info(f'{TASK_C_TITLE} {upgraded_list}\n')

    logging.info(TASK_D_TITLE)
    send_async_requests()

    logging.info(TASK_E_TITLE)
    longest_word = textedit.get_the_longest_word()
    logging.info(f'{TASK_E_LONGEST_WORD_TITLE} {longest_word}')

    frequent_word = textedit.get_most_frequent_word()
    logging.info(f'{TASK_E_FREQUENT_WORD_TITLE} {frequent_word}')

    spec_char_sum = textedit.get_sum_of_special_characters()
    logging.info(f'{TASK_E_SPEC_CHAR_SUM_TITLE} {spec_char_sum}')

    all_palindroms = textedit.get_all_palindroms()
    logging.info(f'{TASK_E_ALL_PALINDROMS_TITLE} {all_palindroms}')


if __name__ == "__main__":
    configure_logging()
    main()
