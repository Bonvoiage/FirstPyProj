
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

    def __len__(self):
        return self.age

    def __del__(self):
        print('Goodbye', self.name)


den = people("DeveA", 21)
max = people("Uran", 41)
del den
max.birthday()
# input("Press Enter to exit")
print(f"Max age: {len(max)}" )