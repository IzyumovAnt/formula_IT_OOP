class Pet:
    """
    Базовый класс для домашних животных
    """
    def __init__(self, name: str, age: int) -> None:
        """
        Инициализирует атрибуты имени и возраста питомца.

        :param name: Имя питомца
        :param age: Возраст питомца
        """
        self._name = name  # Инкапсуляция, так как атрибут неизменяемый
        self.age = age  # Инкапсуляция, так как необходимы проверки ввода

    def __str__(self) -> str:
        """
        :return: Строковое представление объекта
        """
        return f'Питомец {self.name}, возраст {self.age}'

    def __repr__(self) -> str:
        """
        :return: Строковое представление объекта для отладки
        """
        return f'{self.__class__.__name__}(name={self.name!r}, age={self.age})'

    def make_sound(self) -> str:
        """
        :return: Звук питомца
        """
        return f'Питомец издаёт звук'

    def age_in_human_years(self) -> int:
        """
        Метод для вычисления возраста питомца в человеческих годах

        :return: Возраст питомца в человеческих годах
        """
        return self.age * 7

    @property
    def name(self) -> str:
        """Геттер, чтобы сделать атрибут неизменяемым"""
        return self._name

    @property
    def age(self) -> int:
        """Геттер для возвращения защищенного атрибута"""
        return self._age

    @age.setter
    def age(self, age: int) -> None:
        """Сеттер для проведения необходимых проверок"""
        if not isinstance(age, int):
            raise TypeError("Возраст питомца должен быть типа int")
        if age < 0:
            raise ValueError("Возраст не может быть отрицательным")
        self._age = age


class Dog(Pet):
    """
    Дочерний класс, представляющий собаку.
    """
    def __init__(self, name: str, age: int, breed: str) -> None:
        """
        Инициализирует атрибуты родительского класса и добавляет новую характеристику.

        :param name: Имя собаки
        :param age: Возраст собаки
        :param breed: Порода собаки
        """
        super().__init__(name, age)
        self._breed = breed  # Инкапсуляция, так как атрибут не должен изменяться

    def __str__(self) -> str:
        """
        Перегрузка метода для включения информации о породе.

        :return: Строковое представление объекта
        """
        return f'Собака {self.name}, возраст {self.age}, порода {self.breed}'

    def __repr__(self) -> str:
        """
        Перегрузка метода в связи с добавлением информации о породе.

        :return: Строковое представление объекта для отладки
        """
        return f'{self.__class__.__name__}(name={self.name!r}, age={self.age}, breed={self.breed!r})'

    def make_sound(self) -> str:
        """
        Метод перегружен, так как собаки лают.

        :return: Звук, который издаёт собака
        """
        return "Гав-гав!"

    @property
    def breed(self) -> str:
        """Геттер, чтобы сделать атрибут неизменяемым"""
        return self._breed


if __name__ == "__main__":
    bars = Pet("Барсик", 7)
    print(bars)
    print(repr(bars))
    print(bars.make_sound())

    shar = Dog("Шарик", 10, "Немецкая овчарка")
    print(shar)
    print(repr(shar))
    print(shar.age_in_human_years())
    shar.age = 12
    print(shar.age)
    print(shar.make_sound())
