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
    def __init__(self, amount_of_buildings):
        number_of_building = Building.total
        Building.name = f"obj{number_of_building+1}"
        Building.total += 1


buildings_need = 40
print(
f"""
Всего создано зданий {Building.total}
Всего нужно создать зданий {buildings_need}

Создаются здания:
""")
def proverka():
    for i in range(buildings_need):
        print(Building(i).name)
print(
    """
    Проверка
    """)
proverka()

print(
"""
Всего создано зданий""")
print(Building.total)

