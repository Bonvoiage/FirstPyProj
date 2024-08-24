class people:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.say_info()

    def say_info(self):
        print(f'Name: {self.name}, age: {self.age}')


    def birthday(self):
        self.age += 1
        print(f"Happy {self.age} birthday {self.name}!")


den = people("DeveA", 21)
# den.surname = "A"
# den.say_info()
max = people("Uran", 41)

max.birthday()