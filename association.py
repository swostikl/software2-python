# Programs where objects can interact with each other
class Dog:
    def __init__(self, name, birth_year , sound="woof woof"):
        self.name = name
        self.birth_year = birth_year
        self.sound = sound

    def bark(self, times):
        for i in range(times):
            print(self.name + "barks" + self.sound)
        return



class Hotel:
    def __init__(self):
        self.dogs=[]

    def dog_checkin(self, dog):
        self.dogs.append(dog)
        print(dog.name + "Check in")
        return

    def dog_checkout(self, dog):
        self.dogs.remove(dog)
        print(dog.name + "Check out")
        return
    def greet_dogs(self):
        for dog in self.dogs:
            dog.bark(2)
# main program
dog1 = Dog("Tommy" , 2020)
dog2 = Dog("Jim" , 2023)

hotel = Hotel()

hotel.dog_checkin(dog1)
hotel.dog_checkin(dog2)
hotel.greet_dogs()

hotel.dog_checkout(dog1)
hotel.greet_dogs()




