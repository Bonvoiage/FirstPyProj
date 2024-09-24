# #Дополнительное практическое задание по модулю*


class Figure:
    
    
    filled = False
    sides_count = 0

    def __init__(self, color, *sides : int):
        self.r = color[0]
        self.g = color[1]
        self.b = color[2]
        self.set_color(self.r, self.g, self.b)
        self.set_sides(*sides)
        self.__side = 0
        self.__color = []

    # проверка на валидность цвета
    def __is_valid_color(self, new_color):
        if new_color < 0 or new_color > 255:
            # raise ValueError("Недопустимое значение цвета")
            print("Недопустимое значение цвета")
            return False
        if new_color >= 0 or new_color <= 255:
            return True

    # устанавливаем цвет после проверки
    def set_color(self, r, g, b):
        r_check = self.__is_valid_color(r)
        g_check = self.__is_valid_color(g)
        b_check = self.__is_valid_color(b)
        if r_check and g_check and b_check:
            self.__color = [r, g, b]
    
    # получаем цвет
    def get_color(self):
        return self.__color

    # проверка на валидность сторон
    def __is_valid_sides(self, new_sides):
        # checker = False
        # if len(new_sides) != 0:
        #     for i in range(len(*new_sides)):
        #         new_sides_i_number = new_sides[i]
        #         if new_sides_i_number < 0:
        #             checker = False
        #         else:
        #             checker = True
        if len(new_sides) == 1:
            return True
        elif len(new_sides) != self.sides_count:
            print("Недопустимое количество сторон")
            return False
        # elif checker == False:
        #     print("Недопустимое значение стороны")
        #     return False
        else:
            return True
        
    def recurce_start(self, new_sides):
        rec_new_sides = []
        if isinstance(new_sides, list, tuple):
            for i in new_sides:
                self.recurce_start(i)
        elif isinstance(new_sides, int):
            rec_new_sides.append(new_sides)
        return rec_new_sides

    # устанавливаем стороны после проверки
    def set_sides(self, *new_sides):
        sides_check = self.__is_valid_sides(new_sides)
        new_sides = self.recurce_start(new_sides)
        sides_check = self.recurce_start(sides_check)
        if sides_check == True and len(new_sides) != 1:
            self.__sides = new_sides
        elif sides_check and len(new_sides) == 1:
            self.__sides = []
            new_sides = new_sides[0]
            for i in range (0, self.sides_count):
                self.__sides.append(new_sides)
        elif not sides_check and self.__sides != None:
            pass
        elif not sides_check:
            self.__sides = []
            for i in range (0, self.sides_count):
                self.__sides.append(1)

    # получаем стороны
    def get_sides(self):
        return self.__sides
    
    # перметр (сложение всех сторон)
    def __len__(self):
        temp_len = 0
        for i in self.__sides:
            temp_len += i
        return temp_len


class Circle(Figure):

    sides_count= 1
    __radius = 0

class Circle(Figure):

    sides_count = 1  # У круга одна сторона - радиус
    __radius = 0

    def __init__(self, color, *sides : int):
        super().__init__(color, sides)
        self.__radius = sides  # Сохраняем радиус

    # Площадь круга
    def get_square(self):
        check_radius_change = self.get_sides()
        return 3.14 * (check_radius_change[0] ** 2)
    
class Triangle(Figure):

    sides_count= 3

    def __init__(self, color, *sides : int):
        super().__init__(color, *sides)
        self.__side = self.get_sides()

    # Площадь по формуле Герона
    def get_square(self):
        from math import sqrt
        self.__side = self.get_sides()
        p = 0.5 * (self.__side[0] + self.__side[1] + self.__side[2])
        S = sqrt(p * (p - self.__side[0]) * (p - self.__side[1]) * (p - self.__side[2]))
        return S


class Cube(Figure):

    sides_count= 12

    def __init__(self, color_input: tuple, *sides):
        super().__init__(color_input, *sides)
        self.__side = self.get_sides()

    # Площадь куба
    def get_volume(self):
        self.__side = self.get_sides()
        return self.__side[0] ** 3









circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)
triangle1 = Triangle((200, 200, 200), 3, 6, 8)


# Проверка на изменение цветов:
# print(circle1.get_color())
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# # Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# # Проверка периметра (круга), это и есть длина:
print(len(circle1))

# # Проверка объёма (куба):
print(cube1.get_volume())

print(f"""


Площадь куба: {cube1.get_volume()}
Площадь круга: {circle1.get_square()}
Площадь треугольника: {triangle1.get_square()}




""")












# Дополнительное практическое задание по модулю: "Наследование классов."

# Цель: Применить знания полученные в модуле, решив задачу повышенного уровня сложности

# Задание "Они все так похожи":
# 2D? 3D? Даже 4D?.... Настолько глубоко мы заходить конечно же не будем, 4D подождёт, но вот с двумерными и трёхмерными фигурами можем поэкспериментировать.
# Вы когда-нибудь задумывались как устроены графические библиотеки для языков программирования?
# Безусловно, там выполняются огромные расчёты при помощи вашей видеокарты, но... Что лежит в основе удобного использования таких объектов?

# По названию задачи можно понять, что все геометрические фигуры обладают схожими свойствами, такими как: длины сторон, цвет и др.

# Давайте попробуем реализовать простейшие классы для некоторых таких фигур и при этом применить наследование (в будущем, изучая сторонние библиотеки, вы будете замечать схожие классы, уже написанные кем-то ранее):

# Общее ТЗ:
# Реализовать классы Figure(родительский), Circle, Triangle и Cube, объекты которых будут обладать методами изменения размеров, цвета и т.д.
# Многие атрибуты и методы должны быть инкапсулированны и для них должны быть написаны интерфейсы взаимодействия (методы) - геттеры и сеттеры.

# Подробное ТЗ:

# Атрибуты класса Figure: sides_count = 0
# Каждый объект класса Figure должен обладать следующими атрибутами:
# Атрибуты(инкапсулированные): __sides(список сторон (целые числа)), __color(список цветов в формате RGB)
# Атрибуты(публичные): filled(закрашенный, bool)
# И методами:
# Метод get_color, возвращает список RGB цветов.
# Метод __is_valid_color - служебный, принимает параметры r, g, b, который проверяет корректность переданных значений перед установкой нового цвета. Корректным цвет: все значения r, g и b - целые числа в диапазоне от 0 до 255 (включительно).
# Метод set_color принимает параметры r, g, b - числа и изменяет атрибут __color на соответствующие значения, предварительно проверив их на корректность. Если введены некорректные данные, то цвет остаётся прежним.
# Метод __is_valid_sides - служебный, принимает неограниченное кол-во сторон, возвращает True если все стороны целые положительные числа и кол-во новых сторон совпадает с текущим, False - во всех остальных случаях.
# Метод get_sides должен возвращать значение я атрибута __sides.
# Метод __len__ должен возвращать периметр фигуры.
# Метод set_sides(self, *new_sides) должен принимать новые стороны, если их количество не равно sides_count, то не изменять, в противном случае - менять.

# Атрибуты класса Circle: sides_count = 1
# Каждый объект класса Circle должен обладать следующими атрибутами и методами:
# Все атрибуты и методы класса Figure
# Атрибут __radius, рассчитать исходя из длины окружности (одной единственной стороны).
# Метод get_square возвращает площадь круга (можно рассчитать как через длину, так и через радиус).

# Атрибуты класса Triangle: sides_count = 3
# Каждый объект класса Triangle должен обладать следующими атрибутами и методами:
# Все атрибуты и методы класса Figure
# Метод get_square возвращает площадь треугольника. (можно рассчитать по формуле Герона)
# Атрибуты класса Cube: sides_count = 12
# Каждый объект класса Cube должен обладать следующими атрибутами и методами:
# Все атрибуты и методы класса Figure.
# Переопределить __sides сделав список из 12 одинаковы сторон (передаётся 1 сторона)
# Метод get_volume, возвращает объём куба.

# ВАЖНО!
# При создании объектов делайте проверку на количество переданных сторон, если сторон не ровно sides_count, то создать массив с единичными сторонами и в том кол-ве, которое требует фигура.
# Пример 1: Circle((200, 200, 100), 10, 15, 6), т.к. сторона у круга всего 1, то его стороны будут - [1]
# Пример 2: Triangle((200, 200, 100), 10, 6), т.к. сторон у треугольника 3, то его стороны будут - [1, 1, 1]
# Пример 3: Cube((200, 200, 100), 9), т.к. сторон(рёбер) у куба - 12, то его стороны будут - [9, 9, 9, ....., 9] (12)
# Пример 4: Cube((200, 200, 100), 9, 12), т.к. сторон(рёбер) у куба - 12, то его стороны будут - [1, 1, 1, ....., 1]

# Код для проверки:
# circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
# cube1 = Cube((222, 35, 130), 6)

# # Проверка на изменение цветов:
# circle1.set_color(55, 66, 77) # Изменится
# print(circle1.get_color())
# cube1.set_color(300, 70, 15) # Не изменится
# print(cube1.get_color())

# # Проверка на изменение сторон:
# cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
# print(cube1.get_sides())
# circle1.set_sides(15) # Изменится
# print(circle1.get_sides())

# # Проверка периметра (круга), это и есть длина:
# print(len(circle1))

# # Проверка объёма (куба):
# print(cube1.get_volume())


# Выходные данные (консоль):
# [55, 66, 77]
# [222, 35, 130]
# [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]
# [15]
# 15
# 216

# Примечания (рекомендации):
# Рекомендуется сделать дополнительные (свои проверки) работы методов объектов каждого класса.
# Делайте каждый класс и метод последовательно и проверяйте работу каждой части отдельно.
# Для проверки принадлежности к типу рекомендуется использовать функцию isinstance.
# Помните, служебные инкапсулированные методы можно и нужно использовать только внутри текущего класса.
# Вам не запрещается вводить дополнительные атрибуты и методы, творите, но не переборщите!

# Файл с кодом (module6hard.py) прикрепите к домашнему заданию или пришлите ссылку на ваш GitHub репозиторий с файлом решения.

# Успехов!
