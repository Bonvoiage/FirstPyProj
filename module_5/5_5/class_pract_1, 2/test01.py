
class Database:
    """
    """
    def __init__(self, *args, **kwargs):
        self.data = {}
    def add_user(self, username, password):
            self.data[username] = password

class User:
    """
    функция регистрации, ввод юзернейма, пароля, проверка пароля введенного пользователем
    """
    def __init__(self, username, password, password_confirm, *args, **kwargs):
        self.username = username    
        if password == password_confirm:
            self.password = password
        else:
            print("password not confirmed")
            exit
class Password_registration:
    """
    проверка пароля
    """        
    def __init__(self, password):
        self.password_checking = password
    """
    функция проверки пароля на длину символов
    """
    def password_len(password_checking):
        if len(password_checking) < 8 or len(password_checking) > 16 :
            print("Пароль не верный, длина должна быть от 8 до 16 символов, так же содержать буквы верхнего и нижнего регистра")
            return False
        return True
    """
    функция проверки пароля на наличие цифр
    """
    def password_num(password_checking):
        for i in range(len(password_checking)):
            if password_checking[i].isdigit():
                return True
        print("Пароль не верный, не хватает цифр")
        return False
    """
    функция проверки пароля на наличие букв в верхнем регистре
    """
    def password_upper(password_checking):
        for i in range(len(password_checking)):
            if password_checking[i].isupper():
                return True
        print("Пароль не верный, не хватает букв в верхнем регистре")
        return False
    """
    функция проверки пароля на наличие букв в нижнем регистре
    """
    def password_lower(password_checking):
        for i in range(len(password_checking)):
            if password_checking[i].islower():
                return True
        print("Пароль не верный, не хватает букв в нижнем регистре")
        return False
    """
    функция проверки пароля на верность
    """
    def password_checker(password_checking):
        if Password_registration.password_len(password_checking) == False:
            password_checking = False
        elif Password_registration.password_upper(password_checking) == False:
            password_checking = False
        elif Password_registration.password_lower(password_checking) == False:
            password_checking = False
        elif Password_registration.password_num(password_checking) == False:
            password_checking = False
        else:
            password_checking = True
        return password_checking
    

if __name__ == "__main__":
    database = Database()
    repeat = bool
    repeat = True
    while repeat == True:
        choise = input("""
Hello
1 - login:     
2 - registration 
3 - Exit 
""")
        if choise == "1":
            login = input("Логин: ")
            password = input("Пароль: ")
            if login in database.data:
                if database.data[login] == password:
                    print(f"Welcome{login}")
                else:
                    print("Неверный пароль")
            else:
                print("Пользователь не найден")
            continue

        elif choise == "2":
            user = User(login := input("Username: "), 
                        password := input("Password: "), 
                        confirm_password := input("Password confirm: "))
            if Password_registration.password_checker(password) == False:
                print("password not confirmed")
                print("Вы хотите повторить попытку?\ny - да\nn - нет")
                if b := input() == "y":
                    repeat = True
                elif b == "n":
                    repeat = False
                else:
                    repeat = False
                
            
            elif Password_registration.password_checker(password) == True:
                print("password confirmed")
                database.add_user(user.username, user.password)
                # print(login = "123")  ошибка, у нас нет логина
                # print(login := "123") # тут нет ошибки, мы присваиваем логин
                print("\nПользователь добавлен \n")
                print(database.data)
                print("Вы хотите добаввить нового пользователя?\ny - да\nn - нет")
                if a := input() == "y":
                    repeat = True
                elif a == "n":
                    repeat = False
                else:
                    repeat = False
        elif choise == "3":
            repeat = False
