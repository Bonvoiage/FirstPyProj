
class people:

    head = True

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.say_info()

    def say_info(self):
        print(f'Name: {self.name}, age: {self.age}')

    def birthday(self):
        self.age += 1
        print(f"Happy {self.age} birthday {self.name}!")

    def __str__(self):
        return f"Name: {self.name}, age: {self.age}"
    
    def __lt__(self, other):
        if isinstance(other, people):
            return self.age < other.age
        if isinstance(other, int):
            return self.age < other

    def __gt__(self, other):
        if isinstance(other, people):
            return self.age > other.age
        if isinstance(other, int):
            return self.age > other
        

    def __len__(self):
        return self.age

    def __del__(self):
        print('Goodbye', self.name)


den = people("DeveA", 21)
max = people("Uran", 41)
max.birthday()
# input("Press Enter to exit")
print(f"Max age: {len(max)}" )