from abc import ABC, abstractmethod

class CheckPositive:
    """
        Дескриптор, который запрещает устанавливать возраст <= 0.
    """

    # метод для получения имени атрибута (name)
    # теперь в self.name лежит имя атрибута, для которого вызывается дескриптор
    def __set_name__(self, owner, name):
        self.name = name

    # Getter
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]


    # Setter
    def __set__(self, instance, value: int):
        if value <= 0:
            raise ValueError(f"Attribute '{self.name}' must be greater than 0.")
        instance.__dict__[self.name] = value



class CheckNotEmptyString:
    """
        Дескриптор, который запрещает устанавливать имя питомца и
        имя хозяина как пустые строки.
    """
    # метод для получения имени атрибута (name)
    # теперь в self.name лежит имя атрибута, для которого вызывается дескриптор
    def __set_name__(self, owner, name : str):
        self.name = name

    # Getter
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    # Setter
    def __set__(self, instance, value: str):
        if value == "" or value.isspace():
            raise ValueError(f"Attribute '{self.name}' can't be an empty string")
        instance.__dict__[self.name] = value



class Pet(ABC):
    """
       Базовый класс для всех домашних животных.

       Атрибуты:
           name (str): Имя питомца.
           age (int): Возраст питомца.
           master (str): Имя владельца питомца.

       Методы:
           run(): Возвращает строку, описывающую бег питомца.
           jump(): Возвращает строку, описывающую прыжок питомца.
           birthday(): Увеличивает возраст питомца на 1 и возвращает поздравление.
       """

    age = CheckPositive()

    name, master = CheckNotEmptyString(), CheckNotEmptyString()

    def __init__(self, name, age, master):
        """
             Инициализация объекта Pet.

             Параметры:
                 name (str): Имя питомца.
                 age (int): Возраст питомца.
                 master (str): Владелец питомца.
        """
        self.name = name
        self.age = age
        self.master = master

    def run(self):
        """Возвращает строку, описывающую бег питомца."""
        return f"{self.name} is running"

    def jump(self):
        """Возвращает строку, описывающую прыжок питомца."""
        return f"{self.name} is jumping"

    def birthday(self):
        """Увеличивает возраст питомца на 1 и возвращает оповещение"""
        self.age += 1
        return f"{self.name} has B-day today!"


    @abstractmethod
    def voice(self):
        pass


class Dog(Pet):
    """
          Класс, представляющий собаку.

          Наследует от:
              Pet

          Методы:
              bark(): Возвращает строку, описывающую лай собаки.
    """

    def voice(self):
        """Возвращает строку, описывающую лай собаки."""
        return "WOOF!"


class Cat(Pet):
    """
        Класс, представляющий кошку.

        Наследует от:
            Pet

        Методы:
            meow(): Возвращает строку, описывающую мяуканье кошки.
        """

    def voice(self):
        """Возвращает строку, описывающую мяуканье кошки."""
        return "MEOW!"


class Parrot(Pet):
    """
        Класс, представляющий попугая.

        Наследует от:
            Pet

        Методы:
            fly(): Возвращает строку, описывающую полёт попугая.
    """

    def voice(self):
        """Возвращает строку, описывающую чириканье попугая."""
        return "CHIRP!"


if __name__ == "__main__":

    parrot = Parrot("Sam", 2, "Mike")

    print(parrot.name)
    parrot.name = "    "






