# Write a Python program to perform following operation on given string input:

# a) Count Number of Vowel in given string

s = input("Enter a string : ")
vowels = "aeiouAEIOU"
count = 0
for ch in s:
    if ch in vowels:
        count += 1
print("Number of vowels: ",count)

# b) Count Length of string (donot use len() )

length = 0
for ch in s:
    length += 1
print("Length of string : ",length)

# c) Reverse String

rev = ""
for ch in s:
    rev = ch + rev
print("Reversed string:", rev)

# d) Find and replace operation

find_char = input("Enter character to find : ")
replace_char = input("Enter character to replace with : ")

new_str = ""
for ch in s:
    if ch == find_char:
        new_str += replace_char
    else:
        new_str += ch
print("String after replace : ",new_str)

# e) Check palindrome

if s == rev:
    print("The string is palindrome")
else:
    print("The string is not palindrome")
