class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def go_to(self, new_floor):
        if 0 < new_floor <= self.number_of_floors:
            for floor in range(1, new_floor + 1):
                print(floor)
        else:
            print('Такого этажа не существует')
    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: "{self.name}", кол-во этажей: {self.number_of_floors}.'
    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        self.number_of_floors += value
        return self

    def __iadd__(self, other):
        return self + other

    def __radd__(self, other):
        return self + other

House1 = House('ЖК Рублевский', 3)
House2 = House('ЖК Лайково', 54)

# House1.go_to(5)
# House1.go_to(2)
# House2.go_to(56)
# House2.go_to(34)

# print(f'{House1}\n{House2}')
# print(len(House1))
# print(len(House2))

print(House1)
print(House2)

print(House1 == House2) # __eq__

House1 = House1 + 10 # __add__
print(House1)
print(House1 == House2)

House1 += 10 # __iadd__
print(House1)

House2 += 10 # __radd__
print(House2)

print(House1 > House2) # __gt__
print(House1 >= House2) # __ge__
print(House1 < House2) # __lt__
print(House1 <= House2) # __le__
print(House1 != House2) # __ne__