# Расширьте в классе Person метод, который считает год рождения: добавьте вывод,
# что человек пойдет в армию в таком-то году, если это мужчина допризывного возраста.

# Считается, что в армию забирают с 18 лет
# Создайте Васю допризывного возраста и Катю. Вызовите для каждого человека этот метод.


class Person:
    """
        Класс представляет людей с уникальными именами и полом, возрастом 15 лет

        Атрибуты:
            year (int): Текущий год.
            name (str): Имя.
            sex (str): Пол.
            age (int): Возраст.

        """

    year = 2025

    def __init__(self, name, sex):
        self.name = name
        self.age = 15
        self.sex = sex

    def find_age(self):

        """
                Вычисляет год рождения человека, проверяет, соответствует ли пол и возраст призыву в армию. Если пол мужской, но человек
                не достиг призывного возраста, вычисляет, в каком году человек будет призван.

                Аргументы:
                    Не принимает аргументов

                Возвращает:
                    f-string: Строка с годом рождения и достиг/не достиг призывного возраста,
                    в каком году будет призван.


        """
        birth_year = self.year - self.age

        if self.sex == "male":
            if self.age < 18:
                return (f"{self.name} was born in {birth_year} year. "
                        f"{self.name} is below conscription age. Expected to be conscripted in {birth_year + 18} year.")
            else:
                return (f"{self.name} was born in {birth_year} year."
         
                        f"{self.name} has reached conscription age.")

        else:
            return (f"{self.name} was born in {birth_year} year. "
                        f"{self.name} is not subject to conscription because she is female.")



if __name__ == "__main__":

    person1 = Person("Kate", "female")
    person2 = Person("Vasya", "male")

    print(person1.find_age())
    print(person2.find_age())