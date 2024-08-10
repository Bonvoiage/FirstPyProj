#from test_module.module_1_5 import mutable_list
from module_2.Additional_test_module_2 import stone_range

print ()
print ()
print ()

print(isinstance(stone_range, (str, int, list, tuple)))

print()
print (stone_range)


from test_module.module_1_5 import mutable_list


# print(mutable_list)


# import sys
# import os

# # Указываем абсолютный путь к директории, где лежит нужный файл
# module_path = r"D:\Urb\FirstPyProj\other\Moduls\mod1"

# # Добавляем этот путь в sys.path
# if module_path not in sys.path:
#     sys.path.append(module_path)

# # Теперь можно импортировать переменную "a" из 01.py
# from func1 import func_module1

# func_module1()