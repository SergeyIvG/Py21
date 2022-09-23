# Задание 1
# Создайте класс очереди для работы с символьными значениями.

class Queue:
    __characters = list()  # Список будет содержать символы
    __size = 0
    __capacity = 0

    def __init__(self, capacity: int):
        if capacity > 0:
            self.__capacity = capacity

    def enqueue(self, element: str):  # Метод для добавление элемента в очередь.
        if self.__size < self.__capacity:
            if element != '':  # Если ничего не ввели в очередь не добавляю
                self.__characters.append(element[0])  # Если ввели больше одного символа в очередь добавляю первый
                self.__size += 1
        else:
            print('переполнение - добавление невозможно')

    def dequeue(self):  # Метод для удаления элемента из очереди.
        if self.__size > 0:
            popping = self.__characters.pop(0)
            self.__size -= 1
            return popping
        else:
            print('пусто - удаление невозможно')
            return None

    def get_capacity(self):
        return self.__capacity

    def get_size(self):
        return self.__size

    def is_empty(self):   # Метод для проверки очереди на пустоту.
        if self.__size == 0:
            return True
        else:
            return False

    def is_full(self):   # Метод для проверки очереди на заполнение.
        if self.__size == self.__capacity:
            return True
        else:
            return False

    def show(self):   # Метод для отображение всех элементов очереди на экран.
        print(self.__characters)


def menu_choice():    # Функция для отображение на экране меню выбора.
    print('\n1 — проверка очереди на пустоту')
    print('2 — проверка очереди на заполнение')
    print('3 — добавление элемента в очередь')
    print('4 — удаление элемента из очереди')
    print('5 — отображение всех элементов очереди на экран')
    print('0 — завершение работы программы\n')
    return input('Выберите пункт меню: ')


def choice_action(choice: int, obj: Queue):   # Функция для обработки выбранного в меню пункта.
    if choice == 1:
        if obj.is_empty():
            print('Очередь пустая')
        else:
            print('Очередь не пустая')
    elif choice == 2:
        if obj.is_full():
            print('Очередь заполнена')
        else:
            print('Очередь не заполнена')
    elif choice == 3:
        obj.enqueue(input('Введите символ для добавления: '))
    elif choice == 4:
        if obj.dequeue():
            print('символ удален')
    elif choice == 5:
        obj.show()
    else:
        print('Программа завершила работу!')
    return choice


line1 = Queue(5)
exit = 1
while exit:
    try:
        choice = int(menu_choice())
    except ValueError:
        print('Нужно ввести цифру от 0 до 5')
        continue
    if 0 <= choice <= 5:
        exit = choice_action(choice, line1)
