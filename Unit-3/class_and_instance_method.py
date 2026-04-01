class Student:
    school_name = "ABC School"

    def __init__(self, name):
        self.name = name

    def show_name(self):   # instance method
        print("Student Name:", self.name)

    @classmethod
    def show_school(cls):  # class method
        print("School Name:", cls.school_name)


s1 = Student("Mira")
s1.show_name()
Student.show_school()
