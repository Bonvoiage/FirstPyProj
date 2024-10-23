# Домашнее задание по уроку Генерация функций.

def create_operation(operation):
    if operation == "add":
        def add(x, y):
            return x + y
        return add
    elif operation == "subtract":
        def subtract(x, y):
            return x - y
        return subtract
    elif operation == "multiply":
        def multiply(x, y):
            return x * y
        return multiply
    elif operation == "divide":
        def divide(x, y):
            # if y == 0:
            #     return "Error: Division by zero"
            # return x / y
            try:
                return x / y
            except ZeroDivisionError:
                return "Error: Division by zero"
        return divide

# Пример использования фабрики функций:
add_func = create_operation("add")
print(add_func(3, 3))  # 6

div_func = create_operation("divide")
print(div_func(10, 5))  # 2.0

div_by_zero = div_func(10, 0)  # Error: Division by zero
print(div_by_zero)


# Лямбда-функция
square_lambda = lambda x: x ** 2
print(square_lambda(4))  # 16

# Эквивалентная функция с использованием def
def square_def(x):
    return x ** 2

print(square_def(4))  # 16


class Rect:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __call__(self):
        return self.a * self.b

# Пример использования вызываемого объекта:
s_rect = Rect(2, 4)
print(f"Стороны: {s_rect.a}, {s_rect.b}")
print(f"Площадь: {s_rect()}")  # 8



# Цель задания:
# Научиться создавать функции динамически в зависимости от заданных условий и параметров, используя различные подходы, такие как фабрики функций, лямбда-функции и вызываемые объекты.
# Теоретический комментарий:
# 1. Динамическое определение функций (def):
# В Python можно определять функции внутри других функций. Такие функции могут создаваться и возвращаться. Это основа для создания "фабрик функций" - функций, создающих функции.
# 2. Лямбда-функции:
# Лямбда-функции в Python — это анонимные функции, определённые одной строкой. Они удобны для создания простых функций на лету, особенно когда функция нужна временно или для одноразового использования.
# 3. Вызываемые объекты (__call__):
# В Python у класса может быть метод __call__, что позволяет его экземплярам вести себя как функции. Это дает возможность создавать объекты, которые могут быть вызваны как функции и хранить состояние между вызовами.
# Задание:
# Задача 1: Фабрика Функций
# Написать функцию, которая возвращает различные математические функции (например, деление, умножение) в зависимости от переданных аргументов.
# Задача 2: Лямбда-Функции
# Использовать лямбда-функцию для реализации простой операции и написать такую же функцию с использованием def. Например, возведение числа в квадрат
# Задача 3: Вызываемые Объекты
# Создать класс с Rect c полями a, b которые задаются в __init__ и методом __call__, который возвращает площадь прямоугольника, то есть a*b.
# Комментарии к заданию:
# Фабрика функций для сложения и вычитания:
# def create_operation(operation):
#     if operation == "add":
#         def add(x, y):
#             return x + y
#         return add # возвращаем функцию как объект!! Тут скобки не нужны
#     elif operation == "subtract":
#         def subtract(x, y):
#             return x - y
#         return subtract
# my_func_add = create_operation("add")
# print(my_func_add(1,2))
# Пример лямбда функции с аналогом через def
# multiply = lambda x, y: x * y
# print(multiply(2, 3)) # Выводит 6
# def multiply_def(x, y):
#    return x * y
# print(multiply_def(2, 3)) # Выводит 6
# Пример создания вызываемого объекта
# class Repeater:
#    def __init__(self, value):
#        self.value = value
#    def __call__(self, n):
#        return [self.value] * n
# repeat_five = Repeater(5)
# print(repeat_five(3)) # Выводит [5, 5, 5]
# Пример вывода программы
# Задача 1: Фабрика функций
# 6
# 2.0
# Error: Division by zero
# Задача 2 лямбда
# 16
# 16
# Задача 3: Вызываемые объекты
# Стороны: 2, 4
# Площадь: 8

