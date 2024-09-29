import io
from pprint import pprint


name = '../FirstPyProj/module_7/7_2/read_work_with_files/sample2.txt'
file = open(name, "r", encoding="utf-8") # r, w, a | Read, Write, Append
print(f"Write mode: {file.writable()}")
print(f"Read mode: {file.readable()}")
print(f"seek mode: {file.seekable()}")
print(file.buffer)
pprint(file.encoding)
print(file.tell())
pprint(file.read())
print(file.tell())
# print(file.seek(139))
# pprint(file.read())
# file.write("Hello, World!")
# print(file.tell())

file.close()