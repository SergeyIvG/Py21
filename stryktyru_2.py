# Задание 2
# Создайте класс очереди с приоритетами для работы с символьными значениями.

class QueuePriority:
    __characters = list()  # Список будет содержать символы
    __priority = list()    # Список для значения приоритета элемента очереди.
    __size = 0
    __capacity = 0

    def __init__(self, capacity: int):
        if capacity > 0:
            self.__capacity = capacity

    def insert_with_priority(self, element: str, priority: int):  # Метод для добавление элемента в очередь.
        if self.__size < self.__capacity:
            if element != '':                         # Если ничего не ввели в очередь не добавляю
                self.__characters.append(element[0])  # Если ввели больше одного символа в очередь добавляю первый
                self.__priority.append(priority)
                self.__size += 1
        else:
            print('переполнение - добавление невозможно')

    def pull_highest_priority_element(self):  # Метод для удаления элемента из очереди.
        if self.__size > 0:
            max_priority = max(self.__priority)
            index_max_priority = self.__priority.index(max_priority)
            popping = self.__characters.pop(index_max_priority)
            self.__priority.pop(index_max_priority)
            self.__size -= 1
            return popping
        else:
            print('пусто - удаление невозможно')
            return None

    def peek(self):  # Метод для возврата самого большого по приоритету элемента очереди без удаления.
        if self.__size > 0:
            max_priority = max(self.__priority)
            index_max_priority = self.__priority.index(max_priority)
            max_priority_element = self.__characters[index_max_priority]
            return max_priority_element
        else:
            print('пусто - получение элемента невозможно')
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
        if self.__size > 0:
            print('Элементы   -', self.__characters)
            print('Приоритеты -', self.__priority)
        else:
            print('Нет элементов для вывода')


def menu_choice():    # Функция для отображение на экране меню выбора.
    print('\n1 — проверка очереди на пустоту')
    print('2 — проверка очереди на заполнение')
    print('3 — добавление элемента c приоритетом в очередь')
    print('4 — удаление элемента с самым высоким приоритетом из очереди')
    print('5 — возврат самого большого по приоритету элемента')
    print('6 — отображение всех элементов очереди на экран')
    print('0 — завершение работы программы\n')
    return input('Выберите пункт меню: ')


def choice_action(choice: int, obj: QueuePriority):   # Функция для обработки выбранного в меню пункта.
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
        elem = input('Введите символ для добавления: ')
        try:
            priority = int(input('Введите приоритет: '))
        except ValueError:
            print('Вы ввели не число. Приоритет будет равен 0.')
            priority = 0
        obj.insert_with_priority(elem, priority)
    elif choice == 4:
        if obj.pull_highest_priority_element():
            print('символ удален')
    elif choice == 5:
        max_priority_element = obj.peek()
        if max_priority_element:
            print('элемент с самым высоким приоритетом -', max_priority_element)
    elif choice == 6:
        obj.show()
    else:
        print('Программа завершила работу!')
    return choice


line1 = QueuePriority(7)
exit = 1
while exit:
    try:
        choice = int(menu_choice())
    except ValueError:
        print('Нужно ввести цифру от 0 до 6')
        continue
    if 0 <= choice <= 6:
        exit = choice_action(choice, line1)
