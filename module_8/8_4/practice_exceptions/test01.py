import os

print(os.getcwd())
os.chdir("module_8/8_4/practice_exceptions")
print(os.getcwd())

line_number_counter = 1
def calc(line):
    opend_1, operator, opend_2 = line.split(" ")
    opend_1 = int(opend_1)
    opend_2 = int(opend_2)
    if operator == "+":
        result = opend_1 + opend_2
        print(f"{line_number_counter} Результат: {result}")
    elif operator == "-":
        result = opend_1 - opend_2
        print(f"{line_number_counter} Результат: {result}")
    elif operator == "/":
        result = opend_1 / opend_2
        print(f"{line_number_counter} Результат: {result}")
    elif operator == "*":
        result = opend_1 * opend_2
        print(f"{line_number_counter} Результат: {result}")
    elif operator == "//":
        result = opend_1 // opend_2
        print(f"{line_number_counter} Результат: {result}")
    elif operator == "%":
        result = opend_1 % opend_2
        print(f"{line_number_counter} Результат: {result}")
    else:
        raise ValueError("Unknown operation")
    # print(opend_1, opend_2, operator)

with open("calc.txt", "r") as file:
    for line in file:
        try:
            calc(line)
            line_number_counter += 1
        except ValueError as exc:
            if "unpack" in exc.args[0]:
                print(f"В строке {line_number_counter} не хватает данных")
            elif "literal" in exc.args[0]:
                print(f"В строке {line_number_counter} нет операнда")
            # print(f"В строке {line_number_counter} произошла ошибка - {exc}, с параметрами {exc.args}")
            line_number_counter += 1