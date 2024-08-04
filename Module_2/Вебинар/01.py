operator = 2

match operator:
    case 1:
        print("1")
    case 2:
        print("2asdasd")



l = [3, 4, 5, 6, 7, 8, "smth"] 
i = 0
while i <len(l):
    if l[i] == 6:         # скипнули значение 6
        i += 1
        continue
    print(l[i])
    i += 1


for j in "hello":    # j принимает str значение, каждого элемента в str
    print(j)

