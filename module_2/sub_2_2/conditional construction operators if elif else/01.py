# name = input("Введите имя: ")
#
# if name == "admin":
#     print("admin")
# elif name != "admin":
#     print("Hey, ", name)

number_input = int(input("Ввудите число: "))
if number_input % 3 == 0 and number_input % 5 == 0:
    print("FizzBuzz")
elif number_input % 3 == 0:
    print("Fizz")
elif number_input % 5 == 0:
    print("Buzz")
else:
    print("Ne to"2)
