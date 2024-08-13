# #from test_module.module_1_5 import mutable_list
import sys
sys.path.insert(1, "module_2")
from sub_2_2.module_2_2 import first



# print (stone_range)
# print ()
# print ()

# # print(isinstance(stone_range, (str, int, list, tuple)))

# print()
# print ()


# from test_module.module_1_5 import mutable_list


# # print(mutable_list)


# import sys
# # import os

# # Указываем абсолютный путь к директории, где лежит нужный файл
# # module_path = r"D:\Urb\FirstPyProj\module_4"

# # Добавляем этот путь в sys.path
# # if module_path not in sys.path:
# #     sys.path.append(module_path)

# # # Теперь можно импортировать переменную "a" из 01.py
# # from func1 import func_module1

# # func_module1()

for path in sys.path:
    print(path)