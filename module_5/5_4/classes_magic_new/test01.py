# print(int.__mro__)


class User:

    __instance = None

    def __new__(cls, *args, **kwargs):
        print("new")
        if cls.__instance == None:
            cls.__instance = super().__new__(cls)
        return cls.__instance   

    def __init__(self, *args, **kwargs):
        print("init")
        self.args = args
        self.kwargs = kwargs
        for key, value in kwargs.items():
            setattr(self, key, value)

other = [1, 2, 3, 4, 5]
user = {"name": "John", "age": 36}



user1 = User(*other, **user)

print(user1.args) 
print(user1.kwargs)
print(user1.name) 
print(user1.age)
# user2 = User(user)

# print(User.__mro__) 
# print(id(user1), id(user2))
# print(user1 is user2)