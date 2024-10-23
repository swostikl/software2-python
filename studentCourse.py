class Student:
    department="Computer Science"
    count=0
    def __init__(self, name,age,gender  ):
        self.name = name
        self.age = age
        self.gender = gender
        Student.count+=1
        self.courses=[]



    def __str__(self):
        return f'Student name: {self.name} {self.age} {self.gender}'

    def getname(self):
        return self.name

    def get_age(self):
        return self.age

    def get_gender(self):
        return self.gender

    def enrollCourse(self, course):
        self.courses.append(course)
        print(f"Course added {course}")

    def getCourse(self):
        return self.courses


student1=Student('Sailesh','18','Male')
student2=Student('Suzy','28','Female')
student3=Student('Puun','17','Male')
student4=Student('Samin','23','Female')

print(str(student1))
print(str(student2))
print(f"Number of students : {Student.count}")


class Course:
    def __init__(self,name):
        self.name=name
        self.students=[]


    def addStudent(self,student):
        self.students.append(student)
        print(f'The student {student.name} is added to {self.name}')

    def removeStudent(self,student):
        self.students.remove(student)
        print(f'The student {student.name} is removed from {self.name}')

    def getStudents(self):
        for student in self.students:
            print(student)


course1 = Course('Introduction to Computer Science')
course1.addStudent(student1)
course1.addStudent(student2)
course1.getStudents()



























