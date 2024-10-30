# DID in Two different methods
#First method
class Member():
    def __init__(self, membership_id):
        self.membership_id = membership_id

    def introduce(self):
        pass



class Author():
    def __init__(self, books_written):
        self.books_written = books_written

    def introduce(self):
        pass

    def get_books_written(self):
        return self.books_written

class Person(Member, Author):
    def __init__(self,membership_id, books_written, name, age, gender):
        Member.__init__(self, membership_id)
        Author.__init__(self, books_written)
        self.name = name
        self.age = age
        self.gender = gender


    def introduce(self):
       return f"I am {self.name}, {self.age} years old, and i am {self.gender}"


class AuthorMember(Member,Author):
    def __init__(self, name, age, gender, membership_id, books_written):
        Member.__init__(self, membership_id)
        Author.__init__(self, books_written)
        Person.__init__( self,  membership_id, books_written, name, age, gender)

    def introduce(self):
        return f"I am {self.name}, {self.age}, {self.gender},and my membership is {self.membership_id} {self.books_written}"
author_members=[]
author_member1=AuthorMember("Ram", 40, "Male", 21, "'Magic of words' ,'science'")
author_member2=AuthorMember("Rita", 20, "Female", 21, "Magic of science")
author_members.append(author_member1)
author_members.append(author_member2)


for author_member in author_members:
    print(author_member.introduce())

books_written=[]
book1="Magic of words"
book2="Magic of science"
books_written.append(book1)
books_written.append(book2)

for book in books_written:
    print(book)

#Second Method
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        
    def introduce(self):
        pass

class Member(Person):
    def __init__(self,  name, age, gender,membership_id):
        Person.__init__(self,name, age, gender)
        self.membership_id = membership_id
        
        
    def introduce(self):
        pass
    
class Author(Person):
    def __init__(self, name, age, gender, books_written):
        Person.__init__(self, name, age , gender)
        self.books_written = books_written
        
    def introduce(self):
        pass
    

    
class AuthorMember(Member, Author):
    def __init__(self, name, age, gender, membership_id, books_written):
        Member.__init__(self,  name, age, gender, membership_id)
        Author.__init__(self,  name, age, gender, books_written)

    def introduce(self):
        return f"I am {self.name}, {self.age} years old, and i am {self.gender} and my membership is {self.membership_id} and wrote {self.books_written}"



members=[]
member1=AuthorMember("Ram", 40, "Male", 21, "Magic of words")
member2=AuthorMember("Rita", 20, "Female", 21, "Magic of science")
members.append(member1)
members.append(member2)
for member in members:
    print(member.introduce())
    





