class Person:
    max_up = 3
    def __init__(self, name='', race='unknown'):
        self.name = name
        self.race = race
        self.level = 1
        self.health = 100
    def level_up(self):
        self.level += 1
    def change_health(self, other, quantity):
        self.health += quantity
        other.health -= quantity

p1 = Person()
print(p1.max_up)
print(Person.max_up)

p1 = Person()
p2 = Person()
print(f'{Person.max_up = }, {p1.max_up = }, {p2.max_up = }')
p1.max_up = 12
print(f'{Person.max_up = }, {p1.max_up = }, {p2.max_up = }')
Person.max_up = 42
print(f'{Person.max_up = }, {p1.max_up = }, {p2.max_up = }')




p1 = Person()
p2 = Person()
Person.level = 1
print(f'{Person.level = }, {p1.level = }, {p2.level = }')
p1.health = 100
#print(f'{Person.health = }, {p1.health = }, {p2.health = }') #AttributeError: type object 'Person' has no attribute 'health'
#print(f'{p1.health = }, {p2.health = }') # AttributeError:'Person' object has no attribute 'health'
print(f'{p1.health = }')



p1 = Person()
p2 = Person()
print(f'{p1.max_up = }, {p1.level = }, {p1.health = }')
print(f'{p2.max_up = }, {p2.level = }, {p2.health = }')
#print(f'{Person.max_up = }, {Person.level = }, {Person.health =}') # AttributeError: type object 'Person' has no attribute'level'
Person.level = 100
print(f'{Person.level = }, {p1.level = }, {p2.level = }')


p1 = Person('Сильвана', 'Эльф')
p2 = Person('Иван', 'Человек')
p3 = Person('Грогу')
print(f'{p1.name = }, {p1.race = }')
print(f'{p2.name = }, {p2.race = }')
print(f'{p3.name = }, {p3.race = }')

print(f'{p1.level = }, {p2.level = }, {p3.level = }')
p3.level_up()
p1.level_up()
p3.level_up()
print(f'{p1.level = }, {p2.level = }, {p3.level = }')

print(f'{p1.health = }, {p2.health = }, {p3.health = }')
p1.change_health(p2, 10)
print(f'{p1.health = }, {p2.health = }, {p3.health = }')