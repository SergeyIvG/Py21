# Задание 3
# Создайте приложение, которое позволит сохранять информацию о логинах пользователей и их паролях.
# Пользователь это пара логин-пароль

class LogKeeper:
    __log_book = dict()  # В качестве структуры данных для хранения использую словарь

    def __enter_password(self):  # Метод для ввода пароля - должен быть больше 7 символов
        len(self.__log_book)
        while True:              # пароль должен содержать и цифры и маленькие и большие буквы
            password = input('Введите пароль: ')
            if len(password) < 8:
                print('Пароль должен быть не меньше 8 символов. Выберите другой.')
                continue
            if password.isdigit():
                print('Пароль не может содержать только цифры')
                continue
            elif password.isalpha():
                print('Пароль не может содержать только буквы')
                continue
            elif password.islower():
                print('Пароль не может содержать буквы только в нижнем регистре')
                continue
            elif password.isupper():
                print('Пароль не может содержать буквы только в верхнем регистре')
                continue
            password_ok = 0
            valid_char = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_'
            for i in range(len(password)):
                if password[i] in valid_char:
                    password_ok += 1
                else:
                    print('Пароль содержит недопустимые символы')
                    break
            if password_ok == len(password):
                return password

    def __enter_login(self):  # Метод для ввода логина (с проверкой чтобы не повторялся)
        while True:
            login = input('Введите логин: ')
            if len(login) < 6:
                print('Логин должен быть не меньше 6 символов. Выберите другой.')
                continue
            login_ok = 0
            valid_char = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_'
            for i in range(len(login)):
                if login[i] in valid_char:
                    login_ok += 1
                else:
                    print('Логин содержит недопустимые символы')
                    break
            if login_ok == len(login):
                if self.is_exist(login):
                    print('Этот логин уже есть. Выберите другой.')
                    continue
                return login

    def is_exist(self, login: str):  # Метод для проверки есть ли такой логин
        if login in self.__log_book:
            return True
        else:
            return False

    def __add(self, login: str, password: str):  # Метод для добавления в словарь
        self.__log_book[login] = password

    def __pop(self, login: str):  # Метод для удаления из словаря
        del self.__log_book[login]

    def change_password(self, login: str):  # Метод для изменения пароля
        if self.is_exist(login):
            old_password = input('Введите старый пароль: ')  # Менять пароль может тот кто его знает
            if old_password == self.__log_book[login]:
                new_password = self.__enter_password()
                self.__add(login, new_password)
            else:
                print('Пароль неверный')
        else:
            print('Логин не существует')

    def change_login(self, login: str):  # Метод для изменения логина
        new_login = login
        if self.is_exist(login):
            password = input('Введите пароль: ')  # Менять логин может тот кто знает к нему пароль
            if password == self.__log_book[login]:
                new_login = self.__enter_login()
                self.__pop(login)
                self.__add(new_login, password)
            else:
                print('Пароль неверный')
        else:
            print('Логин не существует')
        return new_login

    def new_element(self):  # Метод для создания  новой пары логин-пароль
        login = self.__enter_login()        # Запрашиваем логин
        password = self.__enter_password()  # Запрашиваем пароль
        self.__add(login, password)         # Добавляем в хранилище
        return login

    def del_element(self, login):  # Метод для удаления  пары логин-пароль
        if self.is_exist(login):
            password = input('Введите пароль: ')   # Удалять может тот кто знает пароль
            if password == self.__log_book[login]:
                self.__pop(login)
            else:
                print('Пароль неверный')
        else:
            print('Логин не существует')


def menu_choice():
    print('\n1 — Добавить нового пользователя')
    print('2 — Удалить существующего пользователя')
    print('3 — Проверить существует ли пользователь')
    print('4 — Изменить логин существующего пользователя')
    print('5 — Изменить пароль существующего пользователя')
    print('0 — Завершение работы программы\n')
    return input('Выберите пункт меню: ')


def choice_action(choice: int, obj: LogKeeper):
    if choice == 1:
        obj.new_element()
    elif choice == 2:
        login = input('Введите логин для удаления: ')
        obj.del_element(login)
    elif choice == 3:
        login = input('Введите логин для проверки: ')
        if obj.is_exist(login):
            print('Пользователь существует')
        else:
            print('Пользователя не существует')
    elif choice == 4:
        login = input('Введите логин для изменения: ')
        obj.change_login(login)
    elif choice == 5:
        login = input('Введите логин для изменения пароля: ')
        obj.change_password(login)
    else:
        print('Программа завершила работу!')
    return choice


book = LogKeeper()
exit = 1
while exit:
    try:
        choice = int(menu_choice())
    except ValueError:
        print('Нужно ввести цифру от 0 до 5')
        continue
    if 0 <= choice <= 5:
        exit = choice_action(choice, book)
