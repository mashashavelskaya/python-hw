class Dog:
    """"
    Класс описывает собак и их характеристики.

    Атрибуты:
        height (int): Рост собаки (см).
        weight (int): Вес собаки (кг).
        name (str): Имя собаки.
        age (int): Возраст собаки.
        __master (str): Имя хозяина собаки (приватный атрибут)

    Методы:
        master (str): Возвращает имя хозяина собаки (read-only).

    """

    def __init__(self, height, weight, name, age, master):
        self.height : int = height
        self.weight : int = weight
        self.name : str = name
        self.age : int = age
        self.__master = master

    def jump(self):
        """Возвращает строку, описывающую прыжок собаки."""
        return f"Dog {self.name} jumps!"

    def run(self):
        """Возвращает строку, описывающую бег собаки."""
        return f"Dog {self.name} runs!"

    def bark(self):
        """Возвращает строку, описывающую лай собаки."""
        return f"Dog {self.name} barks!"


    def change_name(self, new_name: str):
        """Меняет атрибут name у объекта.

           Аргументы:
            new_name (str): Новое значение атрибута name.

        Возвращает:
            string: Строка с оповещением об изменении значения атрибута.
        """
        self.name = new_name
        return "Name changed!"

    @property
    def get_master(self):
        """Возвращает имя хозяина собаки"""
        return f"Master: {self.__master}"


if __name__ == "__main__":

    dog1 = Dog(90, 20, "Bob", 7, "Jason")

    print(dog1.get_master)

