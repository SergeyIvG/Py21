import math


#   Задание 1
# Создать базовый класс Фигура с методом для подсчета площади.
# Создать производные классы: прямоугольник, круг, прямоугольный треугольник, трапеция
# со своими методами для подсчета площади.
#   Задание 2
# переопределить магические методы
# int(возвращает площадь) и str (возвращает информацию о фигуре).
class Figure:
    def __init__(self, length):
        self.length = self.input_len(length)    # длина фигуры

    def input_len(self, number):
        if str(number).isdigit():
            return number
        else:
            return 0

    def area(self):
        return self.length * 0  # площадь фигуры

    def __str__(self):
        return f' Отрезок.\n' \
               f' length: {self.length} \tДлина отрезка\n'

    def __int__(self):
        return int(self.area())


class Rectangle(Figure):    # класс прямоугольник
    def __init__(self, length, height):
        super().__init__(length)   # длина от родителя
        self.height = self.input_len(height)            # высота

    def area(self):
        return self.length * self.height    # площадь прямоугольника

    def __str__(self):
        return f' Прямоугольник.\n' \
               f' length: {self.length}  \tдлина первой стороны прямоугольника\n' \
               f' height: {self.height}  \tдлина второй стороны прямоугольника\n'


class Circle(Figure):           # класс круг
    def __init__(self, radius):
        super().__init__(radius)       # радиус записываем в свойство длина

    def area(self):
        return math.pi * (self.length ** 2)     # площадь круга

    def __str__(self):
        return f' Круг.\n' \
               f' length: {self.length} \tрадиус круга\n'


class Triangle(Figure):         # класс прямоугольный треугольник
    def __init__(self, length, height):
        super().__init__(length)  # длина от родителя
        self.height = self.input_len(height)           # высота

    def area(self):
        return self.length * self.height * 0.5    # площадь прямоугольного треугольника

    def __str__(self):
        return f' Прямоугольный треугольник.\n' \
               f' length: {self.length}  \tдлина первого катета\n' \
               f' height: {self.height}  \tдлина второго катета\n'


class Trapezoid(Figure):            # класс трапеция
    def __init__(self, length_bottom, length_top, height):
        super().__init__(length_bottom)  # длина первого основания
        self.length_top = self.input_len(length_top)          # длина второго основания
        self.height = self.input_len(height)                  # высота

    def area(self):
        return (self.length + self.length_top) * self.height / 2    # площадь трапеции

    def __str__(self):
        return f' Трапеция.\n' \
               f' length: {self.length}  \t\tдлина нижнего основания\n' \
               f' length_top: {self.length_top}  \tдлина верхнего основания\n' \
               f' height: {self.height}  \t\tвысота\n'


first_figure = Figure(3)
first_rectangle = Rectangle(4, 5)
first_circle = Circle(6)
first_triangle = Triangle(7, 8)
first_trapezoid = Trapezoid(12, 4, 9)
print('Площадь посчитана через вызов метода класса')
print(first_figure.area())
print(first_rectangle.area())
print(first_circle.area())
print(first_triangle.area())
print(first_trapezoid.area())
print('\n__STR__')
print(first_figure)
print(first_rectangle)
print(first_circle)
print(first_triangle)
print(first_trapezoid)
print('\n__INT__')
print(int(first_figure))
print(int(first_rectangle))
print(int(first_circle))
print(int(first_triangle))
print(int(first_trapezoid))
