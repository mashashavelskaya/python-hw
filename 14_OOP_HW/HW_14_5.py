class Dog:
    """"
        Класс описывает собак и их характеристики.

        Атрибуты:
            name (str): Имя собаки.
            age (int): Возраст собаки.
            master (str): Имя владельца собаки.

        Методы:
            jump(self): Возвращает строку, описывающую прыжок собаки.
            run(self): Возвращает строку, описывающую бег собаки.
            bark(self): Возвращает строку, описывающую лай собаки.
            birthday(): Увеличивает возраст питомца на 1 и возвращает поздравление.

        """

    def __init__(self, name, age, master):
        self.name = name
        self.age = age
        self.master = master

    def run(self):
        return f"{self.name} is running"

    def jump(self):
        return f"{self.name} is jumping"

    def birthday(self):
        self.age += 1
        return f"{self.name} has B-day today!"

    def bark(self):
        return f"{self.name} is barking"


class Cat:
    """"
            Класс описывает кошек и их характеристики.

            Атрибуты:
                name (str): Имя кошки.
                age (int): Возраст кошки.
                master (str): Имя владельца кошки.

            Методы:
                jump(self): Возвращает строку, описывающую прыжок кошки.
                run(self): Возвращает строку, описывающую бег кошки.
                meow(self): Возвращает строку, описывающую мяуканье кошки.
                birthday(): Увеличивает возраст кошки на 1 и возвращает поздравление.

            """
    def __init__(self, name, age, master):
        self.name = name
        self.age = age
        self.master = master

    def run(self):
        return f"{self.name} is running"

    def jump(self):
        return f"{self.name} is jumping"

    def birthday(self):
        self.age += 1
        return f"{self.name} has B-day today!"

    def meow(self):
        return f"{self.name} is meowing"


class Parrot:
    """"
                Класс описывает попугаев и их характеристики.

                Атрибуты:
                    name (str): Имя попугая.
                    age (int): Возраст попугая.
                    master (str): Имя владельца попугая.

                Методы:
                    jump(self): Возвращает строку, описывающую прыжок попугая.
                    run(self): Возвращает строку, описывающую бег попугая.
                    fly(self): Возвращает строку, описывающую полёт попугая.
                    birthday(): Увеличивает возраст попугая на 1 и возвращает поздравление.

                """

    def __init__(self, name, age, master):
        self.name = name
        self.age = age
        self.master = master

    def run(self):
        return f"{self.name} is running"

    def jump(self):
        return f"{self.name} is jumping"

    def birthday(self):
        self.age += 1
        return f"{self.name} has B-day today!"

    def fly(self):
        return f"{self.name} is flying"

