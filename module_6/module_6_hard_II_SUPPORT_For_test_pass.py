import math

class Figure:
    sides_count = 0
    
    def __init__(self, color, *sides):
        self.__color = self.__validate_color(*color)
        if len(sides) != self.sides_count:
            self.__sides = [1] * self.sides_count
        else:
            self.__sides = list(sides)
        self.filled = True
    
    def __validate_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            return [r, g, b]
        return [0, 0, 0]
    
    def __is_valid_color(self, r, g, b):
        return all(isinstance(i, int) and 0 <= i <= 255 for i in (r, g, b))
    
    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]
    
    def get_color(self):
        return self.__color
    
    def __is_valid_sides(self, *sides):
        return all(isinstance(side, int) and side > 0 for side in sides) and len(sides) == self.sides_count
    
    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)
    
    def get_sides(self):
        return self.__sides
    
    def __len__(self):
        return sum(self.__sides)

class Circle(Figure):
    sides_count = 1
    
    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__update_radius()  # Вызываем метод для пересчета радиуса
    
    def __update_radius(self):
        self.__radius = self.get_sides()[0]  # Обновляем радиус
        
    def set_sides(self, *new_sides):
        super().set_sides(*new_sides)
        self.__update_radius()  # Пересчитываем радиус после изменения стороны
    
    def get_square(self):
        return math.pi * (self.__radius ** 2)

class Triangle(Figure):
    sides_count = 3
    
    def get_square(self):
        s = sum(self.get_sides()) / 2
        a, b, c = self.get_sides()
        return math.sqrt(s * (s - a) * (s - b) * (s - c))


class Cube(Figure):
    sides_count = 12
    
    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        if len(sides) != 1:
            self.set_sides(*([1] * 12))
        else:
            self.set_sides(*([sides[0]] * 12))
    
    def get_volume(self):
        return self.get_sides()[0] ** 3




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