#1

# lam_func = lambda x: x + 10
# print(lam_func(5))
# print(type(lam_func))

# my_nums = [3, 1, 4, 1, 5, 9, 2, 6]
# result = map(lam_func, my_nums)
# print(list(result))

#2

# my_nums = [3, 1, 4, 1, 5, 9, 2, 6]
# th_nums = [2, 7, 1, 8, 2, 8, 1, 8]

# result = map(lambda x, y: x + y, my_nums, th_nums)
# print(list(result))

#3

# def get_multiplier_v1(x):
#     if x == 2:
#         def multiplier(y):
#             return y * 2
#     elif x == 3:   
#         def multiplier(y):
#             return y * 3
#     else:
#         raise Exception("Умножение только на 2 или 3")

#     return multiplier

# my_nums = [3, 1, 4, 1, 5, 9, 2, 6]

# by_2 = get_multiplier_v1(2)
# by_3 = get_multiplier_v1(3)

# result = map(by_2, my_nums)
# print(list(result))

# result = map(by_3, my_nums)
# print(list(result))



#4 

# def get_multiplier_v2(x):
    
#     def multiplier(y):
#         return y * x
#     return multiplier

# by_5 = get_multiplier_v2(5)
# by_10 = get_multiplier_v2(10)
# by_100 = get_multiplier_v2(100)

# my_nums = [3, 1, 4, 1, 5, 9, 2, 6]

# print(list(map(by_5, my_nums)))
# print(list(map(by_10, my_nums)))
# print(list(map(by_100, my_nums)))

# result = map(by_5, my_nums)
# print(list(result))

# result = map(by_10, my_nums)
# print(list(result))

# result = map(by_100, my_nums)
# print(list(result))


#6 

from pprint import pprint

def matrix(some_list):

    def multiply_cols(x):
        res = []
        for elem in some_list:
            res.append(elem * x)
        return res
    return multiply_cols

my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
their_numbers = [2, 7, 1, 8, 2, 8, 1, 8]

matrix_on_my_numbers = matrix(my_numbers)

# result = map(matrix_on_my_numbers, their_numbers)
# print(list(result))

my_numbers.extend([10, 20, 30])
# their_numbers.extend([30, 20, 10])

matrix_on_my_numbers = matrix(my_numbers)

result = map(matrix_on_my_numbers, their_numbers)
pprint(list(result))