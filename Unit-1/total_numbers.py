#Write a program to create function which shall accept any number of arguments and display total of all the numbers given as argument.

def total_numbers(*nums):
    total = 0
    for i in nums:
        total += i
    print("Total of given numbers is : ", total)

total_numbers(10, 20, 30)
total_numbers(5, 15, 25, 35)
