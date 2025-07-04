# Создать класс Dog.
# Класс имеет четыре атрибута: height, weight, name, age.
# Класс имеет три метода: jump, run, bark.
# Каждый метод выводит сообщение на экран. Создать объект класса Dog, вызвать все
# методы объекта и вывести на экран все его атрибуты.

class Dog:
    """"
    Класс описывает собак и их характеристики.

    Атрибуты:
        height (int): Рост собаки (см).
        weight (int): Вес собаки (кг).
        name (str): Имя собаки.
        age (int): Возраст собаки.

    """

    def __init__(self, height, weight, name, age):
        self.height : int = height
        self.weight : int = weight
        self.name : str = name
        self.age : int = age

    def jump(self):
        """Возвращает строку, описывающую прыжок собаки."""
        return f"Dog {self.name} jumps!"

    def run(self):
        """Возвращает строку, описывающую бег собаки."""
        return f"Dog {self.name} runs!"

    def bark(self):
        """Возвращает строку, описывающую лай собаки."""
        return f"Dog {self.name} barks!"

    # 14.2
    def change_name(self, new_name: str):
        """Меняет атрибут name у объекта.

           Аргументы:
            new_name (str): Новое значение атрибута name.

        Возвращает:
            string: Строка с оповещением об изменении значения атрибута.
        """
        self.name = new_name
        return "Name changed!"


if __name__ == "__main__":

    dog1 = Dog(90, 20, "Bob", 7)

    print("dog1 attributes: ")
    for k,v in dog1.__dict__.items():
        print(k,v, end="\t")

    print("\n**********\n\ndog1 methods:\n")
    print(dog1.jump())
    print(dog1.run())
    print(dog1.bark())


