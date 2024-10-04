import os

print("текущая директория: ", os.getcwd())  
os.chdir("module_7/7_5/files_in_os")
print("")
print("текущая директория: ", os.getcwd())  
print("")

if os.path.exists("test_folder"):
    os.chdir("test_folder")
else:
    os.mkdir("test_folder")
    os.chdir("test_folder")

print("текущая директория: ", os.getcwd())  

print("")

# os.makedirs("test_folder_1/test_folder_2")
print("текущая директория: ", os.getcwd())
print("")

print(os.listdir())
print("")

for i in os.walk("."):
    print(i)
print("")
os.chdir(r"D:\Users\s.barlamov\repository\FirstPyProj\module_7\7_5")
print("текущая директория: ", os.getcwd())
print("")
os.chdir("../..")
print("текущая директория: ", os.getcwd())
print("")

file = [f for f in os.listdir(".") if os.path.isfile(f)]
print(file)
dirs = [d for d in os.listdir(".") if os.path.isdir(d)]
print(dirs)


print("")
os.chdir(r"D:\Users\s.barlamov\repository\FirstPyProj\module_7\7_5\files_in_os")
print("текущая директория: ", os.getcwd())
print("")

file = [f for f in os.listdir(".") if os.path.isfile(f)]
print(file)
dirs = [d for d in os.listdir(".") if os.path.isdir(d)]
print(dirs)

# os.startfile(file[1])
# os.startfile("text.txt")
print(os.stat("text.txt"))
# print(os.stat("text.txt").st_size)
