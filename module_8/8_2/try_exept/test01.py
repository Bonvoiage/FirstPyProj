def f1(num):
    return 10 / num

def f2():
    print("Function f2")
    summ = 0
    for i in range(-2, 2):
        summ += f1(i)
    return summ

try:
    total = f2()
except ZeroDivisionError as exc:
    print(f"Division by zero - {exc} ")
else:
    print("Total = ", total)