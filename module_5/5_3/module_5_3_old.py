#Домашняя работа по уроку "Перегрузка операторов."
# Создайте новый проект в PyCharm
# Запустите созданный проект
# Ваша задача:
# Создайте новый класс Building
# Создайте инициализатор для класса Building, который будет задавать целочисленный атрибут этажности self.numberOfFloors и строковый атрибут self.buildingType
# Создайте(перегрузите) __eq__, используйте атрибут numberOfFloors и buildingType для сравнения
# Полученный код напишите в ответ к домашнему заданию


class Building():
    def __init__(self, numberOfFloors, buildingType):
        self.numberOfFloors = numberOfFloors
        self.buildingType = buildingType

    def __eq__(self, other):
        return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType
    

b1 = Building(10, "ЖК Эльбрус")
b2 = Building(10, "ЖК Эльбрус")
print(b1 == b2)

b13 = Building(109, "ЖК Эльбрус")
b23 = Building(10, "ЖК Эльбрус")
print(b13 == b23)
####