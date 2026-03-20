class Student:
    def AddStudent(self):
        self.roll_no = int(input("Enter Roll No : "))
        self.name = input("Enter Name : ")
        self.age = int(input("Enter Age : "))
        self.gender = input("Enter Gender : ")
        print(f"\nStudent '{self.name}' added successfully!")

    def DisplayStudent(self):
        print("\n--- Student Details ---")
        print(f"Roll No : {self.roll_no}")
        print(f"Name : {self.name}")
        print(f"Age : {self.age}")
        print(f"Gender : {self.gender}")
        print("-------------------------")

s1 = Student()
s1.AddStudent()
s1.DisplayStudent()

s2 = Student()
s2.AddStudent()
s2.DisplayStudent()
