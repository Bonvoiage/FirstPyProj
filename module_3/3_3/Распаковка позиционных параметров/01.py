# def print_params (*params):  #*args, **kwargs
#     print (params)


# def print_params (*params):  #*args, **kwargs
#     print (*params)
# print_params(1, 2, 3, 4, 5, 6, 7)


# def print_params (a, b, c):  #*args, **kwargs
#     print (a, b, c)
# list_ = [1, 2, 3]
# print_params(list_, 1, 1)


# def print_params (a, b, c):  #*args, **kwargs
#     print (a, b, c)

# list_ = [1, 2, 3]
# print_params(*list_)


# def print_params (a, b, c):  #*args, **kwargs
#     print (a, b, c)

# list_ = [2, 3]
# print_params(1, *list_)
# print_params(*list_, 4)


# def print_params (a, b, c):  #*args, **kwargs
#     print (a, b, c)

# dict_ = {"a" : 1, "b" : 2, "c" : 3}
# print_params(**dict_)


# def print_params (**kwargs):  #*args, **kwargs
#     print (kwargs)
#     for key, value in kwargs.items():
#         print(key, value)

# dict_ = {"a" : 1, "b" : 2, "c" : 3}
# print_params(**dict_)


def print_params (a, b, c):  #*args, **kwargs
    print (a, b, c)

dict_ = {"c" : 1}
list_ = [2, 3]
print_params(*list_, **dict_)




