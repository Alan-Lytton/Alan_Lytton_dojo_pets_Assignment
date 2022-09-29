import dojo_pet


class Ninja:

    def __init__(self, first_name, last_name, pet, treats, pet_food):
        self.f_name = first_name
        self.l_name = last_name
        self.pet = pet
        self.treats = treats
        self.pet_food = pet_food

    def walk(self):
        self.pet.play()
        return self

    def feed(self):
        self.pet.eat()
        return self

    def bathe(self):
        self.pet.noise()
        return self


alan_ninja = Ninja("Alan", "Lytton", dojo_pet.Pet("Mr. Snuffles", "Fox", "play dead", 50, 100), "Cookies", "Raw Meat")
seth_ninja = Ninja("Seth", "Johnson", dojo_pet.PetDog("Master Woofington", "roll over", 100, 100), "bisquit", "Kibble")
elyn_ninja = Ninja ("Elyn", "Roberts", dojo_pet.PetCat("Wiskers McWiskerson", "Absorb Sun", 5, 75), "cat nip", "Fancy Feast")

alan_ninja.feed().walk().bathe()
seth_ninja.bathe()
elyn_ninja.bathe()

