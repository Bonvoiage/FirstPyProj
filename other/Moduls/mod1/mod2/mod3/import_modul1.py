# # from mod1 import modul1
# # from mod1.func1 import func_module1
# #
# #
# #
# # func_module1()



# import sys
# import os

# # Указываем абсолютный путь к директории, где лежит нужный файл
# module_path = r"D:\Urb\FirstPyProj\module_2\sub_2_3"

# # Добавляем этот путь в sys.path
# if module_path not in sys.path:
#     sys.path.append(module_path)

# # Теперь можно импортировать переменную "a" из 01.py
# from module_2_3 import my_list

# print(my_list)

from ....mod1 import func1 as f1

f1.func_module1()