# Write a program to read file which has marks entry of student and display details with total, percentage and grade

def get_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"

f = open("students_data.txt", "r")
lines = f.readlines()
f.close()

for line in lines:
    line = line.strip()
    if line:
        data = line.split(",")
        roll = data[0]
        name= data[1]
        m1 = int(data[2])
        m2 = int(data[3])
        m3 = int(data[4])
        m4 = int(data[5])
        total = m1 + m2 + m3 + m4
        percentage = total / 4
        grade = get_grade(percentage)

        print("Roll No    :", roll)
        print("Name       :", name)
        print("Marks      :", m1, m2, m3, m4)
        print("Total      :", total)
        print("Percentage :", percentage)
        print("Grade      :", grade)
        print("-" * 30)
