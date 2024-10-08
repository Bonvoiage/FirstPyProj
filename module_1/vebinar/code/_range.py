'''
range()
Используется для создания последовательности чисел с заданными значениями от и до, а также интервалом. Такая последовательность часто используется в циклах, особенно в цикле for.
'''
# range(start, stop, step)

#* Пример № 1
# print(list(range(0, 20, 2)))
# print(tuple(range(20)))


# Вывод -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

#* Пример № 2
# for i in range(10):
#     print(i, end = ', ')

# Вывод -> 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

#* Пример № 3
# print(range(10, 20, 2))

# Вывод -> range(10, 20, 2)

#* Пример № 4
# print(list(range(10, 20, 2)))

# Вывод -> [10, 12, 14, 16, 18]

#* Пример № 5
print(list(range(20, 10, -2)))

# Вывод -> [20, 18, 16, 14, 12]