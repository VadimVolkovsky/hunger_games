# E. Написать класс, принимающий на вход текст. 
# Один метод класса должен выводить в консоль самое длинное слово в тексте. 
# Второй метод - самое часто встречающееся слово. 
# Третий метод выводит количество спецсимволов в тексте (точки, запятые и так далее). 
# Четвертый метод выводит все палиндромы через запятую.

text = "Rubytech – системный интегратор и ИТ-партнер корпораций, системообразующих организаций, мадам, государства, казак. Компания дед реализует комплексные шалаш проекты по импортозамещению, обеспечению Abba информационной безопасности, проектированию и внедрению центров обработки данных, созданию корпоративных хранилищ, внедрению сетевой инфраструктуры, внедрению мультимедиа. "
SPEC_CHAR = [",", ".", "@", "!", "?", "&", "_", "-", "/", "–"]


class TextEditor:

    def __init__(self, text: str):
        self.text = text

    def get_the_longest_word(self) -> str:
        """Выводит самое длинное слово в тексте"""
        text_list = self.text.split()
        longest_word = max(text_list, key=len)
        return longest_word

    def get_most_frequent_word(self) -> str:
        """Выводит самое часто встречающееся слово"""
        text_list = self.text.lower().split()
        count_dict = {}
        for word in text_list:
            if word in count_dict:
                count_dict[word] += 1
            else:
                count_dict[word] = 1
        return max(count_dict, key=count_dict.get)

    def get_sum_of_special_characters(self) -> int:
        """Выводит количество спецсимволов в тексте"""
        counter = 0
        text_list = list(self.text)
        for char in text_list:
            if char in SPEC_CHAR:
                counter += 1
        return counter

    def get_all_palindroms(self) -> str:
        """Выводит список всех палиндромов в тексте"""
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
        palindroms = []
        for word in words:
            if word == word[::-1] and len(word) > 2:
                palindroms.append(word)
        return palindroms


textedit = TextEditor(text)


longest_word = textedit.get_the_longest_word()
print(f'Самое длинное слово: {longest_word}')

frequent_word = textedit.get_most_frequent_word()
print(f'Самое часто встречающееся слово: {frequent_word}')

spec_char_sum = textedit.get_sum_of_special_characters()
print(f'Количество спецсимволов в тексте: {spec_char_sum}')

all_palindroms = textedit.get_all_palindroms()
print(f'Слова палиндромы в тексте: {all_palindroms}')
