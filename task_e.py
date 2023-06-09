# E. Написать класс, принимающий на вход текст.
# Один метод класса должен выводить в консоль самое длинное слово в тексте.
# Второй метод - самое часто встречающееся слово.
# Третий метод выводит количество спецсимволов
# в тексте (точки, запятые и так далее).
# Четвертый метод выводит все палиндромы через запятую.

from task_f import time_of_function
from testdata import TASK_E_SPEC_CHAR as SPEC_CHAR
from testdata import TASK_E_TEXT as text
from validation import validate_is_str


class TextEditor:

    def __init__(self, text: str):
        self.text = text

    @time_of_function
    def get_the_longest_word(self) -> str:
        """Выводит самое длинное слово в тексте"""
        validate_is_str(self.text)
        text_list = self.text.split()
        longest_word = max(text_list, key=len)
        return longest_word

    @time_of_function
    def get_most_frequent_word(self) -> str:
        """Выводит самое часто встречающееся слово"""
        validate_is_str(self.text)
        text_list = self.text.lower().split()
        count_dict = {}
        for word in text_list:
            if word in count_dict:
                count_dict[word] += 1
            else:
                count_dict[word] = 1
        return max(count_dict, key=count_dict.get)

    @time_of_function
    def get_sum_of_special_characters(self) -> int:
        """Выводит количество спецсимволов в тексте"""
        validate_is_str(self.text)
        counter = 0
        text_list = list(self.text)
        for char in text_list:
            if char in SPEC_CHAR:
                counter += 1
        return counter

    @time_of_function
    def get_all_palindroms(self) -> str:
        """Выводит список всех палиндромов в тексте"""
        validate_is_str(self.text)
        cleaned_text = self._clean_text(self.text).split()
        palindroms = self._check_is_word_palindrom(cleaned_text)
        palindroms = ", ".join(palindroms)
        return palindroms

    def _clean_text(self, text: str) -> str:
        """Убирает из текста спецсимволы"""
        cleaned_text = text.lower()
        for char in SPEC_CHAR:
            cleaned_text = cleaned_text.replace(char, "")
        return cleaned_text

    def _check_is_word_palindrom(self, words: list) -> list:
        """Проверяет список слов на палиндромность"""
        palindroms = []
        for word in words:
            if word == word[::-1] and len(word) > 2:
                palindroms.append(word)
        return palindroms


textedit = TextEditor(text)
