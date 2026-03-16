import os

FILE = "students.txt"

def add_student():
    roll  = input("Enter Roll No: ")
    name  = input("Enter Name: ")
    marks = input("Enter Marks: ")
    f = open(FILE, "a")
    f.write(roll + "," + name + "," + marks + "\n")
    f.close()
    print("Student added successfully.")

def search_student():
    roll = input("Enter Roll No to serach:")
    if not os.path.exists(FILE):
        print("No records found.")
        return
    f = open(FILE, "r")
    lines = f.readlines()
    f.close()
    for line in lines:
        data = line.strip().split(",")
        if data[0] == roll:
            print("Roll No :", data[0])
            print("Name    :", data[1])
            print("Marks   :", data[2])
            return
    print("Student not found.")

def list_students():
    if not os.path.exists(FILE):
        print("No records found.")
        return
    f = open(FILE, "r")
    lines = f.readlines()
    f.close()
    if len(lines) == 0:
        print("No students available.")
        return
    for line in lines:
        data = line.strip().split(",")
        print("Roll No :", data[0], "| Name :", data[1], "| Marks :", data[2])

def update_student():
    roll = input("Enter Roll No to update: ")
    if not os.path.exists(FILE):
        print("No records found.")
        return
    f = open(FILE, "r")
    lines = f.readlines()
    f.close()
    updated = False
    f = open(FILE, "w")
    for line in lines:
        data = line.strip().split(",")
        if data[0] == roll:
            new_name  = input("Enter new Name: ")
            new_marks = input("Enter new Marks: ")
            f.write(data[0] + "," + new_name + "," + new_marks + "\n")
            updated = True
        else:
            f.write(line)
    f.close()
    if updated:
        print("Student updated successfully.")
    else:
        print("Student not found.")

def delete_student():
    roll = input("Enter Roll No to delete: ")
    if not os.path.exists(FILE):
        print("No records found.")
        return
    f = open(FILE, "r")
    lines = f.readlines()
    f.close()
    deleted = False
    f = open(FILE, "w")
    for line in lines:
        data = line.strip().split(",")
        if data[0] == roll:
            deleted = True
        else:
            f.write(line)
    f.close()
    if deleted:
        print("Student deleted successfully.")
    else:
        print("Student not found.")

while True:
    print("\n===== Student Menu =====")
    print("a) Add Student")
    print("b) Search Student")
    print("c) List All Students")
    print("d) Update Student")
    print("e) Delete Student")
    print("f) Exit")
    choice = input("Enter your choice: ")

    if choice == "a":
        add_student()
    elif choice == "b":
        search_student()
    elif choice == "c":
        list_students()
    elif choice == "d":
        update_student()
    elif choice == "e":
        delete_student()
    elif choice == "f":
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Try again.")
