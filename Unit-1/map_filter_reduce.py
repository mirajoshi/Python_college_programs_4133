# Write a program to make use of map(), filter() and reduce() functions with context to lambda functions.

numbers = [1, 2, 3, 4, 5]

squares = list(map(lambda x: x * x, numbers))
print("Squares using map(): " , squares)

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers using filter():", even_numbers)

sum = 0
for i in numbers:
    sum += i

print("Sum using reduce logic:", sum)
