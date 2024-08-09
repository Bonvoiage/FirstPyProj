for i in range(int(input("введите число раз, сколько цикл должен повториться "))):
    print("столько раз")
list_ = ["One", "Two", "Three"]
for i in list_:
    if i == "Three":
        list_.remove(i)
print(list_)

list_2 = ["One", "Two", "Three"]
for i in range(len(list_)):
    list_[i] = " "  # можем начать работать со списком
    print(list_[i])

list_3 = [2, 3, 4, 5, 6, 12, 1]
sum_ = 0
for i in range(len(list_3)):
    sum_ += list_3[i]
print(sum_)

for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i} * {j} = {i * j}") 


dict_ = {"a" : 1, "b" : 2, "c" : 3}
# for i in dict_:
#     print(i, dict_[i])
for i, k in dict_.items():  # items - ключ, значение, так что i берет на себя ключ, k - значение
    print(i, dict_[i])