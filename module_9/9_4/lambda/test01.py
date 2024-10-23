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

def get_multiplier_v1(x):
    if x == 2:
        def multiplier(y):
            return y * 2
    elif x == 3:   
        def multiplier(y):
            return y * 3
    else:
        raise Exception("Умножение только на 2 или 3")

    return multiplier

my_nums = [3, 1, 4, 1, 5, 9, 2, 6]

by_2 = get_multiplier_v1(2)
by_3 = get_multiplier_v1(3)

result = map(by_2, my_nums)
print(list(result))

result = map(by_3, my_nums)
print(list(result))



