from abc import ABC, abstractmethod

class Printable(ABC):
    @abstractmethod
    def print_info(self):
        pass

    @abstractmethod
    def print_summary(self):
        pass


class Student(Printable):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_info(self):
        print("Student Name:", self.name)
        print("Student Age:", self.age)

    def print_summary(self):
        print("Summary: Student", self.name, "is", self.age, "years old.")


s = Student("Priya", 21)
s.print_info()
print()
s.print_summary()
