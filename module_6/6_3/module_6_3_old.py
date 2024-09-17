# Создайте новый проект или продолжите работу в текущем проекте
# Ваша задача:
# Создайте родительский(базовый) класс Vehicle, который имеет свойство vehicle_type = "none"
# Создайте родительский(базовый) класс Car, который имеет свойство price = 1000000 и функцию def horse_powers, которая возвращает количество лошидиных сил для автомобиля
# Создайте наследника класса Car и Vehicle - класс Nissan и переопределите свойство price и vehicle_type, а также переопределите функцию horse_powers
# Создайте экзмепляр класса Nissan и распечайте через функцию print vehicle_type, price
# Получившийся код прикрепите к заданию текстом



class Vehicle:
    vehicle_type = "none"

    def __init__(self, price):
        self.price = price

    def horse_powers(self):
        return "100 лошадиных сил"
    
class Car:
    def __init__(self, price = 1000000):
        super().__init__(price)

    
    def horse_powers(self):
        return super().horse_powers()
    
class Nissan(Car, Vehicle):

    def __init__(self, price, vehicle_type):
        self.vehicle_type = vehicle_type
        self.price = price

    def horse_powers(self):
        return super().horse_powers()

nissan = Nissan(200000, "Nissan")
print(nissan.vehicle_type, nissan.price)