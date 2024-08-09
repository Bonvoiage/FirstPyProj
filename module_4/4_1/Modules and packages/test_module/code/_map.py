'''
map()
Python map() — это встроенная функция, которая позволяет обрабатывать и преобразовывать все элементы в итерируемом объекте без использования явного цикла for, методом, широко известным как сопоставление (mapping). map() полезен, когда вам нужно применить функцию преобразования к каждому элементу в коллекции или в массиве и преобразовать их в новый массив.
Согласно документации, map() принимает функцию и итерацию (или несколько итераций) в качестве аргументов и возвращает итератор, который выдает преобразованные элементы по запросу. Сигнатура функции map определяется следующим образом:

map(function, iterable[, iterable1, iterable2,..., iterableN])
'''

'''
Чтобы лучше понять map(), предположим, что вам нужно взять список числовых значений и преобразовать его в список, содержащий квадратное значение каждого числа в исходном списке. В этом случае вы можете использовать цикл for и написать что-то вроде этого:
'''

#* Пример № 1
# numbers = [1, 2, 3, 4, 5]
# squared = []

# for num in numbers:
#     squared.append(num ** 2)

# print(squared)

# Вывод -> [1, 4, 9, 16, 25]

# Вы можете добиться того же результата без использования явного цикла for, используя map(). 
# def square(number):
#     return number ** 2

# numbers = [1, 2, 3, 4, 5]
# squared = map(square, numbers)

# print(list(squared))

# Вывод -> [1, 4, 9, 16, 25]

'''
В качестве другого примера предположим, что вам нужно преобразовать все элементы в списке из строки в целое число. 
'''
#* Пример № 2
str_nums = ['4', '8', '6', '5', '3', '2', '8', '9', '2', '5']

int_nums = map(int, str_nums)
print(int_nums)

# # # Вывод -> <map object at 0x7fb2c7e34c70>

print(list(int_nums))

# Вывод -> [4, 8, 6, 5, 3, 2, 8, 9, 2, 5]

print(str_nums)

# Вывод -> ['4', '8', '6', '5', '3', '2', '8', '9', '2', '5']