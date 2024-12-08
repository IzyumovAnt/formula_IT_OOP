import doctest
import math
from typing import Union


class Rectangle:
    def __init__(self, small_side: Union[int, float], large_side: Union[int, float]):
        """
        Создание и подготовка к работе объекта "Прямоугольник"

        :param small_side: Длина меньшей стороны прямоугольника
        :param large_side: Длина большей стороны прямоугольника

        Примеры:
        >>> rectangle = Rectangle(40, 60)
        """
        if not isinstance(small_side, (int, float)):
            raise TypeError("Длина меньшей стороны должна быть числом")
        if not small_side > 0:
            raise ValueError("Меньшая сторона должна иметь положительную длину")
        self.small_side = small_side

        if not isinstance(large_side, (int, float)):
            raise TypeError("Длина большей стороны должна быть числом")
        if not large_side > small_side:
            raise ValueError("Большая сторона должна иметь большую длину, чем меньшая")
        self.large_side = large_side

    def calculate_area(self) -> Union[int, float]:
        """
        Функция, которая считает площадь прямоугольника

        :return: Площадь прямоугольника

        Примеры:
        >>> rectangle = Rectangle(40, 60)
        >>> rectangle.calculate_area()
        2400
        """
        return self.large_side * self.small_side

    def calculate_perimeter(self) -> Union[int, float]:
        """
        Функция, которая считает периметр прямоугольника

        :return: Периметр прямоугольника

        Примеры:
        >>> rectangle = Rectangle(40, 60)
        >>> rectangle.calculate_perimeter()
        200
        """
        return 2 * (self.large_side + self.small_side)

    def calculate_diagonal(self) -> Union[int, float]:
        """
        Функция, которая вычисляет длину диагонали прямоугольника

        :return: Длина диагонали прямоугольника

        Примеры:
        >>> rectangle = Rectangle(40, 60)
        >>> rectangle.calculate_diagonal()
        72.11
        """
        return round(math.sqrt(self.large_side ** 2 + self.small_side ** 2), 2)


class Triangle:
    def __init__(self, side1: Union[int, float], side2: Union[int, float], side3: Union[int, float]):
        """
        Создание и подготовка к работе объекта "Треугольник"

        :param side1: Длина стороны 1
        :param side2: Длина стороны 2
        :param side3: Длина стороны 3

        Примеры:
        >>> triangle = Triangle(45, 54, 61)
        """
        if not isinstance(side1, (int, float)):
            raise TypeError("Длина стороны 1 должна быть числом")
        if not side1 > 0:
            raise ValueError("Сторона 1 должна иметь положительную длину")
        self.side1 = side1

        if not isinstance(side2, (int, float)):
            raise TypeError("Длина стороны 2 должна быть числом")
        if not side2 > 0:
            raise ValueError("Сторона 2 должна иметь положительную длину")
        self.side2 = side2

        if not isinstance(side3, (int, float)):
            raise TypeError("Длина стороны 3 должна быть числом")
        if not side3 > 0:
            raise ValueError("Сторона 3 должна иметь положительную длину")
        self.side3 = side3

    def calculate_area(self) -> Union[int, float]:
        """
        Функция для вычисления площади треугольника

        :return: Площадь треугольника

        Примеры:
        >>> triangle = Triangle(45, 54, 61)
        >>> triangle.calculate_area()
        1176.1
        """
        p = (self.side1 + self.side2 + self.side3) / 2  # полупериметр треугольника
        area = math.sqrt(p * (p - self.side1) * (p - self.side2) * (p - self.side3))
        return round(area, 2)

    def is_equilateral(self) -> bool:
        """
        Функция для распознавания равнобедренных треугольников

        :return: Является ли треугольник равнобедренным

        Примеры:
        >>> triangle = Triangle(45, 54, 61)
        >>> triangle.is_equilateral()
        False
        >>> triangle = Triangle(70, 54, 70)
        >>> triangle.is_equilateral()
        True
        """
        if self.side1 == self.side2 or self.side1 == self.side3 or self.side2 == self.side3:
            return True
        return False

    def prisma_volume(self, prisma_height: Union[int, float]) -> Union[int, float]:
        """
        Функция для вычисления объёма треугольной призмы

        :param prisma_height: Высота треугольной призмы
        :return: Объём треугольной призмы

        Примеры:
        >>> triangle = Triangle(45, 54, 61)
        >>> triangle.prisma_volume(5)
        5880.5
        """
        if not isinstance(prisma_height, (int, float)):
            raise TypeError("Высота призмы должна быть числом")
        if not prisma_height > 0:
            raise ValueError("Высота призмы должны быть положительна")
        return self.calculate_area() * prisma_height


class Cylinder:
    def __init__(self, radius: Union[int, float], height: Union[int, float]):
        """
        Создание и подготовка к работе объекта "Цилиндр"

        :param radius: Радиус основания
        :param height: Высота цилиндра

        Примеры:
        >>> cylinder = Cylinder(2, 7.5)
        """
        if not isinstance(radius, (int, float)):
            raise TypeError("Радиус основания должен быть числом")
        if not radius > 0:
            raise ValueError("Радиус основания должен быть положителен")
        self.radius = radius

        if not isinstance(height, (int, float)):
            raise TypeError("Высота цилиндра должна быть числом")
        if not height > 0:
            raise ValueError("Высота цилиндра должна быть положительна")
        self.height = height

    def calculate_area(self) -> Union[int, float]:
        """
        Функция для вычисления площади поверхности цилиндра

        :return: Площадь поверхности цилиндра

        Примеры:
        >>> cylinder = Cylinder(2, 7.5)
        >>> cylinder.calculate_area()
        119.38
        """
        return round(2 * math.pi * self.radius * (self.radius + self.height), 2)

    def calculate_volume(self) -> Union[int, float]:
        """
        Функция для вычисления объёма цилиндра

        :return: Объём цилиндра

        Примеры:
        >>> cylinder = Cylinder(2, 7.5)
        >>> cylinder.calculate_volume()
        94.25
        """
        return round(math.pi * self.height * self.radius ** 2, 2)


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
