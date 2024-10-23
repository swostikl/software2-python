#Object-oriented lecture by Amir
'''
class Dog:
    pass
# We create a mydog object, constractor
mydog = Dog()

mydog.name="Tommy"
mydog.age=1
print(mydog.name,mydog.age)

yourdog = Dog()
yourdog.name="Tom"
yourdog.age=2
print(yourdog.name,yourdog.age)



class Dog:

    def __init__(self, name,age):
        self.name = name
        self.age = age

    def change_name(self, name):
        self.name = name

mydog = Dog("Tommy", 2)
yourdog = Dog("Tom", 1)

print(f"Dog's name is {mydog.name} is {mydog.age} years old")
mydog.change_name("Fuchu")
yourdog.change_name("Tashi")
print({mydog.name})

#<__main__.Dog object at 0x10320b5e0> gives this output that means it stored in memory and
# give the memory place number if written just print (mydog)

'''

class Dog:
    count=0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Dog.count+=1

    # setter and getter to manipulate the content of the attribute

    def change_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def __str__(self):
        return f"Dog's name is {self.name} is {self.age} years old"




mydog = Dog("Chicko", 2)
yourdog = Dog("Mi", 1)
hisdog = Dog("Snowy", 3)
herdog = Dog("Mikko", 4)
doglist=[mydog, yourdog, hisdog, herdog]


for dog in doglist:
    print(dog)
print(f"Dog's name is {mydog.name} is {mydog.age} years old")
mydog.change_name("mikko")
yourdog.change_name("hap")
print({mydog.name})

print(f'number of dogs created :{Dog.count}')
print(str(mydog))




class Nursing:
    def __init__(self):
        self.dogs = []

    def addDog(self, dog):
        self.dogs.append(dog)
        print(f"the {dog} is added")


    def removeDog(self, dog):
        self.dogs.remove(dog)
        print(f"the {dog} is removed")

    def getDog(self):
        for dog in self.dogs:
            print(dog.get_name(), dog.get_age())



nursing1= Nursing()
nursing2= Nursing()
nursing1.addDog(mydog)
nursing2.addDog(herdog)

