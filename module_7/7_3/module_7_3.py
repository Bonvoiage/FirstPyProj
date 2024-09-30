# Домашнее задание по теме "Оператор "with".



#Я работаю в VSCode мне необходимо писать путь каждый раз при работе с открытием. либо я банально не знаю как по другому.
# universal_file_name = 'module_7/7_3/files_for_module_7_3_new/'

# test01 = universal_file_name + 'file1.txt'
# file_test01 = open(test01, 'w', encoding='utf-8')
# file_test01.write("Hello, World!")
# file_test01.close()

# def write_file(*file_names):
#     list_names = []
#     for file_name in file_names:
#         if file_name in list_names:
#             continue
#         if file_name not in list_names:
#             list_names.append(file_name)
#     return list_names


universal_file_name = 'module_7/7_3/files_for_module_7_3_new/'
class WordsFinder:
    
    punctuation_marks = [',', '.', '=', '!', '?', ';', ':', ' - ']

    def __init__(self, *file_names):
        # self.file_name_raw = []
        # self.file_name_raw = write_file(file_names)
        self.file_names = []
        for file_name in file_names:
            if file_name in self.file_names:
                continue
            if file_name not in self.file_names:
                self.file_names.append(universal_file_name + file_name)

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                content = file.read().lower()  
                for mark in self.punctuation_marks:
                    content = content.replace(mark, '')  
                all_words[file_name] = content.split()  
        return all_words
    
    def find(self, word : str):
        all_words = self.get_all_words()
        lower_word = word.lower()
        for file_name in all_words:
            if lower_word in all_words[file_name]:
                position = all_words[file_name].index(lower_word)
                return (f"""
В документе '{file_name}'
{word} находится в позиции
{position + 1} слово по счёту
 """)
            else:
                return "Такого слова нет"
        

    def count(self, word : str):
        all_words = self.get_all_words()
        lower_word = word.lower()
        count = 0
        for file_name in all_words:
            list_of_words = all_words.values()
            for i in list_of_words:
                for j in i:
                    if lower_word == j:
                        count += 1
                    else:
                        continue
                else:
                    continue
                # можно было доавить сюда 
            # return f"В файле "{file_name}" Слово '{word}' в тексте всего {count} раза" 
            #но получается очень длинно
            return f"Слово '{word}' в тексте всего {count} раза"



# text_file1 = WordsFinder("file1.txt")
# print(text_file1.get_all_words())

finder2 = WordsFinder('file1.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего










# Цель: применить на практике оператор with, вспомнить написание кода в парадигме ООП.

# Задача "Найдёт везде":
# Напишите класс WordsFinder, объекты которого создаются следующим образом:
# WordsFinder('file1.txt, file2.txt', 'file3.txt', ...).
# Объект этого класса должен принимать при создании неограниченного количество названий файлов и записывать их в атрибут file_names в виде списка или кортежа.

# Также объект класса WordsFinder должен обладать следующими методами:
# get_all_words - подготовительный метод, который возвращает словарь следующего вида:
# {'file1.txt': ['word1', 'word2'], 'file2.txt': ['word3', 'word4'], 'file3.txt': ['word5', 'word6', 'word7']}
# Где:
# 'file1.txt', 'file2.txt', ''file3.txt'' - названия файлов.
# ['word1', 'word2'], ['word3', 'word4'], ['word5', 'word6', 'word7'] - слова содержащиеся в этом файле.
# Алгоритм получения словаря такого вида в методе get_all_words:
# Создайте пустой словарь all_words.
# Переберите названия файлов и открывайте каждый из них, используя оператор with.
# Для каждого файла считывайте единые строки, переводя их в нижний регистр (метод lower()).
# Избавьтесь от пунктуации [',', '.', '=', '!', '?', ';', ':', ' - '] в строке. (тире обособлено пробелами, это не дефис в слове).
# Разбейте эту строку на элементы списка методом split(). (разбивается по умолчанию по пробелу)
# В словарь all_words запишите полученные данные, ключ - название файла, значение - список из слов этого файла.

# find(self, word) - метод, где word - искомое слово. Возвращает словарь, где ключ - название файла, значение - позиция первого такого слова в списке слов этого файла.
# count(self, word) - метод, где word - искомое слово. Возвращает словарь, где ключ - название файла, значение - количество слова word в списке слов этого файла.
# В методах find и count пользуйтесь ранее написанным методом get_all_words для получения названия файла и списка его слов.
# Для удобного перебора одновременно ключа(названия) и значения(списка слов) можно воспользоваться методом словаря - item().

# for name, words in get_all_words().items():
#   # Логика методов find или count

# Пример результата выполнения программы:
# Представим, что файл 'test_file.txt' содержит следующий текст:


# Пример выполнения программы:
# finder2 = WordsFinder('test_file.txt')
# print(finder2.get_all_words()) # Все слова
# print(finder2.find('TEXT')) # 3 слово по счёту
# print(finder2.count('teXT')) # 4 слова teXT в тексте всего

# Вывод на консоль:
# {'test_file.txt': ["it's", 'a', 'text', 'for', 'task', 'найти', 'везде', 'используйте', 'его', 'для', 'самопроверки', 'успехов', 'в', 'решении', 'задачи', 'text', 'text', 'text']}
# {'test_file.txt': 3}
# {'test_file.txt': 4}

# Запустите этот код с другими примерами предложенными здесь.
# Если решение верное, то результаты должны совпадать с предложенными.

# Примечания:
# Регистром слов при поиске можно пренебречь. ('teXT' ~ 'text')
# Решайте задачу последовательно - написав один метод, проверьте результаты его работы.

# Файл module_7_3.py и загрузите его на ваш GitHub репозиторий. В решении пришлите ссылку на него.
# Успехов!
