# # Дополнительное практическое задание по модулю: "Подробнее о функциях."

data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

def calculate_structure_sum(args):
    counter = 0
    if isinstance(args, list):
        for i in args:
            counter += calculate_structure_sum(i)
    elif isinstance(args, dict):
        for key, value in args.items():
            counter += calculate_structure_sum(value)
            counter += calculate_structure_sum(key)
    elif isinstance(args, tuple):
        for i in args:
            counter += calculate_structure_sum(i)
    elif isinstance(args, set):
        for i in args:
            counter += calculate_structure_sum(i)
    elif isinstance(args, str):
        counter += len(args)
    elif isinstance(args, int):
        counter += args
    else:
        return 0
    return counter


result = calculate_structure_sum(data_structure)
print(result)



# def test_(*args):
#     simple = False
#     if not args:
#        return 0
#     elif type(args) == list or type(args) == dict or type(args) == tuple or type(args) ==  set or type(args) == bool:
#         simple = False
#         return simple
#     elif type(args) == int or type(args) == str or type(args) == float:
#         simple = True
#         return simple

# test_(data_structure)
# print('fortest')
    
# def recurs_check(main, args):
#    if test_(args) in main == True:
#       return args
#    elif test_(args) in main == False:
      
# def unpack(*args):
#   for i in args:
#       if test_(i) == True:
#         return i
#       elif test_(i) == False:
#           for j in i:
#              if test_(j) == True:
#                 return j
#              elif test_(j) == False:
#                 for k in j:
#                    if test
#       else:
#         pass
#         return i


# # int()  --> int(input())
# # float()
# # bool()
# # str()
# # list()
# # tuple()
# # dict()
# # set()

# def calculate_structure_sum(*args):
#     new_list = []
#     counter = 0
#     for i in args:
#       if test_(i) == False:
#           for j in i:                              
#             pass

# #               elif isinstance(*j, int) == True:
# #                   counter += j
# #                   return counter
# #               elif isinstance(*j, str) == True:
# #                   counter += len(j)
# #                   return counter
# #               else: 
# #                   counter += calculate_structure_sum(i)
# #                   return counter

# #       elif type(i) == dict:
# #           for key, value in i.items():
# #               if type(value) == int and type(key) == str:
# #                   counter += value
# #                   counter += len(key)
# #                   return counter
# #               elif type(value) != int and type(key) == str:
# #                   counter += calculate_structure_sum(value)
# #                   counter += len(key)
# #                   return counter
# #               elif type(value) == int and type(key) != str:
# #                   counter += calculate_structure_sum(key)
# #                   counter += value
# #                   return counter
# #               else: 
# #                   counter += calculate_structure_sum(key)
# #                   counter += calculate_structure_sum(value)
# #                   return counter

# #       elif type(i) == tuple:
# #           for j in i:
# #               if isinstance(j, int) == True:
# #                   counter += j
# #               elif isinstance(j, str) == True:
# #                   counter += len(j)
# #               else: 
# #                   counter += calculate_structure_sum(i)

# # print(calculate_structure_sum(data_structure))
                  
# #       # elif what_type_is_it(i) == tuple:
      
# #       # elif what_type_is_it(i) == dict:
      
# #       # elif what_type_is_it(i) == int:
      
# #       # elif what_type_is_it(i) == bool:
      
# #       # elif what_type_is_it(i) == str:
      
# #       # elif what_type_is_it(i) == set:
      
# result = calculate_structure_sum(data_structure)
# print(result)


# #Задание "Раз, два, три, четыре, пять .... Это не всё?":
# Наши студенты, без исключения, - очень умные ребята. Настолько умные, что иногда по утру сами путаются в том, что намудрили вчера вечером.
# Один из таких учеников уснул на клавиатуре в процессе упорной учёбы (ещё и трудолюбивые). Тем не менее, даже после сна, его код остался рабочим и выглядел следующим образом:

# data_structure = [
#   [1, 2, 3],
#   {'a': 4, 'b': 5},
#   (6, {'cube': 7, 'drum': 8}),
#   "Hello",
#   ((), [{(2, 'Urban', ('Urban2', 35))}])
# ]

# Увидев это студент задался вопросом: "А есть ли универсальное решение для подсчёта суммы всех чисел и длин всех строк?"
# Да, выглядит страшно, да и обращаться нужно к каждой внутренней структуре (списку, словарю и т.д.) по-разному.

# Ученику пришлось каждый раз использовать индексацию и обращение по ключам - универсального решения для таких структур он не нашёл.

# Помогите сокурснику осуществить его задумку.

# Что должно быть подсчитано:
# Все числа (не важно, являются они ключами или значениям или ещё чем-то).
# Все строки (не важно, являются они ключами или значениям или ещё чем-то)

# Для примера, указанного выше, расчёт вёлся следующим образом:
# 1 + 2 + 3 + len('a') + 4 + len('b') + 5 + 6 + len('cube') + 7 + .... + 35 = 99

# Входные данные (применение функции):
# data_structure = [
# [1, 2, 3],
# {'a': 4, 'b': 5},
# (6, {'cube': 7, 'drum': 8}),
# "Hello",
# ((), [{(2, 'Urban', ('Urban2', 35))}])
# ]

# result = calculate_structure_sum(data_structure)
# print(result)


# Выходные данные (консоль):
# 99


# Примечания (рекомендации):
# Весь подсчёт должен выполняться одним вызовом функции.
# Рекомендуется применить рекурсивный вызов функции, для каждой внутренней структуры.
# Т.к. каждая структура может содержать в себе ещё несколько элементов, можно использовать параметр *args
# Для определения типа данного используйте функцию isinstance.