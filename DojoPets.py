
class Pet:

    def __init__(self, name, type, tricks):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.energy = 75
        self.health = 100

    def play (self):
        self.health += 5
        print(f"Playing has increased {self.name}'s health by {self.health}")
        return self

    def eat (self):
        self.energy += 5
        self.health += 10
        print(f"Eating has increased {self.name}'s energy and health by {self.energy} and {self.health}")
        return self

    def noise (self):
        print("Bailey is whinning from the bath")
        return self

    def sleep (self):
        self.energy += 25
        return self 


class Ninja:

    def __init__(self,first_name, last_name, pet, treats, pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet
        self.treats = treats 
        self.pet_food = pet_food 

    def walk (self,):

        self.pet.play()
        return self

    def feed(self):
        
        self.pet.eat()
        return self 

    def bathe(self):

        self.pet.noise()
        return self


bailey = Pet("Bailey", "Eskipoo", "dance") 
matt = Ninja("Matt", "Nothdurft", bailey , "bones", "dry food")

matt.walk().feed().bathe()