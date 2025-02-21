class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getInfo(self):
        print(f"This person's name is {self.name} and they are {self.age} years old.")

class Student(Person):
    def __init__(self, name, age, nis, grade):
        super().__init__(name, age) #memanggil kontruktor parent (person)
        self.nis = nis
        self.grade = grade
    
    def getInfo(self):
        print(f"This student's name is {self.name}, they are {self.age} years old, and they are in grade {self.grade}.")

    def study(self, subject):
        print(f"{self.name}is studying {subject}.")

    #Membuat objek dari kelas Person
    person1 = Person("Kamila", 17)
    person1.getInfo()

    #Membuat objek dari kelas Student
    student1 = Student("Leclerc", 19, "0781234329", "12th Grade")
    student1.getInfo()
    student1.study("Espanol") #Memanggil metode tambahan pada student