def f1(num):
    testdivzero = 0
    try:
        testdivzero = 10 / num
    except ZeroDivisionError:
        print("ZeroDivisionError")
    return testdivzero

def f2():
    print("Function f2")
    summ = 0
    for i in range(-2, 3):
        try:
            summ += f1(i)
            print(summ)
        except ZeroDivisionError:
            print("ZeroDivisionError")
    return summ

try:
    total = f2()
except ZeroDivisionError as exc:
    print(f"Division by zero - {exc} ")
else:
    print("Total = ", total)