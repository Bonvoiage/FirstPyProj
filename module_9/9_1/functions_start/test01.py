# def get_russian_names():
#     print("Вася, Петя, Коля")

# 1

# get_russian_names()


# print(type(get_russian_names))
# print(get_russian_names.__name__)

#2

# print(get_russian_names.__name__)

# my_func = get_russian_names
# print(my_func())
# print(my_func.__name__)


#3

# def get_russian_names():
#     return ["Вася", "Петя", "Коля"]


# def get_british_names():
#     return ["John", "Tom", "Harry"]

# name_getters = [get_russian_names, get_british_names]
# print(name_getters)

# for name_getter in name_getters:
#     print(name_getter())


#4 

# def adder(args):
#     res = 0
#     for number in args:
#         res += number
#     return res


# def multiplyer(args):
#     res = 1
#     for number in args:
#         res *= number
#     return res


# def process_numbers(numbers, function):
#     result = function(numbers)
#     print(f"Результат: {result}")

# my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]

# process_numbers(my_numbers, adder)
# process_numbers(numbers=my_numbers, function=multiplyer)


#5 

# def mul_by_2(x):
#     return x * 2

# my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]

# result = map(mul_by_2, my_numbers)
# print(result)
# print(list(result))


#6
def is_odd(x):
    return x % 2

my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]

result = filter(is_odd, my_numbers)
print(result)
print(list(result))