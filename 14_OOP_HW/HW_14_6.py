class Pet:
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
        """Увеличивает возраст питомца на 1 и возвращает поздравление"""
        self.age += 1
        return f"{self.name} has B-day today!"


class Dog(Pet):
    """
          Класс, представляющий собаку.

          Наследует от:
              Pet

          Методы:
              bark(): Возвращает строку, описывающую лай собаки.
    """

    def bark(self):
        """Возвращает строку, описывающую лай собаки."""
        return f"{self.name} is barking"


class Cat(Pet):
    """
        Класс описывает кошек и их характеристики.

        Наследует от:
            Pet

        Методы:
            meow(): Возвращает строку, описывающую мяуканье кошки.
        """
    def meow(self):
        """Возвращает строку, описывающую мяуканье кошки."""
        return f"{self.name} is meowing"


class Parrot(Pet):
    """
        Класс, представляющий попугая.

        Наследует от:
            Pet

        Методы:
            fly(): Возвращает строку, описывающую полёт попугая.
    """

    def fly(self):
        """Возвращает строку, описывающую полёт попугая."""
        return f"{self.name} is flying"


if __name__ == "__main__":

    dog = Dog("Steve", 3, "Dave")
    cat = Cat("Garfield", 5, "John")
    parrot = Parrot("Buddy", 2, "Kate")

    print(dog.run())
    print(dog.jump())
    print(dog.birthday())
    print(dog.bark())
    print()
    print(cat.run())
    print(cat.jump())
    print(cat.birthday())
    print(cat.meow())
    print()
    print(parrot.run())
    print(parrot.jump())
    print(parrot.birthday())
    print(parrot.fly())


