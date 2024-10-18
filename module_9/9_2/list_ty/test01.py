
#1

# def by_3(n):
#     return n * 3

# def is_odd(x):
#     return x % 2


# my_nums = [3, 1, 4, 1, 5, 9, 2, 6]

# result = map(by_3, filter(is_odd, my_nums))
# print(list(result))


#test
# collection = [1, 2, 3, 4, 5]
# list_comp_1 = [x*2 for x in collection]

#2

# my_nums = [3, 1, 4, 1, 5, 9, 2, 6]
# result = [x * 3 for x in my_nums]
# print(result)


#3

# my_nums = [3, 1, 4, 1, 5, 9, 2, 6]
# result = [x * 3 for x in my_nums if x % 2]
# print(result)

#4 

# my_nums = ["A", 1, 4, "B", 5, "C", 2, 6]
# result = [x if type(x) == str else x * 5 for x in my_nums]
# # result = [x * 2 if x > 2 else x * 10 for x in my_nums]
# print(result)

#5

# my_nums = [3, 1, 4, 1, 5, 9, 2, 6]
# my_nums2 = [2, 7, 1, 8, 2, 8, 1, 8]
# result = [x*y for x in my_nums for y in my_nums2]
# print(result)

# result = [x*y for x in my_nums for y in my_nums2 if x % y]
# print(result)

# result = [x*y for x in my_nums for y in my_nums2 if x % 2 and y // 2]
# print(result)

#6

my_nums = [3, 1, 4, 1, 5, 9, 2, 6]
my_nums2 = [2, 7, 1, 8, 2, 8, 1, 8]

result = {x for x in my_nums}
print(result)

result = {x: x**2 for x in my_nums}
print(result)