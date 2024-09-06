# #Дополнительное практическое задание по модулю

from time import sleep

class User:

    def __init__ (self, nickname, password, age):
        self.nickname = nickname
        self.pword = hash(password)
        self.age = age

    def __str__(self):
        return f'Nickname: {self.nickname}\nAge: {self.age}'
        


class Video:
    

    def __init__(self, tittle : str, duration, time_now = 0, adult_mode = False):
        self.title = tittle
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

#     def __str__(self):
#         print(f"""Название: 
# {self.title}
# Длительность: 
# {self.duration}
# Текущее время: 
# {self.time_now}
# """)


class UrTube:

    def __init__(self):
        self.user_db = {"null": [0, 0]}
        self.video_db = {"null": [0, 0, False]}

    """
Блок USER

    """
    def register(self, nickname, password, age):
        self.nickname = nickname
        self.pword = hash(password)
        self.age = age
        if self.nickname in self.user_db.keys():
            print("Пользователь уже зарегистрирован")
        else:
            self.user_db[self.nickname] = [self.pword, self.age]
            print("Пользователь успешно зарегистрирован")
            self.log_in()
        
    def log_in(self):
        if self.nickname in self.user_db.keys():
            if self.user_db[self.nickname][0] == self.pword:
                print("Вход выполнен, здравствуйте, ", self.nickname, "\n" )
            else:
                print("Неверный пароль", "\n" )
        else:
            print("Пользователь не зарегистрирован", "\n" )

    def current_user(self):
        if self.nickname not in self.user_db.keys():
            return "nonexistent"
        elif self.nickname in self.user_db.keys():
            if self.age >= 18:
                return self.nickname, True
            else:
                return self.nickname, False
        
    """
Блок VIDEO

    """

    def add(self, tittle : str, duration : int, time_now = 0, adult_mode = False):
        self.tittle = tittle
        self.duration = duration        
        self.time_now = time_now        
        self.adult_mode = adult_mode
        if self.tittle in self.video_db.keys():
            print(f"Видео {self.tittle} уже существует")
        else:
            self.video_db[self.tittle] = [self.duration, self.time_now, self.adult_mode]
            print("Видео успешно добавлено")

    def watch_video(self, tittle : str):
        if self.current_user() == "nonexistent":
            print("Войдите в аккаунт, чтобы смотреть видео")
        else:
            if tittle in self.video_db.keys():
                if self.video_db[tittle][2] == True and self.current_user()[1] == True:
                    while self.video_db[tittle][1] < self.video_db[tittle][0]:
                        sleep(1)
                        self.video_db[tittle][1] += 1
                        if self.video_db[tittle][0] - self.video_db[tittle][1] >= 10 and self.video_db[tittle][0] - self.video_db[tittle][1] == 0:
                            print(self.video_db[tittle][0] - self.video_db[tittle][1], "секунд осталось")
                    print(f"Видео {tittle} просмотрено")
                elif self.video_db[tittle][2] == False:
                    print(f"Вам нет 18 лет, пожалуйста покиньте страницу")

                self.video_db[tittle][1] += 1
                if self.video_db[tittle][2] == True:
                    print(f"Видео {tittle} просмотрено")
            else:
                print(f"Видео {tittle} не существует")

    # def tittles(self):
    #     print("Список видео:")
    #     print(self.video_db.keys())
    #     for i in self.video_db.keys():
    #         print(self.video_db.keys())   



ur = UrTube()

v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
# print(ur.get_videos('лучший'))
# print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
