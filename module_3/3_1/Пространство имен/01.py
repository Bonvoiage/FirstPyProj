a = 5
b = 10


def printer():
    global a, b         #если дописать - то перезаписываю глобальную переменную
    c = 15
    d = 20
    print(
        c, d, "local",f"\n",
        a, b, "global"
        )


printer()
print(a, b)