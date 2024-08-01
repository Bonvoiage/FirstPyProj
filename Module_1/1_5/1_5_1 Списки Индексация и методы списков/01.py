# лекция

some_food_list = ["Тыблоко", "Груша", "Папайя", "Коконат"]
print(some_food_list)
print(some_food_list[0])

some_food_list[0] = "Яблоко"
print(some_food_list)

some_food_list.append(True)
print(some_food_list)

# some_food_list.extend("string")
# print(some_food_list)

some_food_list.extend(["string", 2])
print(some_food_list)

some_food_list.remove(2)
print(some_food_list)

print("string" in some_food_list)
print("тото" in some_food_list)

print(some_food_list[0::2])