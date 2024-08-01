# Практическое задание по теме: "Словари и множества"

# Цель: Написать программу на языке Python, используя Pycharm, для работы со словарями и множествами.
#
# 1. В проекте, где вы решаете домашние задания, создайте модуль 'module_1_6.py' и напишите весь код в нём.
#
# 2. Работа со словарями:
#   - Создайте переменную my_dict и присвойте ей словарь из нескольких пар ключ-значение.
# Например: Имя(str)-Год рождения(int).
#   - Выведите на экран словарь my_dict.
#   - Выведите на экран одно значение по существующему ключу, одно по отсутствующему из словаря my_dict без ошибки.
#   - Добавьте ещё две произвольные пары того же формата в словарь my_dict.
#  - Удалите одну из пар в словаре по существующему ключу из словаря my_dict и выведите значение из этой пары на экран.
#   - Выведите на экран словарь my_dict.
#
# Примечания:
# - Для вывода значений на экран используйте функцию print().
# - Помните, что словарь и множество - неупорядоченные коллекции.
# - Больше о методах словарей тут, множеств тут.

var_1 = "Max"
var_2 = "Oleg"
var_3 = "Iosif"
var_4 = "Nikita"
var_5 = "New Key1"
var_6 = "New Key2"
val_1 = 1994
val_2 = 1995
val_3 = 1996
val_4 = 1997
val_5 = 1998
val_6 = 1999
my_dict = {var_1 : val_1,
           var_2 : val_2,
           var_3 : val_3,
           var_4 : val_4   }                                                  #   - Создайте переменную my_dict и присвойте ей словарь из нескольких пар ключ-значение.
print("Первичный словарь")
print(my_dict)                                                                #   - Выведите на экран словарь my_dict.
print()

print("По ключу Max выводится значение ", my_dict.get(var_1))                 #  Выведите на экран одно значение по существующему ключу
print("По несуществующему ключу выводится значение ", my_dict.get("Key"))     #  Выведите на экран одно значение по НЕсуществующему ключу

my_dict.update ( {var_5 : val_5,
                  var_6 : val_6})                                             #   - Добавьте 2 произвольных элемента в множество my_set, которых ещё нет.
#print(my_dict)                                                               #   - словарь my_dict + 2 new keys
popedkey = my_dict.pop(var_2)                                                 #  Удалите одну из пар в словаре по существующему ключу из словаря my_dict и
print("Удаленное значение : ", popedkey)                                      #  Bыведите значение из этой пары на экран
print("Обновленный словарь")
print(my_dict)


# 3. Работа с множествами:
#   - Создайте переменную my_set и присвойте ей множество, состоящее из разных типов данных с повторяющимися значениями.
#   - Выведите на экран множество my_set (должны отобразиться только уникальные значения).   # почему?
#   - Добавьте 2 произвольных элемента в множество my_set, которых ещё нет.
#   - Удалите один любой элемент из множества my_set.
#   - Выведите на экран измененное множество my_set.
#
print()
print("Блок 3")
print()
# case_1 = 2.34
# case_2 = True
# case_3 = 25
# case_4 = "Admin"
# case_5 = [1, 2, 3, 4, 5, 6, 7, 25]
# case_6 = (3, 12, 2.34, 5, [6, 7, "albinos"])
# my_set = {case_1, case_2, case_3, case_4, case_1, case_6, case_5, case_2, case_3}      # понял в чем проблема. нельзя использовать изменяемые элементы, т.е. [] list  
my_set = {1, 1, 2, 2, 3, 4, 5, 12, 17, 24, 1.0, 1.4, "Joker", True, 1, (18, 3, 2, 1, "String")}
print("почему у меня в компиляторе без 'set' стаются уникальные значения, без дублей?")  # все равно не понятно почему без параметра set остаются лишь уникальные значения.
print(my_set)
my_set.add("To be or not to be" )                   #   - Добавьте 2 произвольных элемента в множество my_set, которых ещё нет.
my_set.add(13)                                      #   - Добавьте 2 произвольных элемента в множество my_set, которых ещё нет.
print(my_set)
my_set.discard(1)                                   #   - Удалите один любой элемент из множества my_set.
print(my_set)                                       #   - Выведите на экран измененное множество my_set.













# Пример результата выполнения программы:
# Dict: {'Vasya': 1975, 'Egor': 1999, 'Masha': 2002}
# Existing value: 2002
# Not existing value: None
# Deleted value: 1999
# Modified dictionary: {'Vasya': 1975, 'Kamila': 1981, 'Artem': 1915, 'Masha': 2002}
#
# Set: {1, 'Яблоко', 42.314}
# Modified set: {'Яблоко', 42.314, 13, (5, 6, 1.6)}