# concatenation of strings
print("hello" + " " + "world")

print("Hello, " + "World!")
# print("Hello, %s что то там %s" % "World!", 14) #не работает
print("Hello, %s что то там %s" % ("World!", 14)) 
print("Привет, мое имя %(name)s и возраст %(year)s" % {"name":"Ден", "year" : 14}) #переводит в шестнадцатеричную систему
print("Hello, %s что то там %x" % ("World!", 14)) #переводит в шестнадцатеричную систему

print("Я учусь в {} {}".format("университете", "Urban"))
print("Я учусь в {0} {1} {0}".format("университете", "Urban"))
print("Я учусь в {postfix} {tittle} {tittle}".format(postfix = "университете", tittle = "Urban"))

print(f"{'Hello, World!' *2} Hello, World!")


# multiplication of strings
# print("hello" * 3)