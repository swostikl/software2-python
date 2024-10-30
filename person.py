# Methods for inheritance
'''

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        pass



class Student(Person):
    def __init__(self, name, age, gender,student_id):
        super().__init__(name,age,gender)
        self.student_id = student_id


    def introduce(self):
        return f" I am {self.name}, {self.age}, {self.gender} and my id is {self.student_id}"


person=Student("Swostika",16,"female",2424)
print(person.introduce())



# Example of multiple inheritance
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        pass

class Student(Person):
    def __init__(self, name, age, gender, student_id):
        super().__init__(name, age, gender)
        self.student_id = student_id

    def introduce(self):
        pass


class Assistant(Student):
    def __init__(self, name, age, gender,student_id, salary):
        super().__init__(name, age, gender,student_id)
        self.student_id = student_id
        self.salary = salary

    def introduce(self):
        return f"I am {self.name}, {self.age}, {self.gender}, my id is {self.student_id} and my salary is {self.salary}"



assistant=Assistant("Swosti", 16, "female", 242, 3500)
print(assistant.introduce())


#Multilevel inheritance
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        pass

class Student(Person):
    def __init__(self, name, age, gender,student_id):
        super().__init__(name, age, gender)
        self.student_id = student_id

    def introduce(self):
        return f"I am {self.name}, {self.age}, {self.gender} and my id is {self.student_id}"


class Teacher(Person):
    def __init__(self, name, age, gender,title):
        super().__init__(name,age,gender)
        self.title = title

    def introduce(self):
        return f"I am {self.name}, {self.age}, {self.gender} and my title is {self.title}"


student=Student("Swostika" ,16 ,"Female" ,2424)
print(student.introduce())

teachers=[]
teacher1=Teacher("Amir" ,30 , "Male" ,"Professor")
teacher2= Teacher("Jonita",28,"female", "Teacher")

teachers.append(teacher1)
teachers.append(teacher2)

for teacher in teachers:
    print(teacher.introduce())




#hierarchial inheritance
class Person:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        pass

class Teacher(Person):
    def __init__(self,name,age,gender,title):
        super().__init__(name,age,gender)
        self.title = title

    def introduce(self):
        pass

class Assistant(Teacher):
    def __init__(self,name,age,gender,title,salary):
        super().__init__(name,age, gender,title)
        self.salary = salary

    def introduce(self):
        return f"I am {self.name}, {self.age}, {self.gender} and my salary is {self.salary}."


class PartTime(Teacher):
    def __init__(self,name,age,gender,title,hour):
        super().__init__(name,age,gender,title)
        self.hour = hour

    def introduce(self):
        return f"I am {self.name}, {self.age}, {self.gender} and I work for {self.hour} hours."

assistants=[]
assistant1=Assistant("Rama",16,"female","AT", 4000)
assistant2=Assistant("Deren",16,"male","AT", 4200)
assistants.append(assistant1)
assistants.append(assistant2)
for assistant in assistants:
    print(assistant.introduce())


part_times=[]
part_time1=PartTime("Shyam",16,"Male","PRT",4)
part_time2=PartTime("Radha",16,"Female","PRT",3)
part_times.append(part_time1)
part_times.append(part_time2)

for part_time in part_times:
    print(part_time.introduce())

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





