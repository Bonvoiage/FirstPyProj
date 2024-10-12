# def greet_person(person_name):
#     if person_name == "Alex":
#         raise Exception("No Alex here")
#     print(f"Привет, {person_name}!")

# greet_person("Ученик01")
# greet_person("Alex")
# greet_person("Ученик02")

# try:
#     raise NameError("Привет там")
# except NameError as exc:
#     print(f"Исключение типа {type(exc)}. Его параметры: {exc.args}")
#     raise


# class Pro_Zerro(Exception):
#     pass

# def f1(a, b):
#     if b == 0:  
#         raise Pro_Zerro("Деление на ноль")
#     return a / b

# print(f1(10, 0))


class Pro_Zerro(Exception):
    def __init__(self, message, extra):
        self.message = message
        self.extra = extra

def f2(a, b):
    if b == 0:  
        raise Pro_Zerro("Деление на ноль невозможно", {"a": a, "b": b})
    return a / b

try:
    result = f2(10, 0)
except Pro_Zerro as exc:
    print(f"Исключение {exc}")
    print(f"Параметры: {exc.extra}")
    print(f"Сообщение: {exc.message}")
