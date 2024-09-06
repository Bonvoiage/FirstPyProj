from time import sleep

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return f'Nickname: {self.nickname}\nAge: {self.age}'


class Video:
    def __init__(self, title: str, duration: int, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __str__(self):
        return f"Title: {self.title}, Duration: {self.duration}, Time Now: {self.time_now}, Adult Mode: {self.adult_mode}"


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def register(self, nickname, password, age):
        # Проверяем, существует ли пользователь
        for user in self.users:
            if user.nickname == nickname:
                print(f"Пользователь {nickname} уже существует")
                return

        # Создаем и добавляем нового пользователя
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user
        print(f"Пользователь {nickname} успешно зарегистрирован и вошел в систему")

    def log_in(self, nickname, password):
        # Ищем пользователя с указанными данными
        for user in self.users:
            if user.nickname == nickname and user.password == hash(password):
                self.current_user = user
                print(f"Вход выполнен, здравствуйте, {nickname}")
                return
        print("Неверный логин или пароль")

    def log_out(self):
        self.current_user = None
        print("Выход из учетной записи выполнен")

    def add(self, *videos):
        for video in videos:
            if any(v.title == video.title for v in self.videos):
                print(f"Видео '{video.title}' уже существует")
            else:
                self.videos.append(video)
                print(f"Видео '{video.title}' успешно добавлено")

    def get_videos(self, search_word):
        search_word = search_word.lower()
        result = [video.title for video in self.videos if search_word in video.title.lower()]
        return result

    def watch_video(self, title):
        if not self.current_user:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return

        # Поиск видео
        video = next((v for v in self.videos if v.title == title), None)
        if not video:
            print("Видео не найдено")
            return

        # Проверка возрастного ограничения
        if video.adult_mode and self.current_user.age < 18:
            print("Вам нет 18 лет, пожалуйста покиньте страницу")
            return

        # Воспроизведение видео
        for second in range(video.time_now + 1, video.duration + 1):
            print(second, end=' ', flush=True)
            sleep(1)
        print("\nКонец видео")
        video.time_now = 0


# Пример использования
ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

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
