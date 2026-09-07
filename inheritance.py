# inheritance ( miras alma,kalıtım)

class Person:
    def __init__(self,name,surname,age):
        self.name = name
        self.surname = surname
        self.age = age
        print("Person nesnesi oluşturuldu.")

    def info(self):
        print(self.name,self.surname,self.age)

class Student(Person):
    def __init__(self,name,surname,age,number):
        Person.__init__(self,name,surname,age)
        self.number = number
        print("Student nesnesi oluşturuldu.")
           
    

class Teacher(Person):
    def __init__(self, name, surname, age,branch):
        Person.__init__(self,name, surname, age)
        self.branch = branch
        print("Teacher nesnesi oluşturuldu.")

p1 = Person("Selim Emir","OCAK",23)
p1.info()
s1 = Student("Kerem","KOÇ",200)
s1.info()