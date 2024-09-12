# Основа из предыдущей задачи
class House:
    def __init__(self, name, numb_f):
        self.name = name
        self.number_of_floor = numb_f

    def __len__(self):
        return self.number_of_floor

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floor}.'
# Создаём условия по дополнению класса House следующими специальными методами:
    def __eq__(self, other):    # 1
        if isinstance(other.number_of_floor, int) and isinstance(other, House):
            return self.number_of_floor == other.number_of_floor

    def __lt__(self, other):    # 2
        if isinstance(other.number_of_floor, int) and isinstance(other, House):
            return self.number_of_floor < other.number_of_floor

    def __le__(self, other):
        if isinstance(other.number_of_floor, int) and isinstance(other, House):
            return self.number_of_floor <= other.number_of_floor

    def __gt__(self, other):
        if isinstance(other.number_of_floor, int) and isinstance(other, House):
            return self.number_of_floor > other.number_of_floor

    def __ge__(self, other):
        if isinstance(other.number_of_floor, int) and isinstance(other, House):
            return self.number_of_floor >= other.number_of_floor

    def __ne__(self, other):
        if isinstance(other.number_of_floor, int) and isinstance(other, House):
            return self.number_of_floor != other.number_of_floor

    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floor = self.number_of_floor + value
        return self

    def __radd__(self, value):
        return self.__add__(value)

    def __iadd__(self, value):
        if isinstance(value, int):
            self.number_of_floor += value
        return self

# Вывод результатов по условиям задачи:

h1 = House('Скала', 28)
h2 = House('Хрущ', 5)

print(h1)
print(h2)
print()
# 1
print(h1 == h2)
print()
# 3
print(h2.__add__(23))
print(h1 == h2)
print()
print(h1.__add__(1))
print(h2.__add__(2))
print()
print(h2.__iadd__(5))
print(h2)
print()
print(h1.__radd__(5))
print(h1)
print()
print(h1 < h2)
print(h1 <= h2)
print(h1 > h2)
print(h1 >= h2)
print(h1 != h2)