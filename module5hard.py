import time

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age


class Video:
    def __init__(self, title, duration, time_now = 0, adult_mode = False ):
        self.title = title
        self.duration = duration
        self.adult_mode = adult_mode

    def __str__(self):
        return self.title

class UrTube:
    def __init__(self):
        self.users = {}
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        if nickname not in self.users:
            print("Пользователь не найден")
        for user in self.users:
            if user.nickname == nickname and user.password == password:
                self.current_user = user

    def register(self,nickname, password, age ):
        if nickname in self.users:
            return print(f'Пользователь {nickname} уже существует')
        else:
            self.users[nickname] = User(nickname, password, age)
            self.current_user = self.users[nickname]

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        for i in args:
            if str(i) not in self.videos:
                self.videos.append(i)

    def get_videos(self, search_word):
        search_video = []
        for i in self.videos:
            if search_word.lower() in i.title.lower():
                search_video.append(str(i))
        return search_video

    def watch_video(self,search_film):
        if self.current_user is None:
            print('Войдите в аккаунт, чтобы смотреть видео')
        else:
            for i in self.videos:
                if i.title == search_film:
                    if i.adult_mode == True and self.current_user.age < 18:
                        print('Вам нет 18 лет, пожалуйста покиньте страницу')
                    else:
                        while i.time_now < i.duration:
                            i.time_now += 1
                            print(i.time_now, end=' ')
                            time.sleep(1)
                        print('Конец видео')
                    i.time_now = 0






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