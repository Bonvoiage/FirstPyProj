import io
from pprint import pprint




name = '../FirstPyProj/module_7/7_2/sample.txt'
file = open(name, "r") # r, w, a | Read, Write, Append

print(file.tell())
pprint(file.read())
print(file.tell())
pprint(file.read())

file.close()
