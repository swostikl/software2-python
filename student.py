class Student:
    department = 'Computer Science'
    count=0
    def __init__(self, first_name, last_name, age , gender):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender=gender
        Student.count+=1
       # self.email=f'{self.first_name}.{self.last_name}@metropolia.fi'

    def change_first_name(self, first_name):
        self.first_name = first_name
        return self.first_name

    def getfirst_name(self):
        return self.first_name

    def getlast_name(self, last_name):
        return self.last_name

    def get_age(self, age):
        return self.age

    def get_gender(self, gender):
        return self.gender


    def __str__(self):
        return f'Student name: {self.first_name} {self.last_name} {self.age} {self.gender}'


it=Student( "Suzy" , "Zhang", 20 , "Female")
it1=Student("Sharmila", "Gyawali",18,"Female")
it2=Student("Puun","Subhaani",16,"Male")
it3=Student("Swostika","lama",10, "Female")

#print(f" Student name  is {it.first_name} {it.last_name} is {it.age} years old and is {it.gender}")
it.change_first_name("Yue")
print({it.first_name})


print(str(it), Student.department)


print(f"Number of students created is : {Student.count}")


class Course:
    def __init__(self):
        self.Students=[]

    def add_student(self, student):
        self.Students.append(student)
        print(f"{student} added successfully")


    def remove_student(self, student):
        self.Students.remove(student)
        print(f"{student} removed successfully")

    def get_student(self):
        print(Student.get_first_name(), Student.get_last_name(), Student.get_age(), Student.get_gender())

Course1= Course()
Course2= Course()
Course1.add_student(it)
Course2.add_student(it1)

