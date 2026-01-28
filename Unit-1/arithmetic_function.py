# Write a program to create a function which accepts 2 numbers and one arithmetic operator. Return the answer accordingly.

def calculate(nums, opr):
    a = nums[0]
    b = nums[1]

    if opr == '+':
        return a + b
    elif opr == '-':
        return a - b
    elif opr == '*':
        return a * b
    elif opr == '/':
        return a / b
    else:
        return "Invalid operator"

numbers = []
numbers.append(int(input("Enter first number: ")))
numbers.append(int(input("Enter second number: ")))

operator = input("Enter operator (+, -, *, /): ")

result = calculate(numbers, operator)
print("Result:", result)
