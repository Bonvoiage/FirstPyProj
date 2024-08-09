# лекция

phone_book = {"Denis" : 88005553535, "Max" : 88001000500, "Oleg" : ["Login", "password"]}
print(type(phone_book))

print(phone_book["Denis"])

phone_book["Denis"] = 123123123
print(phone_book["Denis"])

phone_book ["Sid"] = 1231123123
print(phone_book)

print(phone_book)
del phone_book['Max']

phone_book.update({"Sasha": 812381283,
                   "Alex": 1239129319})
print(phone_book)

print(phone_book.get("Alex"))
print(phone_book.get("Max", "Занят он"))

def1 = phone_book.pop("Alex")
print(phone_book)
print(def1)


list1 = [1, 2, 3]
print(list1)
list1.pop(1)
print(list1)
#print(list1(1))    # Ошибка нет такого элемента больше. т.е. если обращение есть, то оно пропускает 2 порядковый номер списка? неудобно.


print(phone_book.keys())
print(phone_book.values())
print(phone_book.items())