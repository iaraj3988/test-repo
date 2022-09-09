

class animal:
    def __init__(self,animalname):
        self.animalname = animalname
class pets(animal):
    breed = 'german'
class dogs(pets):
    accury = 'normal'
    print(f'the details are correct:-')

a = animal
p  = pets
d = dogs
print(d.accury)

        