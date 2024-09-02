# #Домашнее задание по уроку "Различие атрибутов класса и экземпляра"
# Создайте новый проект в PyCharm
# Запустите созданный проект
# Ваша задача:
# Создайте новый класс Buiding с атрибутом total
# Создайте инициализатор для класса Buiding, который будет увеличивать атрибут количества созданных объектов класса Building total
# В цикле создайте 40 объектов класса Building и выведите их на экран командой print
# Полученный код напишите в ответ к домашнему заданию



class Building:
    total = 0
    list_of_buildings = []

    def __new__ (cls, *args, **kwargs):
        return super().__new__(cls)
    def __init__(self, *args, **kwargs):
        args = Building.total
        self.name = f"obj{args+1}"
        Building.list_of_buildings.append(self.name)
        Building.total += 1

###
buildings_need = 40
print(
f"""
Всего создано зданий {Building.total}
Всего нужно создать зданий {buildings_need}

Создаются здания:
""")
for i in range(buildings_need):
    print(Building(i).name)
print(
    """
    Проверка
    """)

print(Building.list_of_buildings)

print(
"""
Всего создано зданий""")
print(Building.total)
print(f"Верно ли то, что кол-во созданых зданий равно колву нужных зданий? {Building.total == buildings_need}")

