class Figure:

    filled = False
    sides_count = 0

    def __init__(self, color, *sides: int):
        self.r = color[0]
        self.g = color[1]
        self.b = color[2]
        self.__color = []
        self.set_color(self.r, self.g, self.b)
        self.__sides = []
        self.set_sides(*sides)

    # Проверка валидности цвета
    def __is_valid_color(self, new_color):
        if 0 <= new_color <= 255:
            return True
        else:
            print("Недопустимое значение цвета")
            return False

    # Устанавливаем цвет после проверки
    def set_color(self, r, g, b):
        if self.__is_valid_color(r) and self.__is_valid_color(g) and self.__is_valid_color(b):
            self.__color = [r, g, b]
    
    # Получаем цвет
    def get_color(self):
        return self.__color

    # Проверка на валидность сторон
    def __is_valid_sides(self, new_sides):
        if len(new_sides) == 1 or len(new_sides) == self.sides_count:
            return True
        else:
            print("Недопустимое количество сторон")
            return False

    # Устанавливаем стороны после проверки
    def set_sides(self, *new_sides):
        if self.__is_valid_sides(new_sides):
            if len(new_sides) == 1:
                self.__sides = [new_sides[0]] * self.sides_count
            else:
                self.__sides = list(new_sides)
        else:
            self.__sides = [1] * self.sides_count

    # Получаем стороны
    def get_sides(self):
        return self.__sides
    
    # Периметр (сложение всех сторон)
    def __len__(self):
        return sum(self.__sides)


class Circle(Figure):

    sides_count = 1

    def __init__(self, color, radius: int):
        super().__init__(color, radius)
    
    # Площадь круга
    def get_square(self):
        radius = self.get_sides()[0]
        return 3.14 * (radius ** 2)


class Triangle(Figure):

    sides_count = 3

    def __init__(self, color, *sides: int):
        super().__init__(color, *sides)

    # Площадь по формуле Герона
    def get_square(self):
        from math import sqrt
        sides = self.get_sides()
        p = sum(sides) / 2
        return sqrt(p * (p - sides[0]) * (p - sides[1]) * (p - sides[2]))


class Cube(Figure):

    sides_count = 12

    def __init__(self, color_input: tuple, side_length: int):
        super().__init__(color_input, side_length)
    
    # Объем куба
    def get_volume(self):
        side = self.get_sides()[0]
        return side ** 3

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