# Ваша задача:
# Создайте родительский(базовый) класс Car, который имеет свойство price = 1000000 и метод def horse_powers, которая возвращает количество лошадиных сил для автомобиля
# Создайте наследника класса Car - класс Nissan и переопределите свойство price, а также переопределите метод horse_powers
# Дополнительно создайте класс Kia, который также будет наследником класса Car и переопределите также свойство price, а также переопределите метод horse_powers

class Car:

    price = 1000000

    def horse_powers(self):
        return "100 лошадиных сил"
    
class Nissan(Car):

    price = 2000000

    def horse_powers(self):
        return "200 лошадиных сил"
    
class Kia(Car):

    price = 3000000

    def horse_powers(self):
        return "300 лошадиных сил"
