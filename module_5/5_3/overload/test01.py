
class people:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_info(self):
        print(f'Name: {self.name}, age: {self.age}')

    def birthday(self):
        self.age += 1
        print(f"Happy {self.age} birthday {self.name}!")

    def __len__(self):
        return self.age
    
    def __lt__(self, other):
        return self.age < other.age
    
    def __gt__(self, other):
        return self.age > other.age
    def __eq__(self, other):
        return self.age == other.age

    # def __del__(self):
    #     print('Goodbye', self.name)

    def __str__(self):
        return f"Name: {self.name}, age: {self.age}"


den = people("DeveA", 21)
max = people("Uran", 21)
# print ("Den = Max", max == den)
# print ("den < max", den < max)
# max.birthday()
# print ("den < max", den < max)
# print ("den > max", den > max)
# print ("max > den", max > den)
# print ("max == den", max == den)

# # input("Press Enter to exit")
# print(f"Max age: {len(max)}" )

print(den)