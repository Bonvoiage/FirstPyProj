import io
from pprint import pprint


name = '../FirstPyProj/module_7/7_3/operator_with/sample2.txt'
with open(name, encoding="utf-8") as file:
    for line in file:
        print(line, end="")
        # for char in line:
            # print(char, end="")
            # print(char)
    print(file.tell())

# print(file.read())






# print(f"Write mode: {file.writable()}")
# print(f"Read mode: {file.readable()}")
# print(f"seek mode: {file.seekable()}")

# print(file.tell())


# pprint(file.read())



# file.close()