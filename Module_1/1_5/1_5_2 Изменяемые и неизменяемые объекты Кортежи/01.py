#лекция

# smth = 1, 2, 3, 4, True, "smthng"
# smth2 = (1, 2, 3, 4)
# smth3 = tuple([1, 2, 3, 4])
# print(smth)
# print(smth2)
# print(smth3)
# print(smth[0])

tuple1= ([1, 2, 3], 4)
print(tuple1)
tuple1[0][2]=12                     #сначала элемент из круглых скобок (первый), затем элемент из квадратных скобок, (третий)
print(tuple1)

tuple2= ([1, 2, 3], 4) + (5, 1, [23, 1, 12])
print(tuple2)
tuple2 = tuple2*2
print(tuple2)