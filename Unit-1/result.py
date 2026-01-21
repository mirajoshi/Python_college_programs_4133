# Result Calculation Program

m1 = float(input("Enter marks of subject 1: "))
m2 = float(input("Enter marks of subject 2: "))
m3 = float(input("Enter marks of subject 3: "))
m4 = float(input("Enter marks of subject 4: "))

total = m1 + m2 + m3 + m4
percentage = total / 4

if m1 >= 35 and m2 >= 35 and m3 >= 35 and m4 >= 35:
    result = "PASS"

    if percentage >= 75:
        grade = "A"
    elif percentage >= 60:
        grade = "B"
    elif percentage >= 50:
        grade = "C"
    else:
        grade = "D"
else:
    result = "FAIL"
    grade = "No Grade"

print("Total Marks:", total)
print("Percentage:", percentage)
print("Result:", result)
print("Grade:", grade)
