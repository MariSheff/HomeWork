
class Animal:
    def __init__(self, name, space):
        self.name = name
        self.space = space

    def __str__(self):
        return self.name


class Cage:
    #lst1 = [] 
    #lst2 = [] 
    def __init__(self, space, animal=None, animal_space=None):
        self.space = space
        self.lst = [] 
        self.animal_space = animal_space

    def add_animal(self, animal: Animal):
        if self.space >= animal.space:
            self. animal_space = animal.space
            self.space -= animal.space
            self.lst.append(animal.name)
            return f'{True} {animal.name}'
        else:
            return f'{False} - мест нет для {animal.name}'


    def get_animals(self):
        return self.lst


    def free_space(self):
        return self.space
  



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
