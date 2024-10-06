

# try:
#     test = 0
#     print (10 / test)

# except ZeroDivisionError:
#     print("На ноль делить нельзя!")


try:
    optional = a + b
    optional = 10 / 0
except ZeroDivisionError:
    print("На ноль делить нельзя!")
except NameError as err:
    print(f"Переменная не определена! {err} тут проблема ")
except:
    print("Неизвестная ошибка!")