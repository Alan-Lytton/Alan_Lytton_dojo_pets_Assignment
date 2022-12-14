class Pet:

    def __init__(self, name, type, tricks, health, energy):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy

    def sleep(self):
        self.energy += 25
        return self

    def eat(self):
        self.energy += 5
        self.health += 10
        return self

    def play(self):
        self.health += 5
        return self

    def noise(self):
        print("What does the fox say?!")
        return self

class PetDog(Pet):
    
    def __init__(self, name, tricks, health, energy):
        super().__init__(name, type, tricks, health, energy)
        self.type = "Dog"

    def noise(self):
        print("Woof Woof!")

class PetCat(Pet):

    def __init__(self, name, tricks, health, energy):
        super().__init__(name, type, tricks, health, energy)
        self.type = "Cat"
    
    def noise(self):
        print("Meow...HISS!!!!")