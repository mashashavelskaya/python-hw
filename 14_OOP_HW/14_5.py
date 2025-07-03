# Добавьте в класс Porsche метод, который считает пробег,
# а также выводит пробег и сколько за сегодня проехал порш.
# Создайте 1 порш и 2 раза вызовите метод

class Porsche:
    """
    Класс представляет автомобиль марки Porsche.

    Атрибуты:
        color (str): Цвет машины.
        year (int): Год выпуска.
        mileage (float): Общий пробег автомобиля.

    """
    model = "Macan"

    def __init__(self, color, year, mileage):
        self.color : str = color
        self.year : int = year

        # Общий пробег будет уникальным атрибутом каждого авто
        self.mileage : float = mileage

    def calc_mileage(self, mileage_today):

        """
        Добавляет к пробегу километраж, пройденный за день.

        Аргументы:
            mileage_today (float): Пробег за сегодня в километрах.

        Возвращает:
            f-string: Строка с сегодняшним и общим пробегом.


        """
        self.mileage = self.mileage + mileage_today
        return (f"Today's mileage is {mileage_today} km.\n"
                f"Total mileage is {self.mileage} km.")


if __name__ == "__main__":

    porsche1 = Porsche("Blue", 2010, 200500.5)

    print(porsche1.calc_mileage(80.7))
    print()
    print(porsche1.calc_mileage(120.3))


