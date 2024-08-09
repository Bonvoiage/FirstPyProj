# Способы вызова функции по умолчанию
# def print_params(a, b, c):
#     print(a, b, c)
#     print(a + b)


# #print_params(1, 2, 3)
# print_params("True", True, 3)


# def print_params(a = 1, b = 2, c = 3):
#     print(a, b, c)


# #print_params(1, 2, 3)
# # print_params(1, 2, c = "stroke")
# print_params(b = True, c = "stroke", a = 12)
# print_params(c = "stroke", 1, 2)   # Нельзя так, ошибка


def print_params(a, *, b, c):
    print(a, b, c)


# print_params(1, 2, 3)   # ошибка, нужно чтобы b и c были именованы
print_params(1, b = True, c = False)
