# Добавить в класс Dog метод change_name.
# Метод принимает на вход новое имя и меняет
# атрибут имени у объекта. Создать один объект класса.
# Вывести имя. Вызвать метод change_name. Вывести имя.
from HW_14_1 import Dog

dog2 = Dog(150, 25, "Mitch", 4)

print("Old name:", dog2.name)

dog2.change_name("Spike")

print("New name:", dog2.name)