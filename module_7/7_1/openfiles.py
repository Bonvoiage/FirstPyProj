from pprint import pprint


# name = '../FirstPyProj/module_7/7_1/sample.txt'
# file = open(name, "r") # r, w, a | Read, Write, Append

# # print(file)
# # pprint(file.read())

# file.close()

# name = '../FirstPyProj/module_7/7_1/sample2.txt'
# file = open(name, "w") # r, w, a | Read, Write, Append
# file.write("Hello, World!\n")

# file.close()

# file = open(name, "a") # r, w, a | Read, Write, Append
# file.write("Hello, World!\n")
# file.close()


name = '../FirstPyProj/module_7/7_1/sample.txt'
file = open(name, "r") # r, w, a | Read, Write, Append

print(file.tell())
pprint(file.read())
print(file.seek(60))
pprint(file.read())

file.close()