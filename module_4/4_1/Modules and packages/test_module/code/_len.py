'''
len()
Эта функция используется для вычисления длины последовательности или итерируемого объекта.
'''

#* Пример № 1
# x = (2, 3, 1, 6, 7)

# print(len(x))

# Вывод -> 5

#* Пример № 2
# print(len('Строка'))

# Вывод -> 6

#* Пример № 3
text = 'Один важный секрет: нужно идти туда, куда хочется, а не туда, куда якобы надо.'

# print(len(text))

for i in range(len(text)):
    print(text[i], end =',')
    print(text[i], end = '')
