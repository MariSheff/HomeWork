
class Animal:
    def __init__(self, name, space):
        self.name = name
        self.space = space

    def __str__(self):
        return self.name


class Cage:
    lst1 = []
    lst2 = []
    def __init__(self, space, animal=None, animal_space=None):
        self.space = space
        self.animal = animal
        self.animal_space = animal_space

    def add_animal(self, animal: Animal):
        if self == cage1:
            if cage1.space >= animal.space:
                cage1.animal = animal
                cage1.animal_space = animal.space
                cage1.space -= animal.space
                Cage.lst1.append(animal.name)
                return f'{True} cage1 {cage1.animal.name}'
            else:
                return f'{False} - мест нет cage1 {animal.name}'
        elif self == cage2:
            if cage2.space >= animal.space:
                cage2.animal = animal
                cage2.animal_space = animal.space
                cage2.space -= animal.space
                Cage.lst2.append(animal.name)
                return f'{True} cage2 {cage2.animal.name}'
            else:
                return f'{False} - мест нет cage2 {animal.name}'


    def get_animals(self):

        if self == cage1:
           return Cage.lst1
        elif self == cage2:
            return Cage.lst2


    def free_space(self):
        if self == cage1:
            return cage1.space
        else:
            return cage2.space



cage1 = Cage(300)
cage2 = Cage(200)

lion = Animal("Alex", 150)
pinguin1 = Animal("Gunter", 20)
pinguin2 = Animal("Ganter", 15)
pinguin3 = Animal("Ginter", 25)
begemoth = Animal("Gloria", 200)
giraffe = Animal("Melvin", 110)
zebra = Animal("Martin", 70)

print(cage1.add_animal(lion))      # True
print(cage2.add_animal(pinguin1))  # True
print(cage1.add_animal(pinguin2))  # True
print(cage2.add_animal(pinguin3))  # True
print(cage1.add_animal(begemoth))  # False
print(cage2.add_animal(giraffe))   # True
print(cage1.add_animal(zebra))     # True
print(cage1.free_space())          # 65
print(cage2.free_space())          # 45
print(cage1.get_animals())         # ['Alex', 'Ganter', 'Martin']
print(cage2.get_animals())         # ['Gunter', 'Ginter', 'Melvin']
