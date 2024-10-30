# simple method revision
'''
class Animal:
    def __init__(self, name):
        self.name = name

    def print_information(self):
        print(f"{self.name}")

myAnimal = []
myAnimal.append(Animal("dog"))
myAnimal.append(Animal("cat"))
myAnimal.append(Animal("mouse"))

for animal in myAnimal:
    animal.print_information()


# Types of inheritance
# (Single inheritance) for example class animal and subclass : mammal
# Multiple inheritance A-B-C
# Hierarchical inheritance B and c is inherited from A
# Multiple inheritance ex. person having 2 qualities


# Single inheritance ( Parent class or base class)

class Animal:
    def __init__(self, name):
        self.name=name

    def speak(self):
        pass

    def print_information(self):
        print(f"{self.name}")


# Child class (or derived class) inheriting from animal

class Dog(Animal):

    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        return f"{self.name} says Woof!"

#create an instance of the Dof class
dog=Dog("Tashi")

# call the speak method of dog class
print(dog.speak())





# Grandparent Class

class Animal:
    def __init__(self, name):
        self.name=name

    def speak(self):
        pass

# Parent class inheriting from Animal

class Mammal(Animal):
    pass

# Child class inheriting from mammal

class Dog(Mammal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        return f"{self.name} says Woof!"

#main program
dog=Dog("Tashi")
print(dog.speak())





#Multiple Inheritance

class Animal:
    def __init__(self, name):
        self.name=name

    def introduce(self):
        pass


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def introduce(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def introduce(self):
        return f"{self.name} says Meow!"


dog=Dog("Tashi")
print(dog.introduce())

cat=Cat("kalu")
print(cat.introduce())




# Multilevel inheritance

class Animal:
    def __init__(self, name):
        self.name=name

    def speak(self):
        pass



class Mammal(Animal):
    def speak(self):
        pass


class Dog(Mammal):
    def speak(self):
        return f"{self.name} says Woof!"


class Cat(Mammal):

    def speak(self):
        return f"{self.name} says Meow!"


dog=Dog("Tashi")
print(dog.speak())

cat=Cat("kalu")
print(cat.speak())

'''



class Person:
    counter=0
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        Person.counter+=1

class Teacher:
    def __init__(self, teacher_title):
        self.teacher_title = teacher_title




class Student(Teacher,Person):
    def __init__(self,name, age, gender,teacher_title, student_id):
        Person.__init__(self, name, age, gender)
        Teacher.__init__(self,teacher_title)
        self.student_id = student_id

    def introduce(self):
        return f"I am {self.teacher_title}.I am {self.name}, {self.age}, {self.gender}, and my id is {self.student_id}."


student=Student("Tashi",40,"M","Professor","242")
print(student.introduce())

