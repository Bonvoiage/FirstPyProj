# def func_with_params(a = 2, b = 2):
#     print(a + b)


# def func_with_params(a, b = 2):  # можем так сделать, но значение по умолчанию может быть только после
#     print(a + b)


# def func_with_params(a, b = 2, c = []):
#     c.append(a)
#     print(c)                                    # добавляет в уже существующий список


def func_with_params(a, b = 2, c = None):
    if c == None:
        c = []
        c.append(a)
    else:
        pass
    print(c)                                    # добавляет в новый список


func_with_params(12)

func_with_params(11)

func_with_params(13)

func_with_params(14)