#Write a program to input p, r, n and find out interest using simple input

p = float(input("Enter principal amount: "))
r = float(input("Enter rate of interest: "))
n = float(input("Enter time (in years): "))

si = (p * r * n) / 100

print("Simple Interest is:", si)
