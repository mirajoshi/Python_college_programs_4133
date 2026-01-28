# 10.Write a program to create 4 lambda functions which shall accept 2 numbers and one arithmetic operator. As per arithmetic operator relatedlambda functions shall be invoked.

operations = [
    lambda a, b: a + b,
    lambda a, b: a - b,
    lambda a, b: a * b,
    lambda a, b: a / b
]

operators = ['+', '-', '*', '/']

a = int(input("Enter first number : "))
b = int(input("Enter second number: "))
opr = input("Enter operator (+, -, *, /): ")

if opr in operators:
    index = operators.index(opr)
    print("Result:", operations[index](a, b))
else:
    print("Invalid operator")
