class student:
    name = ""
    grade = ""

    def __init__(self, student_name, student_grade):
        self.name = student_name
        self.grade = student_grade
    
    def sukaBelajar(self, belajar):
        print(f"{self.name} kelas {self.grade} suka belajar {belajar}")

student1 = student("Balqis", "11D")
student1.sukaBelajar("Balagoh")