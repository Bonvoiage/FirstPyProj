set_ = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7.2, "String", True, (11, 2, 4) }
print(set_)
list_ = [1, 1, 1, 2, 2, 3, 4, 5]
list2_ = [1, 1, 1, 2, 2, 3, 4, 5]
list3_ = [1, 1, 1, 2, 2, 3, 4, 5]
print("here")
print(list_)
# print(set(list_))
list_ = set(list_)

print(list_)

print(list_.discard(1))
print(list_)

list2_ = set(list2_)
print(list2_.remove(1))
print(list2_)
print(list2_.add(12))
print(list2_)